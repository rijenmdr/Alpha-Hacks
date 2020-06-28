import time
import cv2
import json
import datetime
from datetime import timezone
import numpy as np
from PIL import Image

import onnx
import pytorch_face_landmark.vision.utils.box_utils_numpy as box_utils
from caffe2.python.onnx import backend

# onnx runtime
import onnxruntime as ort

import torchvision.transforms as transforms
from pytorch_face_landmark.common.utils import BBox,drawLandmark,drawLandmark_multiple  # import libraries for landmark

from pytorch_face_landmark.feature_calculation import get_lip_height, get_mouth_height, check_mouth_open, eye_aspect_ratio

# setup the parameters
resize = transforms.Resize([112, 112])
to_tensor = transforms.ToTensor()

# Mouth open landmarks indexes
outer_lip_coordinates =  [48, 49, 50, 51, 52, 53, 54, 64, 63, 62, 61, 60]
inner_lip_coordinates = [54, 55, 56, 57, 58, 59, 48, 60, 67, 66, 65, 64]

# Eye landmarks indexes
right_eye_idx = [36, 37, 38, 39, 40, 41]
left_eye_idx = [42, 43, 44, 45, 46, 47]

# Eye blink Params 
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 3
COUNTER = 0
TOTAL = 0

# import the landmark detection models
import onnx
import onnxruntime
onnx_model_landmark = onnx.load("pytorch_face_landmark/pfld.onnx")
onnx.checker.check_model(onnx_model_landmark)
ort_session_landmark = onnxruntime.InferenceSession("pytorch_face_landmark/pfld.onnx")
def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

# face detection setting
def predict(width, height, confidences, boxes, prob_threshold, iou_threshold=0.3, top_k=-1):
    boxes = boxes[0]
    confidences = confidences[0]
    picked_box_probs = []
    picked_labels = []
    for class_index in range(1, confidences.shape[1]):
        probs = confidences[:, class_index]
        mask = probs > prob_threshold
        probs = probs[mask]
        if probs.shape[0] == 0:
            continue
        subset_boxes = boxes[mask, :]
        box_probs = np.concatenate([subset_boxes, probs.reshape(-1, 1)], axis=1)
        box_probs = box_utils.hard_nms(box_probs,
                                       iou_threshold=iou_threshold,
                                       top_k=top_k,
                                       )
        picked_box_probs.append(box_probs)
        picked_labels.extend([class_index] * box_probs.shape[0])
    if not picked_box_probs:
        return np.array([]), np.array([]), np.array([])
    picked_box_probs = np.concatenate(picked_box_probs)
    picked_box_probs[:, 0] *= width
    picked_box_probs[:, 1] *= height
    picked_box_probs[:, 2] *= width
    picked_box_probs[:, 3] *= height
    return picked_box_probs[:, :4].astype(np.int32), np.array(picked_labels), picked_box_probs[:, 4]





label_path = "pytorch_face_landmark/models/voc-model-labels.txt"

onnx_path = "pytorch_face_landmark/models/onnx/version-RFB-320.onnx"
class_names = [name.strip() for name in open(label_path).readlines()]

predictor = onnx.load(onnx_path)
onnx.checker.check_model(predictor)
onnx.helper.printable_graph(predictor.graph)
predictor = backend.prepare(predictor, device="CPU")  # default CPU

ort_session = ort.InferenceSession(onnx_path)
input_name = ort_session.get_inputs()[0].name

# perform face detection and alignment from camera
cap = cv2.VideoCapture(0)  # capture from camera
threshold = 0.7


attention_features = []
start_time = time.time()

start_dt = datetime.datetime.now() 
start_utc_time = start_dt.replace(tzinfo = timezone.utc) 
start_utc_timestamp = start_utc_time.timestamp()

session_extracted_features = {"date_time": start_utc_timestamp}
sum = 0
while True:
    ret, orig_image = cap.read()
    if orig_image is None:
        print("no img")
        break
    image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (320, 240))
    # image = cv2.resize(image, (640, 480))
    image_mean = np.array([127, 127, 127])
    image = (image - image_mean) / 128
    image = np.transpose(image, [2, 0, 1])
    image = np.expand_dims(image, axis=0)
    image = image.astype(np.float32)
    # confidences, boxes = predictor.run(image)
    time_time = time.time()
    confidences, boxes = ort_session.run(None, {input_name: image})
    # print("cost time:{}".format(time.time() - time_time))
    boxes, labels, probs = predict(orig_image.shape[1], orig_image.shape[0], confidences, boxes, threshold)

    if all(boxes.shape):
        if boxes.shape[0] == 1: 
            face_detected = "Single"
        elif boxes.shape[0] > 1:
            face_detected = "Multiple"
    elif boxes.shape[0] < 1:
        face_detected = "None Faces"
        print("Face Not Detected")

    tmp_features_collect = {"face": face_detected}
    
    for i in range(boxes.shape[0]):
        box = boxes[i, :]
        label = f"{class_names[labels[i]]}: {probs[i]:.2f}"

        #cv2.rectangle(orig_image, (box[0], box[1]), (box[2], box[3]), (255, 255, 0), 4)
        # perform landmark detection
        out_size = 56
        img=orig_image.copy()
        height,width,_=img.shape
        x1=box[0]
        y1=box[1]
        x2=box[2]
        y2=box[3]
        w = x2 - x1 + 1
        h = y2 - y1 + 1
        size = int(max([w, h])*1.1)
        cx = x1 + w//2
        cy = y1 + h//2
        x1 = cx - size//2
        x2 = x1 + size
        y1 = cy - size//2
        y2 = y1 + size
        dx = max(0, -x1)
        dy = max(0, -y1)
        x1 = max(0, x1)
        y1 = max(0, y1)

        edx = max(0, x2 - width)
        edy = max(0, y2 - height)
        x2 = min(width, x2)
        y2 = min(height, y2)   
        new_bbox = list(map(int, [x1, x2, y1, y2]))
        new_bbox = BBox(new_bbox)
        cropped=img[new_bbox.top:new_bbox.bottom,new_bbox.left:new_bbox.right]
        if (dx > 0 or dy > 0 or edx > 0 or edy > 0):
            cropped = cv2.copyMakeBorder(cropped, int(dy), int(edy), int(dx), int(edx), cv2.BORDER_CONSTANT, 0)            
        cropped_face = cv2.resize(cropped, (out_size, out_size))

        if cropped_face.shape[0]<=0 or cropped_face.shape[1]<=0:
            continue
        cropped_face = cv2.cvtColor(cropped_face, cv2.COLOR_BGR2RGB)    
        cropped_face = Image.fromarray(cropped_face)
        test_face = resize(cropped_face)
        test_face = to_tensor(test_face)
        #test_face = normalize(test_face)
        test_face.unsqueeze_(0)

        start = time.time()             
        ort_inputs = {ort_session.get_inputs()[0].name: to_numpy(test_face)}
        ort_outs = ort_session_landmark.run(None, ort_inputs)
        end = time.time()
        # print('Time: {:.6f}s.'.format(end - start))
        landmark = ort_outs[0]
        landmark = landmark.reshape(-1,2)
        landmark = new_bbox.reprojectLandmark(landmark)


        outer_lip_landmarks = [tuple(landmark[landmark_cord]) for landmark_cord in outer_lip_coordinates]
        inner_lip_landmarks = [tuple(landmark[landmark_cord]) for landmark_cord in inner_lip_coordinates]
 
        # print('mouth height: %.2f' % get_mouth_height(outer_lip_landmarks, inner_lip_landmarks))
        # print('Is mouth open:', check_mouth_open(outer_lip_landmarks, inner_lip_landmarks) )

        left_eye = [tuple(landmark[eye_landmark]) for eye_landmark in left_eye_idx]
        right_eye = [tuple(landmark[eye_landmark]) for eye_landmark in right_eye_idx]
        
        leftEAR = eye_aspect_ratio(left_eye)
        rightEAR = eye_aspect_ratio(right_eye)
		# average the eye aspect ratio together for both eyes
        ear = (leftEAR + rightEAR) / 2.0

        if ear < EYE_AR_THRESH:
            eye_stat = "closed"
            tmp_features_collect['eye_status'] = eye_stat

            COUNTER += 1
        else:
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                eye_stat = "open"
                tmp_features_collect['eye_status'] = eye_stat

                TOTAL += 1
                COUNTER = 0
                
        
        tmp_features_collect['yawning'] = check_mouth_open(outer_lip_landmarks, inner_lip_landmarks)
        tmp_features_collect["time_stamp"] = time.time() - start_time
        attention_features.append(tmp_features_collect)

        orig_image = drawLandmark_multiple(orig_image, new_bbox, landmark)

    # attention_features.append(time.time() - start_time)
    print("Total Features {}".format(attention_features))

    sum += boxes.shape[0]
    orig_image = cv2.resize(orig_image, (0, 0), fx=0.7, fy=0.7)
    cv2.imshow('annotated', orig_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        end_dt = datetime.datetime.now() 
        end_utc_time = end_dt.replace(tzinfo = timezone.utc) 
        end_utc_timestamp = end_utc_time.timestamp()

        session_extracted_features['attention_features'] = attention_features
        session_extracted_features["end_datet_time"] = end_utc_timestamp

        with open("feature_collect.json", "w") as jdump:
            json.dump(session_extracted_features, jdump)
        print("Total Features {}".format(attention_features))

        break
cap.release()
cv2.destroyAllWindows()
print("sum:{}".format(sum))
