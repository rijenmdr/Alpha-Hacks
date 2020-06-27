<template>
  <div class="main-content" id="panel">
    <div class="header pb-6">
      <section id="login">
        <div class="container mt-3 mb-3">
          <div class="row">
            <div class="col-md-3 mx-auto">
              <div class="card">
                <div class="card-header">
                  <h4>Home Page</h4>
                </div>
                <div class="card-body">
                  <div class="form-group" :class="{invalid:$v.nameOfSiteH.$error}">
                    <input
                      @blur="$v.nameOfSiteH.$touch()"
                      type="text"
                      class="form-control"
                      v-model="nameOfSiteH"
                      placeholder="Name of Website"
                    />
                    <div v-if="$v.nameOfSiteH.$error" class="error">Please enter valid name of Site</div>
                    <div v-if="$v.nameOfSiteH.$model" class="info">This will be name of your Site</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.category.$error}">
                    <input
                      @blur="$v.category.$touch()"
                      type="text"
                      class="form-control"
                      v-model="category"
                      placeholder="Category"
                    />
                    <div v-if="$v.category.$error" class="error">Please enter valid category</div>
                    <div v-if="$v.category.$model" class="info">This will be category</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.headingOneH.$error}">
                    <input
                      @blur="$v.headingOneH.$touch()"
                      type="text"
                      class="form-control"
                      v-model="headingOneH"
                      placeholder="heading one"
                    />
                    <div v-if="$v.headingOneH.$error" class="error">Please enter valid Heading</div>
                    <div v-if="$v.headingOneH.$model" class="info">This will be Heading One</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.descriptionOneH.$error}">
                    <textarea
                      @blur="$v.descriptionOneH.$touch()"
                      rows="3"
                      class="form-control"
                      v-model="descriptionOneH"
                      placeholder="description one"
                    />
                    <div
                      v-if="$v.descriptionOneH.$error"
                      class="error"
                    >Please enter valid Description</div>
                    <div v-if="$v.descriptionOneH.$model" class="info">This will be description</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.headingTwoH.$error}">
                    <input
                      @blur="$v.headingTwoH.$touch()"
                      type="text"
                      class="form-control"
                      v-model="headingTwoH"
                      placeholder="heading two"
                    />
                    <div v-if="$v.headingTwoH.$error" class="error">Please enter valid Heading</div>
                    <div v-if="$v.headingTwoH.$model" class="info">This will be heading two</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.descriptionTwoH.$error}">
                    <textarea
                      @blur="$v.descriptionTwoH.$touch()"
                      rows="3"
                      class="form-control"
                      v-model="descriptionTwoH"
                      placeholder="description two"
                    />
                    <div
                      v-if="$v.descriptionTwoH.$error"
                      class="error"
                    >Please enter valid Description</div>
                    <div v-if="$v.descriptionTwoH.$model" class="info">This will be Description</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.headingThreeH.$error}">
                    <input
                      @blur="$v.headingThreeH.$touch()"
                      type="text"
                      class="form-control"
                      v-model="headingThreeH"
                      placeholder="heading three"
                    />
                    <div
                      v-if="$v.headingThreeH.$error"
                      class="error"
                    >Please enter valid Heading three</div>
                    <div v-if="$v.headingThreeH.$model" class="info">This will be Heading three</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.descriptionThreeH.$error}">
                    <textarea
                      @blur="$v.descriptionThreeH.$touch()"
                      rows="3"
                      class="form-control"
                      v-model="descriptionThreeH"
                      placeholder="description three"
                    />
                    <div
                      v-if="$v.descriptionThreeH.$error"
                      class="error"
                    >Please enter valid Description</div>
                    <div v-if="$v.descriptionThreeH.$model" class="info">This will be Description</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.featureOneH.$error}">
                    <input
                      @blur="$v.featureOneH.$touch()"
                      type="text"
                      class="form-control"
                      v-model="featureOneH"
                      placeholder="feature one"
                    />
                    <div v-if="$v.featureOneH.$error" class="error">Please enter valid Feature</div>
                    <div v-if="$v.featureOneH.$model" class="info">This will be feature one</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.featureOneDesH.$error}">
                    <textarea
                      @blur="$v.featureOneDesH.$touch()"
                      rows="3"
                      class="form-control"
                      v-model="featureOneDesH"
                      placeholder="feature description"
                    />
                    <div
                      v-if="$v.featureOneDesH.$error"
                      class="error"
                    >Please enter valid description</div>
                    <div v-if="$v.featureOneDesH.$model" class="info">This will be description</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.featureTwoH.$error}">
                    <input
                      @blur="$v.featureTwoH.$touch()"
                      type="text"
                      class="form-control"
                      v-model="featureTwoH"
                      placeholder="feature two"
                    />
                    <div v-if="$v.featureTwoH.$error" class="error">Please enter valid feature two</div>
                    <div v-if="$v.featureTwoH.$model" class="info">This will be feature two</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.featureTwoDesH.$error}">
                    <textarea
                      @blur="$v.featureTwoDesH.$touch()"
                      rows="3"
                      class="form-control"
                      v-model="featureTwoDesH"
                      placeholder="feature description"
                    />
                    <div
                      v-if="$v.featureTwoDesH.$error"
                      class="error"
                    >Please enter valid description</div>
                    <div v-if="$v.featureTwoDesH.$model" class="info">This will be description</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.featureThreeH.$error}">
                    <input
                      @blur="$v.featureThreeH.$touch()"
                      type="text"
                      class="form-control"
                      v-model="featureThreeH"
                      placeholder="Feature three"
                    />
                    <div
                      v-if="$v.featureThreeH.$error"
                      class="error"
                    >Please enter valid feature three</div>
                    <div v-if="$v.featureThreeH.$model" class="info">This will be feature three</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.featureThreeDesH.$error}">
                    <textarea
                      @blur="$v.featureThreeDesH.$touch()"
                      rows="3"
                      class="form-control"
                      v-model="featureThreeDesH"
                      placeholder="feature description"
                    />
                    <div
                      v-if="$v.featureThreeDesH.$error"
                      class="error"
                    >Please enter valid description</div>
                    <div v-if="$v.featureThreeDesH.$model" class="info">This will be description</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="col-md-3 mx-auto">
              <div class="card">
                <div class="card-header">
                  <h4>About Page</h4>
                </div>
                <div class="card-body">
                  <div class="form-group" :class="{invalid:$v.introductionA.$error}">
                    <textarea
                      @blur="$v.introductionA.$touch()"
                      rows="3"
                      class="form-control"
                      v-model="introductionA"
                      placeholder="Introduction"
                    />
                    <div
                      v-if="$v.introductionA.$error"
                      class="error"
                    >Please enter valid Introduction</div>
                    <div v-if="$v.introductionA.$model" class="info">This will be Introduction</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.whatWeDoA.$error}">
                    <textarea
                      @blur="$v.whatWeDoA.$touch()"
                      rows="10"
                      class="form-control"
                      v-model="whatWeDoA"
                      placeholder="What we do"
                    />
                    <div v-if="$v.whatWeDoA.$error" class="error">Please enter valid description</div>
                    <div v-if="$v.whatWeDoA.$model" class="info">This will be description</div>
                  </div>
                </div>
                <div class="card-header">
                  <h4>Background Color</h4>
                </div>
                <div class="card-body">
                  <div class="form-group">
                    <select v-model="backgroundColor" class="form-control form-control">
                      <option value="green">Green</option>
                      <option value="#30332E">Black</option>
                      <option value="#DECA04">Yellow</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-3 mx-auto">
              <div class="card">
                <div class="card-header">
                  <h4>Service Page</h4>
                </div>
                <div class="card-body">
                  <div class="form-group" :class="{invalid:$v.serviceOne.$error}">
                    <input
                      @blur="$v.serviceOne.$touch()"
                      type="text"
                      class="form-control"
                      v-model="serviceOne"
                      placeholder="Service One"
                    />
                    <div v-if="$v.serviceOne.$error" class="error">Please enter valid Service</div>
                    <div v-if="$v.serviceOne.$model" class="info">This will be Service One</div>
                  </div>

                  <div class="form-group" :class="{invalid:$v.serviceOneDes.$error}">
                    <textarea
                      @blur="$v.serviceOneDes.$touch()"
                      rows="3"
                      class="form-control"
                      v-model="serviceOneDes"
                      placeholder="description of service one"
                    />
                    <div v-if="$v.serviceOneDes.$error" class="error">Please enter valid description</div>
                    <div v-if="$v.serviceOneDes.$model" class="info">This will be description</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.serviceTwo.$error}">
                    <input
                      @blur="$v.serviceTwo.$touch()"
                      type="text"
                      class="form-control"
                      v-model="serviceTwo"
                      placeholder="service two"
                    />
                    <div v-if="$v.serviceTwo.$error" class="error">Please enter valid Service two</div>
                    <div v-if="$v.serviceTwo.$model" class="info">This will be service two</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.serviceTwoDes.$error}">
                    <textarea
                      @blur="$v.serviceTwoDes.$touch()"
                      rows="3"
                      class="form-control"
                      v-model="serviceTwoDes"
                      placeholder="description two"
                    />
                    <div v-if="$v.serviceTwoDes.$error" class="error">Please enter valid description</div>
                    <div v-if="$v.serviceTwoDes.$model" class="info">This will be description</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.serviceThree.$error}">
                    <input
                      @blur="$v.serviceThree.$touch()"
                      type="text"
                      class="form-control"
                      v-model="serviceThree"
                      placeholder="service three"
                    />
                    <div
                      v-if="$v.serviceThree.$error"
                      class="error"
                    >Please enter valid Service three</div>
                    <div v-if="$v.serviceThree.$model" class="info">This will be Service three</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.serviceThreeDes.$error}">
                    <textarea
                      @blur="$v.serviceThreeDes.$touch()"
                      rows="3"
                      class="form-control"
                      v-model="serviceThreeDes"
                      placeholder="description of service three"
                    />
                    <div
                      v-if="$v.serviceThreeDes.$error"
                      class="error"
                    >Please enter valid description</div>
                    <div v-if="$v.serviceThreeDes.$model" class="info">This will be description</div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-3 mx-auto">
              <div class="card">
                <div class="card-header">
                  <h4>Contact Page</h4>
                </div>
                <div class="card-body">
                  <div class="form-group" :class="{invalid:$v.titleC.$error}">
                    <input
                      @blur="$v.titleC.$touch()"
                      type="text"
                      class="form-control"
                      v-model="titleC"
                      placeholder="title"
                    />
                     <div v-if="$v.titleC.$error" class="error">Please enter valid title</div>
                    <div v-if="$v.titleC.$model" class="info">This will be title in contact page</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.descriptionC.$error}">
                    <textarea
                      @blur="$v.descriptionC.$touch()"
                      rows="6"
                      class="form-control"
                      v-model="descriptionC"
                      placeholder="description"
                    />
                     <div v-if="$v.descriptionC.$error" class="error">Please enter valid description</div>
                    <div v-if="$v.descriptionC.$model" class="info">This will be description</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.emailC.$error}">
                    <input
                      @blur="$v.emailC.$touch()"
                      type="text"
                      class="form-control"
                      v-model="emailC"
                      placeholder="email"
                    />
                     <div v-if="$v.emailC.$error" class="error">Please enter valid email</div>
                    <div v-if="$v.emailC.$model" class="info">This will be email</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.phoneC.$error}">
                    <input
                      @blur="$v.phoneC.$touch()"
                      type="number"
                      class="form-control"
                      v-model="phoneC"
                      placeholder="phone"
                    />
                     <div v-if="$v.phoneC.$error" class="error">Please enter valid Phone</div>
                    <div v-if="$v.phoneC.$model" class="info">This will be Phone</div>
                  </div>
                  <div class="form-group" :class="{invalid:$v.addressC.$error}">
                    <input
                      @blur="$v.addressC.$touch()"
                      type="text"
                      class="form-control"
                      v-model="addressC"
                      placeholder="address"
                    />
                     <div v-if="$v.addressC.$error" class="error">Please enter valid address</div>
                    <div v-if="$v.addressC.$model" class="info">This will be address</div>
                  </div>

                  <div v-if="!$v.$invalid" class="form-group">
                    <button
                      @click="createWebsite"
                      class="btn bg-success text-white btn-block border-white"
                    >Create</button>
                  </div>
                   <div v-else class="form-group">
                    <button
                      
                      class="btn bg-success text-white btn-block border-white"
                    >Fill Up Data</button>
                  </div>
                  <div class="form-group">
                    <button
                      @click="dashboard"
                      class="btn bg-danger text-white btn-block border-white"
                    >Cancel</button>
                  </div>
                </div>
              </div>
            </div>

            <div class="col-md-3 mx-auto"></div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import host from '../../../host.js'
import {
  required,
  email,
  maxLength,
  minLength
} from "vuelidate/lib/validators";
export default {
  data() {
    return {
      category: "",
      nameOfSiteH: "",
      headingOneH: "",
      descriptionOneH: "",
      headingTwoH: "",
      descriptionTwoH: "",
      headingThreeH: "",
      descriptionThreeH: "",
      featureOneH: "",
      featureTwoH: "",
      featureThreeH: "",
      introductionA: "",
      whatWeDoA: "",
      titleC: "",
      emailC: "",
      descriptionC: "",
      phoneC: "",
      addressC: "",
      featureOneDesH: "",
      featureTwoDesH: "",
      featureThreeDesH: "",
      serviceOne: "",
      serviceTwo: "",
      serviceOneDes: "",
      serviceTwoDes: "",
      serviceThree: "",
      serviceThreeDes: "",
      backgroundColor: ""
    };
  },
  validations: {
    nameOfSiteH: { required },
    category: { required },
    headingOneH: { required },
    descriptionOneH: { required },
    headingTwoH: { required },
    descriptionTwoH: { required },
    headingThreeH: { required },
    descriptionThreeH: { required },
    featureOneH: { required },
    featureOneDesH: { required },
    featureTwoH: { required },
    featureTwoDesH: { required },
    featureThreeH: { required },
    featureThreeDesH: { required },
    introductionA: { required },
    whatWeDoA: { required },
    serviceOne: { required },
    serviceTwo: { required },
    serviceThree: { required },
    serviceOneDes: { required },
    serviceTwoDes: { required },
    serviceThreeDes: { required },
    titleC: { required },
    descriptionC: { required },
    phoneC: { required },
    emailC: { required },
    addressC: { required }
  },
  created() {
    //yeslay 2 hrs khayo . default ma value bind  nahune bug raixa so created ma value change garayrw garayko

    this.backgroundColor = "green";
  },
  methods: {
    dashboard() {
      this.$router.push("/dashboard");
    },
    onFileChanged(event) {
      console.log(event.target.files[0]);
    },
    async createWebsite() {
      let JWTToken = localStorage.getItem("token");
      if (!JWTToken) {
        JWTToken = this.$store.getters.getToken;
      }
      await axios
        .post(host.host+
          "/api/add_website",

          {
            category: this.category,
            nameOfSiteH: this.nameOfSiteH,
            headingOneH: this.headingOneH,
            descriptionOneH: this.descriptionOneH,
            headingTwoH: this.headingTwoH,
            descriptionTwoH: this.descriptionTwoH,
            headingThreeH: this.headingThreeH,
            descriptionThreeH: this.descriptionThreeH,
            featureOneH: this.featureOneH,
            featureTwoH: this.featureTwoH,
            featureThreeH: this.featureThreeH,
            introductionA: this.introductionA,
            whatWeDoA: this.whatWeDoA,
            titleC: this.titleC,
            emailC: this.emailC,
            descriptionC: this.descriptionC,
            phoneC: this.phoneC,
            addressC: this.addressC,
            user: this.$store.getters.getUser,
            featureOneDesH: this.featureOneDesH,
            featureTwoDesH: this.featureTwoDesH,
            featureThreeDesH: this.featureThreeDesH,
            serviceOne: this.serviceOne,
            serviceTwo: this.serviceTwo,
            serviceThree: this.serviceThree,
            serviceOneDes: this.serviceOneDes,
            serviceTwoDes: this.serviceTwoDes,
            serviceThreeDes: this.serviceThreeDes,
            backgroundColor: this.backgroundColor
          },
          {
            headers: {
              Authorization: `Token ${JWTToken}`
            }
          }
        )
        .then(res => {
          this.$store.dispatch("addNotifications", {
            type: "success",
            message: "This is the view of your new website"
          });
          this.$store.dispatch("setId", res.data.website.id);
          this.$router.push("/userWebsite/" + res.data.website.id);
        })
        .catch(err => {
          console.log("err");
          console.log(err);
        });
    }
  }
};
</script>
<style scoped>
input:focus,
select:focus,
textarea:focus {
  outline: none;
  box-shadow: none !important;
  -moz-box-shadow: none !important;
  -webkit-box-shadow: none !important;
  -o-box-shadow: none !important;
  -ms-box-shadow: none !important;
}
.invalid input {
  border: 1px solid red;
}

.invalid textarea {
  border: 1px solid red;
}
@import url("https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap");
.error {
  font-size: 15px;
  text-align: center;
  color: #f04104;
  font-family: "Patrick Hand", cursive;
}
.info {
  font-size: 15px;
  text-align: center;
  color: #32f004;
  font-family: "Patrick Hand", cursive;
}
</style>