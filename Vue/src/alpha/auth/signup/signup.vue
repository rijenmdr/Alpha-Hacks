<template>
  <div>
    <Header />
    <section class="section section-shaped section-lg mt-0 mb-0">
      <div class="shape shape-style-1 bg-gradient-default">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
      </div>
      <div class="container">
        <div class="signup-content">
          <div class="signup-form">
            <h2 class="form-title">Sign up</h2>
            <p class="error">{{error}}</p>

            <form @submit.prevent="signUp" class="register-form" id="register-form">
              <div class="form-group" :class="{invalid:$v.username.$error}">
                <label for="name">
                  <i class="fas fa-user"></i>
                </label>
                <input
                  @blur="$v.username.$touch()"
                  type="text"
                  v-model="username"
                  name="name"
                  id="name"
                  placeholder="Your Name"
                />
              </div>
              <div class="form-group" :class="{invalid:$v.email.$error}">
                <label for="email">
                  <i class="fas fa-envelope"></i>
                </label>
                <input
                  @blur="$v.email.$touch()"
                  v-model="email"
                  type="email"
                  name="email"
                  id="email"
                  placeholder="Your Email"
                />
              </div>
              <div class="form-group" :class="{invalid:$v.password1.$error}">
                <label for="pass">
                  <i class="fas fa-key"></i>
                </label>
                <input
                  v-model="password1"
                  @blur="$v.password1.$touch()"
                  type="password"
                  name="pass"
                  id="pass"
                  placeholder="Password"
                />
              </div>
              <div class="form-group" :class="{invalid:$v.password2.$error}">
                <label for="re-pass">
                  <i class="fas fa-user-lock"></i>
                </label>
                <input
                  type="password"
                  name="re_pass"
                  @blur="$v.password2.$touch()"
                  v-model="password2"
                  id="re_pass"
                  placeholder="Repeat your password"
                />
              </div>
              <!-- <div class="form-group">
              <input type="checkbox" name="agree-term" id="agree-term" class="agree-term" />
              <label for="agree-term" class="label-agree-term">
                <span>
                  <span></span>
                </span>I agree all statements in
                <a href="#" class="term-service">Terms of service</a>
              </label>
              </div>-->
              <div class="form-group form-button">
                <button
                  :disabled="$v.$invalid"
                  type="submit"
                  class="btn btn-success btn-block mt-3"
                >Register</button>
              </div>
            </form>
          </div>
          <div class="signup-image">
            <figure>
              <img src="../../../assets/signup-image.jpg" alt="sing up image" />
            </figure>
            <router-link to="/login" class="signup-image-link">I am already member</router-link>
          </div>
        </div>
      </div>
    </section>
    <Footer />
  </div>
</template>
<script>
import Footer from "../../Footer";
import Header from "../headerAuth";
import {
  required,
  email,
  maxLength,
  minLength,
  sameAs
} from "vuelidate/lib/validators";

export default {
  components: {
    Footer,
    Header
  },
  data() {
    return {
      username: "",
      email: "",
      password1: "",
      password2: "",
      error: ""
    };
  },
  validations: {
    email: {
      required,
      email
    },
    username: {
      required,
      maxLength: maxLength(15)
    },
    password1: {
      required,
      minLength: minLength(6)
    },
    password2: {
      sameAs: sameAs("password1")
    }
  },
  methods: {
    async signUp() {
      await this.$store.dispatch("signUp", {
        username: this.username,
        password1: this.password1,
        password2: this.password2,
        email: this.email
      });
      const error = this.$store.getters.getError;
      if (error) {
        this.error = "please enter valid credentials";
      } else {
        this.$router.push("/dashboard");
      }
    }
  }
};
</script>
<style scoped>
.error {
  color: red;
  text-align: center;
}
.invalid label {
  color: red;
}
.invalid input {
  border: 1px solid red;
  background-color: #ffc9aa;
}
input,
select,
textarea {
  outline: none;
  appearance: unset !important;
  -moz-appearance: unset !important;
  -webkit-appearance: unset !important;
  -o-appearance: unset !important;
  -ms-appearance: unset !important;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  appearance: none !important;
  -moz-appearance: none !important;
  -webkit-appearance: none !important;
  -o-appearance: none !important;
  -ms-appearance: none !important;
  margin: 0;
}

input:focus,
select:focus,
textarea:focus {
  outline: none;
  box-shadow: none !important;
  -moz-box-shadow: none !important;
  -webkit-box-shadow: none !important;
  -o-box-shadow: none !important;
  -ms-box-shadow: none !important;
}

input[type="checkbox"] {
  appearance: checkbox !important;
  -moz-appearance: checkbox !important;
  -webkit-appearance: checkbox !important;
  -o-appearance: checkbox !important;
  -ms-appearance: checkbox !important;
}
input {
  width: 100%;
  display: block;
  border: none;
  border-bottom: 1px solid #999;
  padding: 6px 30px;
  font-family: Poppins;
  box-sizing: border-box;
}
input::-webkit-input-placeholder {
  color: #999;
}
input::-moz-placeholder {
  color: #999;
}
input:-ms-input-placeholder {
  color: #999;
}
input:-moz-placeholder {
  color: #999;
}
input:focus {
  border-bottom: 1px solid #222;
}
input:focus::-webkit-input-placeholder {
  color: #222;
}
input:focus::-moz-placeholder {
  color: #222;
}
input:focus:-ms-input-placeholder {
  color: #222;
}
input:focus:-moz-placeholder {
  color: #222;
}

input[type="checkbox"]:not(old) {
  width: 2em;
  margin: 0;
  padding: 0;
  font-size: 1em;
  display: none;
}

input[type="checkbox"]:not(old) + label {
  display: inline-block;
  line-height: 1.5em;
  margin-top: 6px;
}

input[type="checkbox"]:not(old) + label > span {
  display: inline-block;
  width: 13px;
  height: 13px;
  margin-right: 15px;
  margin-bottom: 3px;
  border: 1px solid #999;
  border-radius: 2px;
  -moz-border-radius: 2px;
  -webkit-border-radius: 2px;
  -o-border-radius: 2px;
  -ms-border-radius: 2px;
  background: white;
  background-image: -moz-linear-gradient(white, white);
  background-image: -ms-linear-gradient(white, white);
  background-image: -o-linear-gradient(white, white);
  background-image: -webkit-linear-gradient(white, white);
  background-image: linear-gradient(white, white);
  vertical-align: bottom;
}

input[type="checkbox"]:not(old):checked + label > span {
  background-image: -moz-linear-gradient(white, white);
  background-image: -ms-linear-gradient(white, white);
  background-image: -o-linear-gradient(white, white);
  background-image: -webkit-linear-gradient(white, white);
  background-image: linear-gradient(white, white);
}

input[type="checkbox"]:not(old):checked + label > span:before {
  content: "\f26b";
  display: block;
  color: #222;
  font-size: 11px;
  line-height: 1.2;
  text-align: center;
  font-family: "Material-Design-Iconic-Font";
  font-weight: bold;
}

.agree-term {
  display: inline-block;
  width: auto;
}

label {
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  -moz-transform: translateY(-50%);
  -webkit-transform: translateY(-50%);
  -o-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  color: #222;
}

.label-has-error {
  top: 22%;
}

label.error {
  position: relative;

  background-position-y: 3px;
  padding-left: 20px;
  display: block;
  margin-top: 20px;
}

label.valid {
  display: block;
  position: absolute;
  right: 0;
  left: auto;
  margin-top: -6px;
  width: 20px;
  height: 20px;
  background: transparent;
}
label.valid:after {
  font-family: "Material-Design-Iconic-Font";
  content: "\f269";
  width: 100%;
  height: 100%;
  position: absolute;
  /* right: 0; */
  font-size: 16px;
  color: green;
}

.label-agree-term {
  position: relative;
  top: 0%;
  transform: translateY(0);
  -moz-transform: translateY(0);
  -webkit-transform: translateY(0);
  -o-transform: translateY(0);
  -ms-transform: translateY(0);
}

.form-submit {
  display: inline-block;
  background: #6dabe4;
  color: #fff;
  border-bottom: none;
  width: auto;
  padding: 15px 39px;
  border-radius: 5px;
  -moz-border-radius: 5px;
  -webkit-border-radius: 5px;
  -o-border-radius: 5px;
  -ms-border-radius: 5px;
  margin-top: 25px;
  cursor: pointer;
}
.form-submit:hover {
  background: #4292dc;
}

.form-group {
  position: relative;
  margin-bottom: 25px;
  overflow: hidden;
}
.form-group:last-child {
  margin-bottom: 0px;
}
.register-form {
  width: 100%;
}
.container {
  width: 900px;
  background: #fff;
  margin: 0 auto;
  box-shadow: 0px 15px 16.83px 0.17px rgba(0, 0, 0, 0.05);
  -moz-box-shadow: 0px 15px 16.83px 0.17px rgba(0, 0, 0, 0.05);
  -webkit-box-shadow: 0px 15px 16.83px 0.17px rgba(0, 0, 0, 0.05);
  -o-box-shadow: 0px 15px 16.83px 0.17px rgba(0, 0, 0, 0.05);
  -ms-box-shadow: 0px 15px 16.83px 0.17px rgba(0, 0, 0, 0.05);
  border-radius: 20px;
  -moz-border-radius: 20px;
  -webkit-border-radius: 20px;
  -o-border-radius: 20px;
  -ms-border-radius: 20px;
}

@media screen and (max-width: 1200px) {
  .container {
    width: calc(100% - 30px);
    max-width: 100%;
  }
}
@media screen and (min-width: 1024px) {
  .container {
    max-width: 1200px;
  }
}
@media screen and (max-width: 768px) {
  .form-title {
    text-align: center;
  }
  .form-button {
    text-align: center;
  }
}
.form-title {
  margin-bottom: 33px;
}
display-flex,
.display-flex,
.display-flex-center,
.signup-content,
.signin-content,
.social-login,
.socials {
  display: flex;
  display: -webkit-flex;
}
.signup {
  margin-bottom: 150px;
}

.signup-content {
  padding: 75px 0;
}

.signup-form,
.signup-image,
.signin-form,
.signin-image {
  width: 50%;
  overflow: hidden;
}

.signup-image {
  margin: 0 55px;
}
.signup-image {
  margin-top: 45px;
}
.signup-form {
  margin-left: 75px;
  margin-right: 75px;
  padding-left: 34px;
}
.signup-image-link {
  font-size: 14px;
  color: #222;
  display: block;
  text-align: center;
}
@media screen and (max-width: 768px) {
  .signup-content,
  .signin-content {
    flex-direction: column;
    -moz-flex-direction: column;
    -webkit-flex-direction: column;
    -o-flex-direction: column;
    -ms-flex-direction: column;
    justify-content: center;
    -moz-justify-content: center;
    -webkit-justify-content: center;
    -o-justify-content: center;
    -ms-justify-content: center;
  }

  .signup-form {
    margin-left: 0px;
    margin-right: 0px;
    padding-left: 0px;
    /* box-sizing: border-box; */
    padding: 0 30px;
  }
  .signup-form,
  .signup-image,
  .signin-form,
  .signin-image {
    width: auto;
  }
}
</style>