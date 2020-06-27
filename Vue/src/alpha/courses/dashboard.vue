<template>
  <div class="main">
    <!-- Modal -->
    <div
      class="modal fade"
      id="monitormode"
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
            <button data-dismiss="modal" type="button" @click="NO" class="btn btn-secondary">NO</button>
            <button data-dismiss="modal" type="button" @click="YES" class="btn btn-primary">YES</button>
          </div>
        </div>
      </div>
    </div>
    <div class="div1">
      <Sidebar :number="number" />
    </div>
    <div class="div2">
      <MainDash />
    </div>
    <div></div>
  </div>
</template>
<script>
import axios from "axios";
import host from "../../host.js";
import MainDash from "./mainDash";
import Sidebar from "./sidebar";
export default {
  data() {
    return {
      number: ""
    };
  },
  components: {
    MainDash,
    Sidebar
  },
  methods: {
    YES() {
      this.$router.push("/learnZone?monitormode=true");
    },

    NO() {
      this.$router.push("/learnZone?monitormode=false");
    }
  },
  async created() {
    let token = this.$store.getters.getToken;
    if (!token) {
      token = localStorage.getItem("token");
    }
    let user = this.$store.getters.getUser;
    if (!user) {
      user = localStorage.getItem("user");
    }
    let data = {
      token: token,
      user: user
    };
    await this.$store.dispatch("setUserSite", data);
    await axios
      .post(
        host.host + "/api/dashboard",
        {
          user: user
        },
        {
          headers: {
            Authorization: `Token ${token}`
          }
        }
      )
      .then(res => {
        this.number = res.data.data.length || 0;
        console.log(this.number);
        axios
          .post(
            host.host + "/api/search_paid_user",
            {
              username: user
            },
            {
              headers: {
                Authorization: `Token ${token}`
              }
            }
          )
          .then(res => {
            if (res.data.paidUser.length > 0) {
              if (this.$store.getters.getAlert) {
                this.$store.dispatch("setPaidUser", res.data.paidUser);
              }
            }
          })
          .catch(err => {
            console.log("error");
            console.log(err);
          });
      });
  }
};
</script>
<style scoped>
<style scoped > .mainDash {
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
</style>

