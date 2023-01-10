<template>
  <nav
    class="sidebar white-theme"
    :style="{ width: sidebarWidth + 'px' }"
    @[mouseEnterEvent]="onEnter"
    @[mouseLeaveEvent]="onLeave"
  >
    <div style="height: 100%">
      <transition name="fade">
        <div v-show="showSidebar" class="clock">
          <slot name="sidebarClock">
            <Clock1 />
          </slot>
        </div>
      </transition>
      <div v-show="showSidebar" class="menuHeader"></div>
      <div
        @[menuScrollEvent]="onMenuScroll"
        class="menuWraper"
        :class="{
          miniCoolapseMenu: !showSidebar,
        }"
      >
        <template v-for="(item, index) in props.sidebarItems" :key="index">
          <SidebarItem :item="item" :depth="0" />
        </template>
        <div class="menuFooter"></div>
      </div>
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
import SidebarItem from "@/components/SidebarItem.vue";
import { computed, provide, ref, watch } from "vue";

const props = defineProps(["sidebarItems"]);
const emit = defineEmits(["updateshowSidebar"]);

const showSidebar = ref(true);
const menuHover = ref(false);
const menuScroll = ref(false);
const sidebarWidth = ref(200);
const totalId = ref(0);
const currentItemHover = ref(null);

const mouseEnterEvent = computed(() => {
  return !showSidebar.value ? "mouseenter" : null;
});
const mouseLeaveEvent = computed(() => {
  return !showSidebar.value ? "mouseleave" : null;
});
const menuScrollEvent = computed(() => {
  return !showSidebar.value ? "scroll" : null;
});

function toggleSidebar() {
  showSidebar.value = !showSidebar.value;
}
function updateCurrentItemHover(id) {
  currentItemHover.value = id;
}
function updateId() {
  totalId.value++;
  return totalId.value;
}
function updateMenuHover(val) {
  menuHover.value = val;
}
function onEnter() {
  updateMenuHover(true);
}
function onLeave() {
  updateMenuHover(false);
}
function onMenuScroll() {
  menuScroll.value = !menuScroll.value;
}

watch(showSidebar, (newShowSidebar) => {
  sidebarWidth.value = newShowSidebar ? 200 : 40;
  emit("updateshowSidebar", newShowSidebar);
  if (!newShowSidebar) {
    updateMenuHover(true);
  }
});

provide("showSidebar", showSidebar);
provide("currentItemHover", currentItemHover);
provide("updateCurrentItemHover", updateCurrentItemHover);
provide("updateId", updateId);
provide("menuHover", menuHover);
provide("menuScroll", menuScroll);
</script>

<style lang="scss">
@use "../scss/icons.scss";
.sidebar {
  overflow: hidden;
  height: 100%;
  position: fixed;
  border-right: 1px solid rgb(0, 0, 0, 0.5);
  transition: 0.2s;
  display: flex;
  flex-flow: column;
  z-index: 849;
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
  height: 100%;
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
.menuWraper {
  height: 100%;
  display: flex;
  flex-flow: column;
  overflow-y: overlay;
  overflow-x: hidden;
}
</style>