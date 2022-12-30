<template>
  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
  <router-view />
</template>

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
</style>
