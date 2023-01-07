<template>
  <div ref="menuItem" class="menu-item-base alignCenter">
    <!--<div v-if="active" class="BlockBack"></div> -->
    <!-- ======================== -->
    <!-- ======================== -->
    <!-- 1 this is the menu label -->
    <!-- ======================== -->
    <!-- ======================== -->

    <div class="label TransBG">
      <div
        class="left"
        ref="labelRef"
        :class="{
          marginAuto: !showSidebar && depth == 0,
          collapseEnd: !showSidebar,
        }"
      >
        <i aria-hidden="true" class="material-symbols-outlined">{{
          item.icon.text
        }}</i>
        <span class="labelName">{{ labelName }}</span>
      </div>
      <template v-if="(!showSidebar && depth != 0) || showSidebar">
        <div
          v-if="item.children"
          class="icons postIconOpenAnima"
          :class="{ opened: showChildren }"
        ></div>
      </template>
    </div>

    <!-- ========================================================= -->
    <!-- ========================================================= -->
    <!--2 this container is for when menu Children when full width -->
    <!-- ========================================================= -->
    <!-- ========================================================= -->
    <div v-if="showSidebar || (depth != 0 && !showSidebar)">
      <div
        class="items-container"
        :style="{ maxHeight: heifOfContainer, transition: transitionTime }"
        ref="container"
        v-if="item.children"
      >
        <template v-if="renderChildren">
          <SidebarItem
            v-for="(item, index) in item.children"
            :key="index"
            :item="item"
            :depth="depth + 1"
          />
        </template>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- ========================================== -->
    <!--3  this container is for mini Menu Children -->
    <!-- ========================================== -->
    <!-- ========================================== -->

    <div
      v-if="!showSidebar && depth == 0 && !collapsed"
      :class="{ topContainer: depth == 0, vasopacitiy: !expanded }"
      ref="topContainerRef"
      :style="{
        [MakeSpace
          ? 'bottom'
          : 'top']: `calc(${ContainerOffsetYConputed} - 1px)`,
        left: `calc(${widthMiniMenu} - 1px)`,
        maxHeight: TopcontainerHiefht,
        width: showChildren ? '250px' : '0px',
        zIndex: showChildren ? '850' : '849',
        animationDelay: seTAnimationTimeOut ? '0.3s' : '0',
      }"
    >
      <div
        @click="miniLabelClick"
        @mousewheel="mousewheelop"
        class="labelMini"
        :class="{
          [miniActiveClass]: miniActive,
          [activeClass]: active,
        }"
        :style="{
          position: 'fixed',
          whiteSpace: 'nowrap',
          left: menuType == 'fully' ? '0px' : miniLabelDirection,
          width: miniLabelWidth,
          [MakeSpace ? 'bottom' : 'top']: ContainerOffsetYConputed,
          opacity: depth == 0 && showChildren ? '1' : '0',
        }"
      >
        <!--main menu btn-->
        <div
          v-if="showChildren"
          class="left"
          :class="{ marginAuto: !showSidebar && depth == 0 }"
          :style="{
            left: widthMiniMenu,
            top: labelMiniYYofsset + 'px',
          }"
        >
          <span class="labelName">{{ item?.name }}</span>
        </div>
      </div>
      <div class="labelminiSub" v-if="depth == 0 && !MakeSpace"></div>
      <div
        class="items-container"
        :style="{
          maxHeight: heifOfContainer,
          transition: transitionTime,
        }"
        ref="container"
        v-if="item.children"
      >
        <template v-if="renderChildren">
          <SidebarItem
            v-for="(item, index) in item.children"
            :key="index"
            :item="item"
            :depth="depth + 1"
            :setMaxHeightTopCProp="setMaxHeightTopC"
          />
        </template>
      </div>
      <div class="labelminiSub" v-if="depth == 0 && MakeSpace"></div>
    </div>
  </div>
</template>

<script setup>
import SidebarItem from "@/components/SidebarItem.vue";
import { computed, nextTick, onActivated, ref } from "@vue/runtime-core";
import { useRouter } from "vue-router";

const props = defineProps(["item", "depth", "setMaxHeightTopCProp"]);
const router = useRouter();

const showSidebar = inject("showSidebar");
const MakeSpace = ref(false);
const active = ref(false);
const miniActive = ref(false);
const showChildren = ref(false);
const expanded = ref(false);
const renderChildren = ref(false);
const cacheHeight = ref(null);
const containerHeight = ref("0");
const TopcontainerHeight = ref("fit-content");
const menuItem = ref();
const topContainerRef = ref();
const hieghtTimeout = null;
const topConTime = null;
const renderTimeOut = null;

const labelName = computed(() => {
  if (!showSidebar) {
    return props.depth != 0 ? props.item?.name : false;
  }
  return props.item?.name;
});

function setMaxHeightTopC() {
  const x = topContainerRef?.getBoundingClientRect();
  if (MakeSpace) {
    TopcontainerHeight = x.height + "px";
  } else {
    TopcontainerHeight = x.height - (x.top + x.height) - 2 + "px";
  }
}
function setSmallMenuDataForToggle(val) {
  clearTimeout(topConTime);
  clearTimeout(hieghtTimeout);
  clearTimeout(renderTimeOut);
  nextTick(() => {
    expanded = val;
  });
  showChildren = val;
}
function openItemCildren() {
  if (props.depth == 1 && !showSidebar) {
    props.setMaxHeightTopCProp();
  }
  if (!showSidebar && props.depth == 0) {
    showChildren = true;
    nextTick(() => {
      expanded = true;
    });
  }
  if (!props.item?.children) return;
  if (expanded) return;
  setSmallMenuDataForToggle(true);
  renderChildren = true;
  if (cacheHeight) {
    containerHeight = cacheHeight;
  } else {
    containerHeight = props.item?.children.length * menuItem.offsetHeight + 3;
  }
  cacheHeight = null;
  if (!showSidebar && props.depth == 0) {
    containerHeight = "fit-content";
  }
  //add animation
  hieghtTimeout = setTimeout(() => {
    containerHeight = "fit-content";
  }, 200);
}
function extractChildrenRoutes(obj, keyToFind) {
    if (!obj) return
    return Object.entries(obj).reduce(
      (acc, [key, value]) =>
        key == keyToFind
          ? acc.concat(value)
          : typeof value == 'object'
          ? acc.concat(extractChildrenRoutes(value, keyToFind))
          : acc,
      []
    )
  }
function isCurrentUrl(url) {
  let location = window.location;
  return (
    location.href == location.origin + url ||
    location.pathname + location.hash == url ||
    location.pathname + location.search == url ||
    location.href == url ||
    location.hash == url
  );
}
function resloveHref(href) {
  if (router) {
    const x = router.resolve(href);
    return x.href;
  }
  return href;
}
function checkActive() {
  if (props.item?.href && isCurrentUrl(resloveHref(props.item?.href))) {
    active = true;
    miniActive = false;
  } else {
    active = false;
    if (!props.item?.children) return;
    let hasFound = false;
    let x = extractChildrenRoutes(props.item?.children, "href") || [];
    for (var i = 0; i < x.length; i++) {
      if (isCurrentUrl(resloveHref(x[i]))) {
        hasFound = true;
        // clearTimeout(hieghtTimeout)
        // clearTimeout(renderTimeOut)
        miniActive = true;
        if (menuMounted || !showSidebar) break;
        if (ChildrenOpenActiveRoute) {
          openItemCildren();
        }
        break;
      }
    }
    miniActive = hasFound;
  }
}

onActivated(() => {
  checkActive();
});
</script>