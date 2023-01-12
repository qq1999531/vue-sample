<template>
  <header class="header sidebarExpanded white-theme">this is header!</header>
</template>
<style lang="scss">
.header {
  height: 50px;
  z-index: 700;
  transition: 0.2s;
  &.sidebarExpanded {
    padding-left: 200px;
  }
  &.sidebarCollapsed {
    padding-left: 40px;
  }
  &.white-theme {
    border-bottom: 1px solid rgb(0, 0, 0, 0.5);
  }
  &.black-theme {
    border-bottom: 1px solid rgb(255, 255, 255, 0.5);
  }
}
</style>