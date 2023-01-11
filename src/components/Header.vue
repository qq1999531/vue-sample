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
}
</style>