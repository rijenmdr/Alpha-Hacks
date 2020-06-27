<template>
  <div class="main">

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
import MainDash from "./Main";
import Sidebar from "./Sidebar";
export default {
  data() {
    return {
      number: "",
      stats: false
    };
  },

  components: {
    MainDash,
    Sidebar
  },
 
};
</script>

<style scoped >
.mainDash {
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

