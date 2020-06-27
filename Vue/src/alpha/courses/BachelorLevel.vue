<template>
  <section class="section section-lg pt-lg-0 mt--200">
    <div class="container courses">
      <div class="row justify-content-center">
        <div class="col-lg-12">
          <div class="row row-grid coursesList">
            <div class="col-lg-4">
              <card class="border-0" hover shadow body-classes="py-5">
                <icon name="ni ni-check-bold" type="primary" rounded class="mb-4"></icon>
                <h6 class="text-primary text-uppercase">C programming</h6>
                <p class="description mt-3">Created By : Alpha Team</p>
                <div class="mt-3">
                  <badge type="primary" class="mr-3" rounded>Module : 20</badge>
                  <badge type="primary" rounded>Hours : 10</badge>
                </div>
                <base-button tag="a" href="#" type="primary" class="mt-4">Join Now</base-button>
              </card>
            </div>
            <div class="col-lg-4">
              <card class="border-0" hover shadow body-classes="py-5">
                <icon name="ni ni-check-bold" type="success" rounded class="mb-4"></icon>
                <h6 class="text-primary text-uppercase">Data Structure</h6>
                <p class="description mt-3">Created By : Alpha Team</p>
                <div class="mt-3">
                  <badge type="primary" class="mr-3" rounded>Module : 20</badge>
                  <badge type="primary" rounded>Hours : 10</badge>
                </div>
                <base-button tag="a" href="#" type="primary" class="mt-4">Join Now</base-button>
              </card>
            </div>
            <div class="col-lg-4">
              <card class="border-0" hover shadow body-classes="py-5">
                <icon name="ni ni-check-bold" type="primary" rounded class="mb-4"></icon>
                <h6 class="text-primary text-uppercase">Statistics</h6>
                <p class="description mt-3">Created By : Alpha Team</p>
                <div class="mt-3">
                  <badge type="primary" class="mr-3" rounded>Module : 20</badge>
                  <badge type="primary" rounded>Hours : 10</badge>
                </div>
                <base-button tag="a" href="#" type="primary" class="mt-4">Join Now</base-button>
              </card>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<style scoped>
.courses {
  margin-top: 33vh;
}
.description {
  display: inline;
}
.coursesList {
  justify-content: space-between;
  width: 75vw;
}
</style>