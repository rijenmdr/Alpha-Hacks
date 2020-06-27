<template>
  <nav
    id="navbar-main"
    class="navbar navbar-main navbar-expand-lg navbar-transparent navbar-light headroom"
  >
    <div class="container">
      <router-link class="navbar-brand mr-lg-5 logo" to="/">
        Alpha
        <span class="text1">Read</span>
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbar_global"
        aria-controls="navbar_global"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="navbar-collapse collapse" id="navbar_global">
        <div class="navbar-collapse-header">
          <div class="row">
            <div class="col-6 collapse-brand">
              <a href="./index.html"></a>
            </div>
            <div class="col-6 collapse-close">
              <button
                type="button"
                class="navbar-toggler"
                data-toggle="collapse"
                data-target="#navbar_global"
                aria-controls="navbar_global"
                aria-expanded="false"
                aria-label="Toggle navigation"
              >
                <span></span>
                <span></span>
              </button>
            </div>
          </div>
        </div>
        <ul class="navbar-nav navbar-nav-hover align-items-lg-left">
          <li class="nav-item">
            <a href="#" class="nav-link">
              <i class="ni ni-ui-04 d-lg-none"></i>
              <span class="nav-link-inner--text">Online Courses</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link">
              <i class="ni ni-ui-04 d-lg-none"></i>
              <span class="nav-link-inner--text ml-1">Certification</span>
            </a>
          </li>
        </ul>
        <ul class="navbar-nav align-items-lg-center ml-lg-auto">
         
        </ul>
      </div>
    </div>
  </nav>
</template>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Cabin:wght@700&display=swap");
.logo {
  font-size: 22px;
  font-family: "Cabin", sans-serif;
}
.text1 {
  color: #fda204;
}
</style>
