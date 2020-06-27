import axios from "axios";
import host from "../../host.js";
const state = {
  token: "",
  error: false,
  user: "",
};
const mutations = {
  SET_TOKEN(state, token) {
    state.token = token;
  },
  SET_ERROR(state, bol) {
    state.error = bol;
  },
  SET_USER(state, user) {
    state.user = user;
  },
  LOGOUT(state) {
    state.token = null;
  },
};
const actions = {
  async Login({ commit, dispatch }, credential) {
    commit("SET_ERROR", false);
    await axios
      .post(host.host + "/rest-auth/login/", {
        username: credential.username,
        password: credential.password,
      })
      .then((res) => {
        console.log(credential.username);
        commit("SET_USER", credential.username);
        commit("SET_TOKEN", res.data.key);
        if (credential.remember) {
          localStorage.setItem("token", res.data.key);
          const now = new Date();
          const expirationDate = new Date(now.getTime() + 3600000);
          localStorage.setItem("expiresIn", expirationDate);
          localStorage.setItem("user", credential.username);
        }
        dispatch("addNotifications", {
          type: "success",
          message: "Login successful",
        });
      })
      .catch((err) => {
        commit("SET_ERROR", true);
      });
  },
  async signupWithGoogle({ commit, dispatch }, resp) {
    let name =resp.Tt.Bd
    const token = resp.wc.access_token;
    await axios
      .post("http://localhost:8000/auth/google/", {
        access_token: token,
      })
      .then((resp) => {
        commit("SET_USER", name);
        commit("SET_TOKEN", resp.data.key);
        dispatch("addNotifications", {
          type: "success",
          message: "Login successful",
        });
        
        dispatch("addNotifications", {
          type: "success",
          message: "Login successful",
        });
      })
      .catch((err) => {
        console.log("error")
        console.log(err.response);
      });
  },
  async signUp({ commit, dispatch }, data) {
    commit("SET_ERROR", false);
    await axios
      .post(host.host + "/registration/", {
        username: data.username,
        email: data.email,
        password1: data.password1,
        password2: data.password2,
      })
      .then((res) => {
        const now = new Date();
        const expirationDate = new Date(now.getTime() + 3600000);
        localStorage.setItem("expiresIn", expirationDate);
        localStorage.setItem("token", res.data.key);
        localStorage.setItem("user", data.username);
        commit("SET_USER", data.username);
        commit("SET_TOKEN", res.data.key);
        dispatch("addNotifications", {
          type: "success",
          message: "SignUp successful",
        });
      })
      .catch((err) => {
        console.log(err);
        console.log("error aayo");
        commit("SET_ERROR", true);
      });
  },
  logout({ commit, dispatch }) {
    localStorage.removeItem("token");
    localStorage.removeItem("expiresIn");
    localStorage.removeItem("user");
    commit("LOGOUT");
    dispatch("addNotifications", {
      type: "danger",
      message: "You are now logged out",
    });
    dispatch("removePaidUser");
  },
};
const getters = {
  getToken: (state) => {
    return state.token;
  },
  getError: (state) => {
    return state.error;
  },
  getUser: (state) => {
    return state.user;
  },
};
export default {
  state,
  getters,
  mutations,
  actions,
};
