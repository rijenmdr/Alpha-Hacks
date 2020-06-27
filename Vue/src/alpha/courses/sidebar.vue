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

            <span class="nav-link-text">Popular Courses</span>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/dashboard/schoollevel" class="nav-link">
            <i class="fa fa-square" aria-hidden="true"></i>

            <span class="nav-link-text">School Level</span>
          </router-link>
        </li>

        <li v-if="number<=1 || paidUser" class="nav-item">
          <router-link to="/dashboard/plustwolevel" class="nav-link">
            <i class="fa fa-square" aria-hidden="true"></i>

            <span class="nav-link-text">+2 Level</span>
          </router-link>
        </li>
        <li v-else class="nav-item">
          <router-link v-if="!paidUser" to="/upgradetopro" class="nav-link">
            <i class="fas fa-edit text-success"></i>
            <span class="nav-link-text">Upgrate to Create</span>
          </router-link>
        </li>

        <li class="nav-item">
          <router-link to="/dashboard/bachelorlevel" class="nav-link">
            <i class="fa fa-square" aria-hidden="true"></i>

            <span class="nav-link-text">Bachelor</span>
          </router-link>
        </li>

        <li class="nav-item">
          <router-link to="/dashboard/feedback" class="nav-link">
            <i class="fa fa-square" aria-hidden="true"></i>

            <span class="nav-link-text">Career Development</span>
          </router-link>
        </li>
        <li class="nav-item">
          <div class="nav-link" data-toggle="modal" data-target="#profile">
            <i class="ni ni-single-02 text-yellow"></i>
            <span class="nav-link-text">Public Speaking</span>
          </div>
        </li>
        <li v-if="!paidUser" class="nav-item">
          <router-link class="nav-link" to="/upgradetopro">
            <i class="ni ni-send text-dark"></i>
            <span class="nav-link-text">Upgrade</span>
          </router-link>
        </li>
        <li v-if="paidUser" class="nav-item" data-toggle="modal" data-target="#modalProUser">
          <router-link to="/dashboard/protemplates" class="nav-link">
            <i class="fa fa-pencil-square text-primary" aria-hidden="true"></i>
            <span class="nav-link-text">Pro Template</span>
          </router-link>
        </li>

        <li v-if="paidUser" class="nav-item">
          <div class="nav-link" data-toggle="modal" data-target="#customTemplates">
            <i class="fas fa-edit"></i>
            <span class="nav-link-text">Custom Templates</span>
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
