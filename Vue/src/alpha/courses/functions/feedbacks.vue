<template>
  <div class="main-content" id="panel">
    <div class="header bg-primary pb-5 headerTop"></div>
    <div class="deleteWebsite">
      <div class="container">
        <div class="row mt-5">
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
                    <div class="col-auto">
                      <div
                        class="icon icon-shape bg-gradient-orange text-white rounded-circle shadow"
                      >
                        <i class="fas fa-envelope"></i>
                      </div>
                    </div>
                  </div>
                  <p class="mt-3 mb-0 text-sm">
                    <span class="text-success mr-2">
                      <i class="fa fa-user"></i> Owner:
                    </span>
                    <span class="text-nowrap">{{site.user}}</span>
                  </p>
                  <p class="mt-3 mb-0 text-sm">
                    <span class="text-success mr-2">
                      <i class="fa fa-arrow-up"></i> Created:
                    </span>
                    <span class="text-nowrap">{{site.created_date}}</span>
                  </p>
                  <div @click="feedback(site.id)" class="btn btn-neutral btn-icon mt-2 btn">
                    <span class="btn-inner--icon">
                      <i class="fas fa-hand-point-right"></i>
                    </span>
                    <span class="nav-link-inner--text text-success"> See Feedback</span>
                  </div>
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
import axios from "axios";
export default {
  data() {
    return {
      userSite: this.$store.getters.getUserSite
    };
  },
  created() {
    // console.log(this.$store.getters.getUserSite.length)
    // let length=this.$store.getters.getUserSite.length
    // axios.get("http://localhost:8000/api/get_review/" + shopid)
    // .then(res => {
    //     console.log(res)
    //     this.feeds = res.data.feedback;
    // });
  },
  methods: {
    feedback(val) {
      this.$router.push("/dashboard/feedback/" + val);
    }
  }
};
</script>
<style scoped>
.feedback {
  margin-top: 10vh;
  margin-bottom: 10vh;
}
.btn {
  border: 1px solid green;
}
.headerTop{
  width: 140%;
}
.main-content{
  width: 80vw;
}
</style>