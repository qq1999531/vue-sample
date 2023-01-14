<template>
  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
  <Sidebar @updateshowSidebar="updateshowSidebar" :sidebarItems="defaultMenu" />
  <Header />
  <div class="router-viewContainer sidebarExpanded white-theme">
    <router-view />
  </div>
</template>

<script setup>
import Sidebar from "@/components/Sidebar.vue";
import Header from "@/components/Header.vue";
import $ from "jquery";
import { useStore } from "vuex";
import { computed, watch } from "@vue/runtime-core";

const appStore = useStore();

const defaultMenu = [
  {
    name: "Home",
    href: "/",
    icon: { text: "home" },
  },
  {
    name: "Settings",
    href: "setting",
    icon: { text: "settings" },
  },
];

const appTheme = computed(() => {
  return appStore.state.appTheme;
});

function updateshowSidebar(showSidebar) {
  if (showSidebar) {
    $(".sidebarCollapsed")
      .addClass("sidebarExpanded")
      .removeClass("sidebarCollapsed");
  } else {
    $(".sidebarExpanded")
      .addClass("sidebarCollapsed")
      .removeClass("sidebarExpanded");
  }
}

watch(appTheme, (newAppTheme, oldAppTheme) => {
  $("." + oldAppTheme)
    .addClass(newAppTheme)
    .removeClass(oldAppTheme);
});
</script>

<style lang="scss">
$material-symbols-font-path: "~material-symbols/";
@import "material-symbols";
* {
  padding: 0px;
  margin: 0px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased; //字体抗锯齿
  -moz-osx-font-smoothing: grayscale; //字体抗锯齿
  text-align: center;
  height: 100%;
}
.white-theme {
  background-color: rgb(255, 255, 255);
  color: #000000;
}
.black-theme {
  background-color: rgb(0, 0, 0);
  color: #ffffff;
}
.router-viewContainer {
  overflow-y: auto;
  transition: 0.2s;
  height: calc(100vh - 51px);
  &.sidebarExpanded {
    padding-left: 200px;
  }
  &.sidebarCollapsed {
    padding-left: 40px;
  }
}
</style>
