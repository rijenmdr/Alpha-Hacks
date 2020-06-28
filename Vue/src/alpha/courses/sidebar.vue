<template>
  <div class="main">
    <div class="div1">
      <div class="logo ml-5 mt-4">
        <router-link class="navbar-brand mr-lg-5 logo" to="/">
          Alpha
          <span class="text1">Online</span>
        </router-link>
      </div>
    </div>
    <div class="div2 ml-5">
      <ul class="navbar-nav">
        <li class="nav-item mb-4">
          <span class="nav-link-text">Categories</span>
        </li>
        <li class="nav-item">
          <router-link to="/dashboard" class="nav-link">
            <i class="fa fa-square" aria-hidden="true"></i>

            <span class="nav-link-text">Recents</span>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/dashboard/bachelorlevel" class="nav-link">
            <i class="fa fa-square" aria-hidden="true"></i>

            <span class="nav-link-text">Bachelor</span>
          </router-link>
        </li>
        <li v-if="number<=1 || paidUser" class="nav-item">
          <router-link to="/dashboard/plustwolevel" class="nav-link">
            <i class="fa fa-square" aria-hidden="true"></i>

            <span class="nav-link-text">+2 Level</span>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/dashboard/schoollevel" class="nav-link">
            <i class="fa fa-square" aria-hidden="true"></i>

            <span class="nav-link-text">Class 10</span>
          </router-link>
        </li>

        <li class="nav-item">
          <router-link to="/dashboard/feedback" class="nav-link">
            <i class="fa fa-square" aria-hidden="true"></i>

            <span class="nav-link-text">Class 9</span>
          </router-link>
        </li>
        <li class="nav-item">
          <div class="nav-link" data-toggle="modal" data-target="#profile">
            <i class="fa fa-square" aria-hidden="true"></i>
            <span class="nav-link-text">Class 8</span>
          </div>
        </li>
      </ul>
    </div>
    <div
      class="modal fade"
      id="profile"
      tabindex="-1"
      role="dialog"
      aria-labelledby="exampleModalCenterTitle"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">Modal title</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">This feature is under construction</div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" data-dismiss="modal">Ok</button>
          </div>
        </div>
      </div>
    </div>
    <div
      class="modal fade"
      id="customTemplates"
      tabindex="-1"
      role="dialog"
      aria-labelledby="exampleModalCenterTitle"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">Modal title</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">This custom templates will be available soon !!!</div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Ok</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      paidUser: ""
    };
  },
  props: ["number"],
  methods: {
    logout() {
      this.$store.dispatch("logout");
      this.$router.push("/");
    }
  },
  created() {
    setTimeout(() => {
      console.log(this.$store.getters.getPaidUser);
      this.paidUser = this.$store.getters.getPaidUser;
    }, 2000);
  }
};
</script>
<style  scoped>
a:hover {
  text-decoration: none;
}
@import url("https://fonts.googleapis.com/css2?family=Cabin:wght@700&display=swap");
.logo {
  font-size: 22px;
  font-family: "Cabin", sans-serif;
}
.text1 {
  color: #d3b001;
}
.main {
  flex-direction: column;
  height: 100vh;
  border-right: 5px solid #e9ede8;
}
.div1 {
  height: 15vh;
}
.logo {
  text-align: center;
}
</style>
