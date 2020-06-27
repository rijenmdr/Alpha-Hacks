<template>
  <div class="main-content" id="panel">
    <!-- Header -->
    <!-- Header -->
    <video autoplay="true" id="videoElement"></video>
    <div class="container mainView">
      <div class="container-fluid">
        <div class="container">
          <div v-if="stats!='present'" class="row mt-5"></div>
          <div v-if="stats!='present'" class="row mt-2"></div>
          <div class="row mt-5">
            <div class="col-md-6">
              <div class="pr-md-5">
                <h3>Key Learnings</h3>
                <p>
                  An online business strategy can boost your chances of digital success, helping you to define clear goals and focus your online activity. In this lesson, we'll explore:
                  how an online business can benefit from a business strategy
                  best practices when creating a business strategy
                  examples of common goals and popular strategies to achieve them.
                </p>
                <ul class="list-unstyled mt-5">
                  <li class="py-2">
                    <div class="d-flex align-items-center">
                      <badge type="success" circle class="mr-3" icon="fa fa-arrow-right"></badge>
                      <h6 class="mb-0">how an online business can benefit from a business strategy</h6>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="d-flex align-items-center">
                      <badge type="success" circle class="mr-3" icon="fa fa-arrow-right"></badge>
                      <h6 class="mb-0">best practices when creating a business strategy</h6>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="d-flex align-items-center">
                      <badge type="success" circle class="mr-3" icon="fa fa-arrow-right"></badge>
                      <h6
                        class="mb-0"
                      >examples of common goals and popular strategies to achieve them.</h6>
                    </div>
                  </li>
                </ul>
              </div>
            </div>

            <div class="col-lg-6 mt-5">
              <iframe width="420" height="345" src="https://www.youtube.com/embed/tgbNymZ7vqY"></iframe>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="stats=='present'" class="header bg-primary pb-0">
      <div class="row">
        <div class="col-xl-3 col-md-6 mt-3 margin">
          <div class="card card-stats">
            <!-- Card body -->
            <div class="card-body">
              <div class="row">
                <div class="col">
                  <h5 class="card-title text-uppercase text-muted mb-0">Total Web Visits</h5>
                  <span class="h2 font-weight-bold mb-0">900</span>
                </div>
                <div class="col-auto"></div>
              </div>
              <p class="mt-3 mb-0 text-sm">
                <span class="text-success mr-2">3.48%</span>
                <span class="text-nowrap">Since last month</span>
              </p>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-md-6 mt-3 ml-5">
          <div class="card card-stats">
            <!-- Card body -->
            <div class="card-body">
              <div class="row">
                <div class="col">
                  <h6 class="card-title text-uppercase text-muted mb-0">Contentration Level</h6>
                  <span class="h2 font-weight-bold mb-0">20%</span>
                </div>
                <div class="col-auto"></div>
              </div>
              <p class="mt-3 mb-0 text-sm">
                <span class="text-success mr-2">3.48%</span>
                <span class="text-nowrap">Since last month</span>
              </p>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-md-6 ml-5">
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
    <div v-else class="buttondisable">
      <base-button
        tag="button"
        type="primary"
        class="mt-4"
        data-toggle="modal"
        data-target="#disablemonitormode"
      >Disable Monitor Mode</base-button>
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
    <!-- Page content -->
  </div>
</template>
<script>
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
    }
  },
  methods: {
    YES() {
      this.stats = "present";
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
.buttondisable {
  position: absolute;
  top: 62vh;
  left: 78.7vw;
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