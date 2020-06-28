<template>
  <div class="main-content" id="panel">
    <!-- Header -->
    <!-- Header -->
    <div></div>
    <div class="container mb-5">
      <div class="container-fluid">
        <div class="container">
          <div v-if="stats!='present'" class="row mt-5"></div>
          <div v-if="stats!='present'" class="row mt-2"></div>
          <div class="row mt-5">
            <div class="col-md-6">
              <div class="pr-md-5">
                <h3>Key Learnings</h3>
                <p>In algebra, a quadratic equation is any equation that can be rearranged in standard form as where x represents an unknown, and a, b, and c represent known numbers, where a ≠ 0. If a = 0, then the equation is linear, not quadratic, as there is no term.</p>
                <ul class="list-unstyled mt-5">
                  <li class="py-2">
                    <div class="d-flex align-items-center">
                      <h6
                        class="mb-0"
                      >The name Quadratic comes from "quad" meaning square, because the variable gets squared (like x2).</h6>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="d-flex align-items-center">
                      <h6
                        class="mb-0"
                      >It is also called an "Equation of Degree 2" (because of the "2" on the x)</h6>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="d-flex align-items-center">
                      <h6 class="mb-0">
                        The Standard Form of a Quadratic Equation looks like this:
                        Quadratic Equation: ax^2 + bx + c = 0
                      </h6>
                    </div>
                  </li>
                </ul>
              </div>
            </div>

            <div class="col-lg-6 mt-5">
              <iframe width="420" height="345" src="https://www.youtube.com/embed/1JsH0Up_5Hc"></iframe>
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
  margin-top: 10vh;
}
</style>