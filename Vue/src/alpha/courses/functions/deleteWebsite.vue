<template>
  <div class="main-content" id="panel">
    <div class="header bg-primary pb-5 headTop"></div>
    <div class="deleteWebsite">
      <div class="container">
        <div class="row">
          <div class="col-md-6" v-for="(site,i) in userSite" v-bind:key="i">
            <div class="col-xl-12 col-md-6">
              <div class="card card-stats">
                <!-- Card body -->
                <div class="card-body">
                  <div class="row">
                    <div class="col">
                      <h5 class="card-title text-uppercase text-muted mb-0">{{site.nameOfSiteH}}</h5>
                      <span class="h2 font-weight-bold mb-0">{{site.id}}</span>
                    </div>
                    <div @click="deleteSite(site.id)" class="col-auto">
                      <div
                        class="icon icon-shape bg-gradient-orange text-white rounded-circle shadow"
                      >
                        <i class="fas fa-trash"></i>
                      </div>
                    </div>
                  </div>
                  <p class="mt-3 mb-0 text-sm">
                    <span class="text-success mr-2">
                      <i class="fa fa-arrow-up"></i> Created:
                    </span>
                    <span class="text-nowrap">{{site.created_date}}</span>
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import host from '../../../host.js'
import axios from "axios";
export default {
  data() {
    return {
      userSite: this.$store.getters.getUserSite
    };
  },
  methods: {
    async deleteSite(val) {
      let JWTToken = localStorage.getItem("token");
      if (!JWTToken) {
        JWTToken = this.$store.getters.getToken;
      }
      await axios
        .delete(host.host+"/api/delete_website/" + val, {
          headers: {
            Authorization: `Token ${JWTToken}`
          }
        })
        .then(res => {
          this.$store.dispatch("addNotifications", {
            type: "danger",
            message: "Your site is deleted"
          });
          this.$store.dispatch("setUserSite", {
            token: this.$store.getters.getToken,
            user: this.$store.getters.getUser
          });
          
          this.$router.push("/deleteSuccess");
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>
<style scoped>
.deleteWebsite {
  margin-top: 10vh;
  margin-bottom: 10vh;
}
.headTop{
  width: 130%;
}
.main-content{
  width: 80vw;
}
</style>