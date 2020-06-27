<template>
  <div class="main-content">
    <div class="header pb-6">
      <section id="login">
        <div class="container mt-3 mb-3">
          <div class="row">
            <div class="col-md-3 mx-auto">
              <div class="card">
                <div class="card-header">
                  <h4>Home Page</h4>
                </div>
                <div class="card-body">
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control"
                      v-model="nameOfSiteH"
                      placeholder="Name of Website"
                    />
                  </div>
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control"
                      v-model="category"
                      placeholder="Category"
                    />
                  </div>
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control"
                      v-model="headingOneH"
                      placeholder="heading one"
                    />
                  </div>
                  <div class="form-group">
                    <textarea
                      rows="3"
                      class="form-control"
                      v-model="descriptionOneH"
                      placeholder="description one"
                    />
                  </div>
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control"
                      v-model="headingTwoH"
                      placeholder="heading two"
                    />
                  </div>
                  <div class="form-group">
                    <textarea
                      rows="3"
                      class="form-control"
                      v-model="descriptionTwoH"
                      placeholder="description two"
                    />
                  </div>
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control"
                      v-model="headingThreeH"
                      placeholder="heading three"
                    />
                  </div>
                  <div class="form-group">
                    <textarea
                      rows="3"
                      class="form-control"
                      v-model="descriptionThreeH"
                      placeholder="description three"
                    />
                  </div>
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control"
                      v-model="featureOneH"
                      placeholder="feature one"
                    />
                  </div>
                  <div class="form-group">
                    <textarea
                      rows="3"
                      class="form-control"
                      v-model="featureOneDesH"
                      placeholder="feature description"
                    />
                  </div>
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control"
                      v-model="featureTwoH"
                      placeholder="feature two"
                    />
                  </div>
                  <div class="form-group">
                    <textarea
                      rows="3"
                      class="form-control"
                      v-model="featureTwoDesH"
                      placeholder="feature description"
                    />
                  </div>
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control"
                      v-model="featureThreeH"
                      placeholder="Feature three"
                    />
                  </div>
                  <div class="form-group">
                    <textarea
                      rows="3"
                      class="form-control"
                      v-model="featureThreeDesH"
                      placeholder="feature description"
                    />
                  </div>
                </div>
              </div>
            </div>

            <div class="col-md-3 mx-auto">
              <div class="card">
                <div class="card-header">
                  <h4>About Page</h4>
                </div>
                <div class="card-body">
                  <div class="form-group">
                    <textarea
                      rows="3"
                      class="form-control"
                      v-model="introductionA"
                      placeholder="Introduction"
                    />
                  </div>
                  <div class="form-group">
                    <textarea
                      rows="10"
                      class="form-control"
                      v-model="whatWeDoA"
                      placeholder="What we do"
                    />
                  </div>
                </div>
                <div class="card-header">
                  <h4>Background Color</h4>
                </div>
                <div class="card-body">
                  <div class="form-group">
                    <select v-model="backgroundColor" class="form-control form-control">
                      <option value="green">Green</option>
                      <option value="#30332E">Black</option>
                      <option value="#DECA04">Yellow</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-3 mx-auto">
              <div class="card">
                <div class="card-header">
                  <h4>Service Page</h4>
                </div>
                <div class="card-body">
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control"
                      v-model="serviceOne"
                      placeholder="Service One"
                    />
                  </div>

                  <div class="form-group">
                    <textarea
                      rows="3"
                      class="form-control"
                      v-model="serviceOneDes"
                      placeholder="description of service one"
                    />
                  </div>
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control"
                      v-model="serviceTwo"
                      placeholder="service two"
                    />
                  </div>
                  <div class="form-group">
                    <textarea
                      rows="3"
                      class="form-control"
                      v-model="serviceTwoDes"
                      placeholder="description two"
                    />
                  </div>
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control"
                      v-model="serviceThree"
                      placeholder="service three"
                    />
                  </div>
                  <div class="form-group">
                    <textarea
                      rows="3"
                      class="form-control"
                      v-model="serviceThreeDes"
                      placeholder="description of service three"
                    />
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-3 mx-auto">
              <div class="card">
                <div class="card-header">
                  <h4>Contact Page</h4>
                </div>
                <div class="card-body">
                  <div class="form-group">
                    <input type="text" class="form-control" v-model="titleC" placeholder="title" />
                  </div>
                  <div class="form-group">
                    <textarea
                      rows="6"
                      class="form-control"
                      v-model="descriptionC"
                      placeholder="description"
                    />
                  </div>
                  <div class="form-group">
                    <input type="text" class="form-control" v-model="emailC" placeholder="email" />
                  </div>
                  <div class="form-group">
                    <input type="text" class="form-control" v-model="phoneC" placeholder="phone" />
                  </div>
                  <div class="form-group">
                    <input
                      type="text"
                      class="form-control"
                      v-model="addressC"
                      placeholder="address"
                    />
                  </div>

                  <div class="form-group">
                    <button
                      @click="update"
                      class="btn bg-success text-white btn-block border-white"
                    >Update</button>
                  </div>
                  <div class="form-group">
                    <button
                      @click="cancel"
                      class="btn bg-danger text-white btn-block border-white"
                    >Cancel</button>
                  </div>
                </div>
              </div>
            </div>

            <div class="col-md-3 mx-auto">
              <!-- <div>
              <img src="../../../assets/userWebsite/Home.png" height="250vh" width="350vw" />
            </div>
            <div>
              <img src="../../../assets/userWebsite/about.png" height="250vh" width="350vw" />
            </div>
            <div>
              <img src="../../../assets/userWebsite/contact.png" height="250vh" width="350vw" />
              </div>-->
              <!-- <div class="card-header">
              <h4>Images</h4>
            </div>
            <div class="form-group">
              <input type="file" @change="onFileChanged" class="form-control" multiple="multiple"/>
            </div>
            <div class="form-group">
              <input type="file" @change="onFileChanged(2)" class="form-control" />
            </div>
            <div class="form-group">
              <input type="file" @change="onFileChanged(3)" class="form-control" />
            </div>
            <div class="form-group">
              <input type="file" @change="onFileChanged(4)" class="form-control" />
            </div>
            <div class="form-group">
              <input type="file" @change="onFileChanged(5)" class="form-control" />
              </div>-->
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import host from '../../../host.js'
export default {
  data() {
    return {
      nameOfSiteH: "",
      headingOneH: "",
      descriptionOneH: "",
      headingTwoH: "",
      descriptionTwoH: "",
      headingThreeH: "",
      descriptionThreeH: "",
      featureOneH: "",
      featureTwoH: "",
      featureThreeH: "",
      introductionA: "",
      whatWeDoA: "",
      titleC: "",
      emailC: "",
      descriptionC: "",
      phoneC: "",
      addressC: "",
      featureOneDesH: "",
      featureTwoDesH: "",
      featureThreeDesH: "",
      serviceOne: "",
      serviceTwo: "",
      serviceThree: "",
      serviceOneDes: "",
      serviceTwoDes: "",
      serviceThreeDes: "",
      backgroundColor: "",
      category: ""
    };
  },
  created() {
    let JWTToken = localStorage.getItem("token");
    if (!JWTToken) {
      JWTToken = this.$store.getters.getToken;
    }
    let id = this.$route.params.id;
    axios
      .get(host.host+"/api/get_website/" + id, {
        headers: {
          Authorization: `Token ${JWTToken}`
        }
      })
      .then(res => {
        this.nameOfSiteH = res.data.website.nameOfSiteH;
        this.headingOneH = res.data.website.headingOneH;
        this.descriptionOneH = res.data.website.descriptionOneH;
        this.headingTwoH = res.data.website.headingTwoH;
        this.descriptionTwoH = res.data.website.descriptionTwoH;
        this.headingThreeH = res.data.website.headingThreeH;
        this.descriptionThreeH = res.data.website.descriptionThreeH;
        this.featureOneH = res.data.website.featureOneH;
        this.featureTwoH = res.data.website.featureTwoH;
        this.featureThreeH = res.data.website.featureThreeH;
        this.introductionA = res.data.website.introductionA;
        this.whatWeDoA = res.data.website.whatWeDoA;
        this.titleC = res.data.website.titleC;
        this.emailC = res.data.website.emailC;
        this.descriptionC = res.data.website.descriptionC;
        this.phoneC = res.data.website.phoneC;
        this.addressC = res.data.website.addressC;
        this.featureOneDesH = res.data.website.featureOneDesH;
        this.featureTwoDesH = res.data.website.featureTwoDesH;
        this.featureThreeDesH = res.data.website.featureThreeDesH;
        this.serviceOne = res.data.website.serviceOne;
        this.serviceTwo = res.data.website.serviceTwo;
        this.serviceThree = res.data.website.serviceThree;
        this.serviceOneDes = res.data.website.serviceOneDes;
        this.serviceTwoDes = res.data.website.serviceTwoDes;
        this.serviceThreeDes = res.data.website.serviceThreeDes;
        this.backgroundColor = res.data.website.backgroundColor;
        this.category = res.data.website.category;
      });
  },
  methods: {
    cancel() {
      this.$router.push("/dashboard");
    },
    async update() {
      let JWTToken = localStorage.getItem("token");
      if (!JWTToken) {
        JWTToken = this.$store.getters.getToken;
      }

      await axios
        .put(host.host+
          "/api/update_website/" + this.$route.params.id,

          {
            nameOfSiteH: this.nameOfSiteH,
            headingOneH: this.headingOneH,
            descriptionOneH: this.descriptionOneH,
            headingTwoH: this.headingTwoH,
            descriptionTwoH: this.descriptionTwoH,
            headingThreeH: this.headingThreeH,
            descriptionThreeH: this.descriptionThreeH,
            featureOneH: this.featureOneH,
            featureTwoH: this.featureTwoH,
            featureThreeH: this.featureThreeH,
            introductionA: this.introductionA,
            whatWeDoA: this.whatWeDoA,
            titleC: this.titleC,
            emailC: this.emailC,
            descriptionC: this.descriptionC,
            phoneC: this.phoneC,
            addressC: this.addressC,
            user: this.$store.getters.getUser,
            featureOneDesH: this.featureOneDesH,
            featureTwoDesH: this.featureTwoDesH,
            featureThreeDesH: this.featureThreeDesH,
            serviceOne: this.serviceOne,
            serviceTwo: this.serviceTwo,
            serviceThree: this.serviceThree,
            backgroundColor: this.backgroundColor,
            serviceOneDes: this.serviceOneDes,
            serviceTwoDes: this.serviceTwoDes,
            serviceThreeDes: this.serviceThreeDes
          },
          {
            headers: {
              Authorization: `Token ${JWTToken}`
            }
          }
        )
        .then(res => {
          this.$store.dispatch("addNotifications", {
            type: "success",
            message: "Update Successful"
          });
          this.$router.push("/dashboard");
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>