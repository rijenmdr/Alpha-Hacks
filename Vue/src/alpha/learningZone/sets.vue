<template>
  <div class="main-content" id="panel">
    <!-- Header -->
    <!-- Header -->
    <div></div>
    <button
      type="button"
      class="btn readmore"
      data-toggle="modal"
      data-target="#exampleModalLong"
    >Read More</button>
    <div class="container mb-5">
      <div class="container-fluid">
        <div class="container">
          <div v-if="stats!='present'" class="row mt-5"></div>
          <div v-if="stats!='present'" class="row mt-2"></div>
          <div class="row mt-5">
            <div class="col-md-6">
              <div class="pr-md-5">
                <h3>Key Learnings</h3>
                <p>
                  In mathematics set is defined as the collection of well defined object which can be separated distinctly.
                  For instance,
                  S = {2, 4, 6, 8} is collection of the even integers.
                </p>
                <ul class="list-unstyled mt-5">
                  <li class="py-2">
                    <div class="d-flex align-items-center">
                      <h6 class="mb-0">A set can be explained in different ways:</h6>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="d-flex align-items-center">
                      <h6 class="mb-0">i. Listing method: A = {a, b, c, .z}</h6>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="d-flex align-items-center">
                      <h6 class="mb-0">ii. Descriptive method: N = {the natural numbersfrom 1 to 50}</h6>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="d-flex align-items-center">
                      <h6 class="mb-0">iii. Set builder method: A – B= A -(A∩ B )</h6>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="d-flex align-items-center">
                      <h6 class="mb-0">iv. Venn – diagram</h6>
                    </div>
                  </li>
                </ul>
              </div>
            </div>

            <div class="col-lg-6 mt-5">
              <iframe width="420" height="345" src="https://www.youtube.com/embed/hJgSUe1CTs4"></iframe>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="stats=='present'" class="header bg-primary pb-0">
      <div class="row">
        <div class="col-xl-7 col-md-6 mt-3 mb-3 margin">
          <div class="card card-stats">
            <!-- Card body -->
            <div class="card-body">
              <div class="row">
                <div class="col">
                  <h5 class="card-title text-uppercase text-muted mb-0">Recommendations :</h5>
                </div>
                <div class="col-auto"></div>
              </div>
              <div>
                <a target="_blank" class="mt-3 mb-0 text-sm">https://en.wikipedia.org/wiki/Nepal</a>
              </div>
              <div>
                <a
                  target="_blank"
                  class="mt-3 mb-0 text-sm"
                >https://www.youtube.com/watch?v=3YTo6Oa1XcY</a>
              </div>
              <div>
                <a
                  target="_blank"
                  class="mt-3 mb-0 text-sm"
                >https://www.youtube.com/watch?v=3YTo6Oa1XcY</a>
              </div>
            </div>
          </div>
        </div>

        <div class="col-xl-3 col-md-6 ml-5 mt-1">
          <div class="card card-stats">
            <!-- Card body -->
            <div class="card-body">
              <div class="row">
                <div>
                  <apexchart width="180" type="line" :options="options" :series="series"></apexchart>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="stats!='present'" class="button">
      <base-button
        tag="button"
        type="primary"
        class="mt-4"
        data-toggle="modal"
        data-target="#entermonitormode"
      >Enter Monitor Mode</base-button>
    </div>
    <div v-else class="buttonchat">
      <base-button
        tag="button"
        type="primary"
        class="mt-4"
        data-toggle="modal"
        data-target="#chat"
      >Any Questions ?</base-button>
    </div>
    <!-- Modal -->
    <div
      class="modal fade"
      id="entermonitormode"
      tabindex="-1"
      role="dialog"
      aria-labelledby="exampleModalCenterTitle"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">Would You Like To Enable Monitor Mode</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div
            class="modal-body"
          >We use camera to monitor your activity to calculate your contentration index that helps to enhance your learning efficiency and experience</div>
          <div class="modal-footer">
            <button data-dismiss="modal" type="button" @click="YES" class="btn btn-primary">OK</button>
          </div>
        </div>
      </div>
    </div>
    <!-- Modal -->
    <div
      class="modal fade"
      id="disablemonitormode"
      tabindex="-1"
      role="dialog"
      aria-labelledby="exampleModalCenterTitle"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">Are you sure to Disable Monitor Mode</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div
            class="modal-body"
          >We use camera to monitor your activity to calculate your contentration index that helps to enhance your learning efficiency and experience</div>
          <div class="modal-footer">
            <button data-dismiss="modal" type="button" @click="DISYES" class="btn btn-primary">OK</button>
          </div>
        </div>
      </div>
    </div>
    <!-- Modal -->
    <div
      class="modal fade"
      id="chat"
      tabindex="-1"
      role="dialog"
      aria-labelledby="exampleModalCenterTitle"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">Enter Your Querry..</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <textarea rows="5" cols="50"></textarea>
          </div>
          <div class="modal-footer">
            <button data-dismiss="modal" type="button" class="btn btn-primary">OK</button>
          </div>
        </div>
      </div>
    </div>
    <!-- Modal -->
    <div
      class="modal fade"
      id="exampleModalLong"
      tabindex="-1"
      role="dialog"
      aria-labelledby="exampleModalLongTitle"
      aria-hidden="true"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">Modal title</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <h5>Universal sets</h5>
            <p>A universal set is the collection of all objects in a particular context or theory. All other sets in that framework constitute subsets of the universal set, which is denoted as letter U. The objects themselves are known as elements or members of U.</p>
            <h5>Subsets</h5>
            <p>The set made by elements of the universal sets is called subsets of the universal sets
            For example</p>
            <p>U = {1, 2, 3, 4, …………..50}</p>
            <p>A = {even integers from 1 to 50}</p>
           <p> B= {odd numbers from 1 to 50}</p>
           <p> Here, A and B are the subsets of U=</p>
           <h5> Overlapping sets </h5>
            <p>Two sets are said to be overlapped if they have same element in common.
           <p> A∩ B = {6}
            A and B are overlapping sets.
            Disjoint sets
            Two sets are said to be disjoint sets if there is no element in common.
            Cardinality of the sets
            The number of the elements in the given sets is known as cardinality of sets.</p>
            A = {1, 2, 5,}
            B = {5, 3, 4}
            AUB = {1, 2, 3, 4, 5}
            n(A) =3
            n(B) = 3
            n(AUB) = 5
            Cardinality of the three sets
            LetA and B and Crepresent threesets asa shown in the figure s
            n(AUBUC) =n(A) + n(B) + n(C) - n(A∩ B) -- n(B∩ C) - n(C∩ A) +n(A∩ B∩ C)
            Operation of sets
            Union of sets
            The set which includes elements of A and B is called union of the sets.
            A = {1, 2, 5,}
            B = {5, 3, 4}
            AUB = {1, 2, 3, 4, 5}
            Or, AUB= {x: xϵ A orxϵ B}
            n(A) =3
            n(B) = 3
            n(AUB) = n(A) + n(B) - n(A∩ B)
            = 3 +3 -1 = 5
            Intersections of sets
            If the elements of set belongs to both Sets A and B, it is called intersection of A and B.
            A = {1, 2, 5}
            B = {5, 3, 4}
            A∩ B = {5}
            n(A∩ B) = n(A) – n0 (A) = 3 -2 = 1
            Or, A∩ B = {x: xϵ A and xϵ B}
            Complement of sets
            The set that contains all the elements of universal sets except the given set A is called complement of the set A . It is denoted by A̅
            Difference of sets
            If A and B are the two sets , the difference of the dsets is the elements of the set thst includes only in one set .
            A – B= A -(A∩ B )
            B- A= B-(A∩ B )
            Example
            Examples1
            In a group of 200 students who like game, 120 like cricket game an 105 like football game. By drawing Venn diagram find
            i. how many students like both the games ?
            ii. How many students like only cricket?
            Soln
            n(U) = 200
            C and F denote the students who study Cricket and football respectively.
            n(C) =120
            n(F) = 105
            n( C ∩ F)=?
            We have
            n(CUF)=n(C) + n(F) -n(C∩ F)
            200=120 + 105 -n(C∩ F)
            n(C∩ F)= 25
            n0(C) = n(C)-n( C ∩ F)= 120 – 25 = 95
            Examples 2
            In the certain examination, 50% students passed in account, 30% passed in English, 30% failed in both and 25 student passes in both subjects. By drawing Venn – diagram, find the number of the students who passes in account only.
            Let total number be x A and E denotes the students who study account and English respectively
            n(A) =50%
            n(E) = 30%
            n( A U E)c = 30%
            n( A U E) = 25
            We have
            n(U)= n(A)+ n(E)+n(AUE)¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ - n( A ∩E)
            100%= 50 % + 30% + 30 % - n( A ∩E)
            n( A ∩E) = 10%
            According to the question,
            10% of x = 25
            x= 250
            The number of the students who passed in accounts only = 40% of the 250 = 100
            Examples 3
            In a survey it was found that 8.%people like oranges ,85% like mangoes and 75% like both But 45 people like none of themDrawing Venn –diagram , find the number of the people whowere in the survey.
            Soln:
            Let O and M be the number of people who like oranges and mangoes respectively.
            n (U) =n(OUM) + n(OUM)¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
            100%=n (O) + n (M) - n(O∩M) + n(OUM)¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
            100% =80% + 85% - 75% + n(OUM)¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
            n(OUM)¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯= 10%
            According to the question,
            10%of total number(say x)= 45
            Or, x=450010 = 450</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
           
          </div>
        </div>
      </div>
    </div>
    <!-- Page content -->
  </div>
</template>
<script>
</script>
<script>
import axios from "axios";
import VueApexCharts from "vue-apexcharts";
import host from "../../host.js";
export default {
  components: {
    apexchart: VueApexCharts
  },
  created() {
    if (this.$route.query.monitormode == "true") {
      this.stats = "present";
      var video = document.querySelector("#videoElement");

      if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices
          .getUserMedia({ video: true })
          .then(function(stream) {
            video.srcObject = stream;
          })
          .catch(function(err0r) {
            console.log("Something went wrong!");
          });
      }
    }
  },
  methods: {
    YES() {
      this.stats = "present";
      var video = document.querySelector("#videoElement");

      if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices
          .getUserMedia({ video: true })
          .then(function(stream) {
            video.srcObject = stream;
          })
          .catch(function(err0r) {
            console.log("Something went wrong!");
          });
      }
    },
    DISYES() {
      this.stats = "false";
    }
  },
  data() {
    return {
      stats: "false",
      options: {
        chart: {
          id: "vuechart-example"
        },
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998]
        }
      },
      series: [
        {
          name: "series-1",
          data: [30, 40, 45, 50, 49, 60, 70, 91]
        }
      ]
    };
  }
};
</script>
<style scoped>
.mainDash {
  margin-top: 5vh;
}
.bibek {
  border-bottom: 1px solid white;

  margin-bottom: 10px;
  padding-top: 10px;
  box-sizing: border-box;
}
.logout-button {
  cursor: pointer;
}
.buttonCustom {
  margin-top: -20px;
}
.text1 {
  font-size: 12px;
}
.buttonchat {
  position: absolute;
  top: 67vh;
  left: 82.6vw;
}
.mainView {
  margin-top: -24vh;
}
.premium {
  border: 1px solid #cacfc9;
  color: #67ee46;
  padding-left: 10px;
  box-sizing: border-box;
}
.main {
  display: flex;
}
.div1 {
  width: 20%;
}
.row {
  width: 80vw;
}
.mainView {
  height: 67vh;
}
.margin {
  margin-left: 7vw;
}
.button {
  margin-left: 60vw;
  margin-top: 9vh;
}
.readmore {
  position: absolute;
  top: 80vh;
  left: 23.2vw;
  border: 1px solid black;
}
</style>