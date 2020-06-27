<template>
  <div class="main-content" id="panel">
    <!-- Header -->
    <!-- Header -->
    <div class="header bg-primary pb-5">
      <div class="container-fluid">
        <div class="header-body">
          <div class="row align-items-center bibek">
            <div class="col-lg-7 col-7"></div>
            <div class="col-lg-5 col-7 mt-3">
              <!-- <h6 class="h5 text-white d-inline-block ml-5">Welcome {{user}}</h6> -->
              <nav class="d-none d-md-inline-block ml-md-5 float-right">
                <button
                  type="button"
                  class="btn btn-white btn-sm buttonCustom"
                  data-toggle="modal"
                  data-target="#exampleModalCenter"
                >
                  <i class="fa fa-sign-out" aria-hidden="true"></i>Logout
                </button>
              </nav>
              <nav class="d-none d-md-inline-block ml-md-5 float-right">
                <div class="btn text-white btn-sm buttonCustom">
                  <i class="fa fa-user" aria-hidden="true"></i>
                  Welcome {{user}}
                </div>
              </nav>
            </div>
          </div>
          <!-- Modal -->
          <div
            class="modal fade"
            id="exampleModalCenter"
            tabindex="-1"
            role="dialog"
            aria-labelledby="exampleModalCenterTitle"
            aria-hidden="true"
          >
            <div class="modal-dialog modal-dialog-centered" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLongTitle">Alert</h5>
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div class="modal-body">You will be logged out of this session !!!</div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                  <button
                    @click="logout"
                    type="button"
                    data-dismiss="modal"
                    class="btn btn-primary"
                  >Continue</button>
                </div>
              </div>
            </div>
          </div>
          <!-- Card stats -->
          <div class="row">
            <div class="col-xl-12 col-md-12 row">
              <h2 class="text-white ml-2">Online courses</h2>
              <p
                class="text-white ml-2"
              >Discover a range of free learning content designed to help your business or in your career. You can learn by selecting individual modules, or dive right in and take an entire course end-to-end.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <router-view></router-view>
      </div>
    </div>
    <!-- Page content -->
  </div>
</template>
<script>
import axios from "axios";
import Recent from "./Recent";
import host from "../../host.js";
import Sidebar from "./sidebar";

export default {
  components: {
    Sidebar,
    Recent
  },
  data() {
    return {
      number: "",
      user: this.$store.getters.getUser || localStorage.getItem("user")
    };
  },
  async created() {
    await axios
      .post(
        host.host + "/api/dashboard",
        {
          user: user
        },
        {
          headers: {
            Authorization: `Token ${JWTToken}`
          }
        }
      )
      .then(res => {
        this.sites = res.data.data;
        this.number = res.data.data.length;
        axios
          .post(
            host.host + "/api/get_hotels",
            {
              user: user
            },
            {
              headers: {
                Authorization: `Token ${JWTToken}`
              }
            }
          )
          .then(res => {
            this.hotels = res.data.data;
            this.hotelId = res.data.data[0].id;
          });
      })
      .catch(err => {
        console.log(err);
      });
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
      this.$router.push("/");
    }
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
</style>