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
          <component
            :is="currentClock"
            :key="store.state.clockStyle"
          ></component>
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
import Clock2 from "@/components/clocks/Clock2.vue";
import SidebarItem from "@/components/SidebarItem.vue";
import { computed, provide, ref, watch } from "vue";
import { useStore } from "vuex";

const props = defineProps(["sidebarItems"]);
const emit = defineEmits(["updateshowSidebar"]);
const store = useStore();

const showSidebar = ref(true);
const menuHover = ref(false);
const menuScroll = ref(false);
const sidebarWidth = ref(200);
const totalId = ref(0);
const currentItemHover = ref(null);
let clockMap = new Map().set("Clock1", Clock1).set("Clock2", Clock2);
let currentClock = clockMap.get(store.state.clockStyle);

const mouseEnterEvent = computed(() => {
  return !showSidebar.value ? "mouseenter" : null;
});
const mouseLeaveEvent = computed(() => {
  return !showSidebar.value ? "mouseleave" : null;
});
const menuScrollEvent = computed(() => {
  return !showSidebar.value ? "scroll" : null;
});
const clockStyle = computed(() => {
  return store.state.clockStyle;
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
  console.log(currentClock);
  sidebarWidth.value = newShowSidebar ? 200 : 40;
  emit("updateshowSidebar", newShowSidebar);
  if (!newShowSidebar) {
    updateMenuHover(true);
  }
});
watch(clockStyle, (newClockStyle) => {
  currentClock = clockMap.get(newClockStyle);
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
  transition: 0.2s;
  display: flex;
  flex-flow: column;
  z-index: 849;
  &.white-theme {
    border-right: 1px solid rgb(0, 0, 0, 0.5);
  }
  &.black-theme {
    border-right: 1px solid rgb(255, 255, 255, 0.5);
  }
}
.clock {
  height: 140px;
  transition: 0.2s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  height: 0px;
}
.fade-enter-to,
.fade-leave-from {
  opacity: 1;
  height: 140px;
}
.fade-enter-active,
.fade-leave-active {
  transition: all 0.2s ease;
}
.menuHeader {
  margin-inline-start: auto;
  margin-inline-end: auto;
  border-style: inset;
  border-width: 2px;
  border-radius: 6px;
  width: 80%;
  opacity: 0.5;
  transition: 0.2s;
  .white-theme & {
    border-color: #000000;
    background: #000000;
  }
  .black-theme & {
    border-color: #ffffff;
    background: #ffffff;
  }
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