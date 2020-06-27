<template>
  <div class="main-content" id="panel">
    <div class="header bg-primary pb-6"></div>
    <div class="row">
      <div class="col-xl-12">
        <div class="card">
          <div class="card-header border-0">
            <div class="row align-items-center">
              <div class="col">
                <h3 class="mb-0">Your Websites</h3>
              </div>
              <div class="col text-right">
                <a href="#!" class="btn btn-sm btn-primary">Delete all</a>
              </div>
            </div>
          </div>
          <div class="table-responsive">
            <!-- Projects table -->
            <table class="table align-items-center table-flush">
              <thead class="thead-light">
                <tr>
                  <th scope="col">Visitor Id</th>
                  <th scope="col">First Name</th>
                  <th scope="col">Last Name</th>
                  <th scope="col">Email</th>
                  <th scope="col">Message</th>
                  <th scope="col">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="feed in feeds">
                  <th>{{feed.id}}</th>
                  <th>{{feed.first_name}}</th>
                  <th>{{feed.last_name}}</th>
                  <th>{{feed.email}}</th>
                  <th>{{feed.message}}</th>
                  <th>
                    <div @click="deleteFeed(feed.id)" class="btn btn-danger">
                      <i class="fas fa-trash"></i>
                    </div>
                  </th>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import host from '../../../host.js'
export default {
  data() {
    return {
      feeds: ""
    };
  },
  created() {
    let shopid = this.$route.params.shopid;
    axios.get(host.host + "/api/get_review/" + shopid).then(res => {
      this.feeds = res.data.feedback;
    });
  },
  methods: {
    deleteFeed(id) {
      axios
        .delete(host.host+"/api/delete_feedback/" + id)
        .then(res => {
          let shopid = this.$route.params.shopid;
          axios
            .get(host.host+"/api/get_review/" + shopid)
            .then(res => {
              this.feeds = res.data.feedback;
            });
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>
<style scoped>
  .main-content{
    width:80vw;
  }
</style>