<template>
  <nav
    class="sidebar white-theme"
    :style="{ width: 200 * showSidebarFactor + 'px' }"
  >
    <div style="height: 100%">
      <transition name="fade">
        <div v-show="showSidebar" class="clock">
          <slot name="sidebarClock">
            <Clock1 :showSidebarFactor="showSidebarFactor" />
          </slot>
        </div>
      </transition>
      <div v-show="showSidebar" class="menuHeader"></div>
      <div style="height: 100%" class="menuFooter"></div>
    </div>
    <div class="bottomBtn" @click="toggleSidebar">
      <div
        class="icons"
        :class="{
          leftSpin: showSidebar,
          rightSpin: !showSidebar,
        }"
      ></div>
    </div>
  </nav>
</template>

<script setup>
import Clock1 from "@/components/clocks/Clock1.vue";
import { computed, ref, watch } from "vue";

const emit = defineEmits(["showSidebarEvent"]);

const showSidebar = ref(true);
const showSidebarFactor = computed(() => {
  return showSidebar.value ? 1 : 0.2;
});

function toggleSidebar() {
  showSidebar.value = !showSidebar.value;
}

watch(showSidebar, (newShowSidebar) => {
  console.log(`showSidebar is ${newShowSidebar}`);
  emit("showSidebarEvent", showSidebarFactor);
});
</script>

<style lang="scss">
@use "../scss/icons.scss";
.sidebar {
  overflow: hidden;
  height: 100%;
  position: fixed;
  border-right: 1px solid rgb(127, 127, 127);
  transition: 0.2s;
  display: flex;
  flex: 1 1 auto;
  flex-flow: column;
}
.white-theme {
  background-color: rgb(255, 255, 255);
}
.black-theme {
  background-color: rgb(0, 0, 0);
}
.clock {
  height: 140px;
  transition: 0.2s;
}
.fade-enter-from {
  opacity: 0;
}
.fade-enter-to {
  opacity: 1;
}
.fade-enter-active,
.fade-leave-active {
  transition: all 0.2s ease;
}
.fade-leave-from {
  opacity: 1;
}
.fade-leave-to {
  opacity: 0;
}
.menuHeader {
  margin-inline-start: auto;
  margin-inline-end: auto;
  border-style: inset;
  border-width: 2px;
  border-radius: 10px;
  width: 80%;
  border-color: #000000;
  opacity: 0.5;
  transition: 0.2s;
  background: #000000;
}
.menuFooter {
  flex-flow: column;
  display: flex;
  flex: 0 1 auto;
}
.bottomBtn {
  cursor: pointer;
  transition: 0.2s;
  display: flex;
  justify-content: center;
  height: 50px;
  align-items: center;
}
.rightSpin {
  transform: rotate(90deg);
}
.leftSpin {
  transform: rotate(-90deg);
}
</style>