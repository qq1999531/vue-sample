<template>
  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
  <Sidebar @updateshowSidebar="updateshowSidebar" />
  <router-view />
  {{ showSidebar }}
</template>

<script setup>
import Sidebar from "@/components/Sidebar.vue";
import $ from "jquery";

function updateshowSidebar(ShowSidebar) {
  if (ShowSidebar) {
    $(".sidebarCollapsed")
      .addClass("sidebarExpanded")
      .removeClass("sidebarCollapsed");
  } else {
    $(".sidebarExpanded")
      .addClass("sidebarCollapsed")
      .removeClass("sidebarExpanded");
  }
}
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
  color: #000000;
}
.white-theme {
  background-color: rgba(255, 255, 255);
}
.black-theme {
  background-color: rgb(0, 0, 0);
}
</style>
