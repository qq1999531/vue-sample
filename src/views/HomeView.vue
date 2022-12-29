<template>
  <div class="home">
    <!--<img alt="Vue logo" src="../assets/logo.png">-->
    <!--<HelloWorld msg="Welcome to Your Vue.js App"/>-->
    <Sidebar @showSidebarEvent="showSidebarEvent" />
    <div class="homeMain" style="padding-left: 40px">home</div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import Sidebar from "@/components/Sidebar.vue";
import $ from "jquery";
export default {
  name: "HomeView",
  components: {
    HelloWorld,
    Sidebar,
  },
  methods: {
    showSidebarEvent(showSidebarFactor) {
      $(".homeMain").css("padding-left", 200 * showSidebarFactor.value);
      console.log(showSidebarFactor.value);
    },
  },
};
</script>

<style lang="scss">
.homeMain{
  transition: 0.2s;
}
</style>>
