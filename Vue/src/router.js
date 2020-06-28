import Vue from "vue";
import VueRouter from "vue-router";
import Home from "./alpha/Landing";
import Login from "./alpha/auth/login/login";
import LoginMain from "./alpha/auth/login/loginMain";
import SignUpMain from "./alpha/auth/signup/signup";
import SignUpMainTeacher from "./alpha/auth/signup/signupteacher";
import Dashboard from "./alpha/courses/dashboard";

import Recent from "./alpha/courses/Recent";
import SchoolLevel from "./alpha/courses/SchoolLevel";
import PlusTwoLevel from "./alpha/courses/PlusTwoLevel";
import BachelorLevel from "./alpha/courses/BachelorLevel";
import learnZone from "./alpha/learningZone/MainView";
import learnZoneView from "./alpha/learningZone/Main";
import learnZoneViewSets from "./alpha/learningZone/sets";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    component: Login,
    children: [{ path: "", component: LoginMain }],
  },
  {
    path: "/signup",
    component: SignUpMain,
  },
  {
    path: "/signupteacher",
    component: SignUpMainTeacher,
  },
  {
    path: "/dashboard",
    component: Dashboard,
    children: [
      { path: "", component: Recent },
      { path: "schoollevel", component: SchoolLevel },
      { path: "plustwolevel", component: PlusTwoLevel },
      { path: "bachelorlevel", component: BachelorLevel },
    ],
  },
  {
    path: "/learnZone",
    component: learnZone,
    children: [
      { path: "", component: learnZoneView },
      { path: "sets", component: learnZoneViewSets },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
