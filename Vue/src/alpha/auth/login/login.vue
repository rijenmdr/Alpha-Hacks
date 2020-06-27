<template>
  <div>
    <Header />
    <router-view></router-view>
    <!-- Footer -->
  </div>
</template>
<script>
import Header from "../headerAuth";
import LoginMain from "./loginMain";

export default {
  components: {
    Header,
    LoginMain
  },

  data() {
    return {
      username: null,
      password: null,
      error: "",
      remember: ""
    };
  },

  methods: {
    async login() {
      await this.$store.dispatch("Login", {
        username: this.username,
        password: this.password,
        remember: this.remember
      });

      const error = this.$store.getters.getError;
      console.log(this.$store.getters.getUser);
      if (error) {
        this.error = "Username and Password didn't match";
      } else {
        this.$router.push("/dashboard");
      }
    }
  },
  created() {
    const token = localStorage.getItem("token");
    if (!token) {
      return;
    }
    const expirationDate = localStorage.getItem("expiresIn");
    const now = new Date();
    if (now >= expirationDate) {
      return;
    }
    this.$router.push("/dashboard");
  }
};
</script>
