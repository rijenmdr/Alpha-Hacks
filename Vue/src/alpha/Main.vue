<template>
  <div class="position-relative">
    <!-- shape Hero -->
    <img class="png" src="../assets/land.svg" alt />
    <section class="section-shaped my-0">
      <div class="shape shape-style-1 shape-default shape-skew">
        <span></span>
        <span></span>
        <span></span>
      </div>
      <div class="container shape-container d-flex">
        <div class="col px-0">
          <div class="row">
            <div class="col-lg-7">
              <h1 class="display-3 text-white">
                Learn new skills online
                <span>prepare today for better tomorrow</span>
              </h1>
              <p
                class="lead text-white"
              >This platform helps you to learn at your own pace, with flexible and personalized training courses designed to build your confidence and help you flourish.</p>
              <div class="btn-wrapper">
                <router-link to="/learnmore" class="mr-2">
                  <base-button class="mb-3 mb-sm-0" type="info">LEARN MORE</base-button>
                </router-link>
                <router-link to="/login">
                  <base-button class="mb-3 mb-sm-0" type="white">GET STARTED</base-button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- 1st Hero Variation -->
  </div>
</template>
<style scoped>
.image {
  width: 100%;
}
.png {
  position: absolute;
  width: 500px;
  top: 25vh;
  left: 55vw;
}
</style>