import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SettingView from "../views/SettingView.vue";
import VtuberView from "../views/VtuberView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/setting",
    name: "setting",
    component: SettingView,
  },
  {
    path: "/vtuber",
    name: "vtuber",
    component: VtuberView,
  },
  {
    path: "/test",
    name: "test",
    component: () =>
    import(/* webpackChunkName: "about" */ "../views/TestView.vue"),
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
