<template>
  <div
    ref="menuItem"
    class="menu-item-base"
    :class="{
      MenuItemWidthOnMiniCollapse: !showSidebar && props.depth != 0,
    }"
  >
    <!-- 1 this is the menu label -->

    <div
      class="label"
      @[shouldMouseEnterEvent]="hover = true"
      @[shouldMouseLeaveEvent]="hover = false"
      @click="labelClick"
      :style="{
        paddingLeft: `${props.depth * 18}px`,
      }"
      :class="{
        TransitionC: showSidebar || (!showSidebar && !showChildren),
        activeClass: active,
        labelHoverClass: (props.depth != 0 && !showSidebar) || showSidebar,
      }"
    >
      <div
        class="left"
        ref="labelRef"
        :class="{
          marginAuto: !showSidebar && props.depth == 0,
        }"
      >
        <i aria-hidden="true" class="material-symbols-outlined">{{
          props.item.icon.text
        }}</i>
        <span v-show="labelName" class="labelName">{{ labelName }}</span>
      </div>
      <template v-if="(!showSidebar && props.depth != 0) || showSidebar">
        <div
          v-if="props.item.children"
          class="icons postIconOpenAnima"
          :class="{ opened: showChildren }"
        ></div>
      </template>
    </div>

    <!--2 this container is for when menu Children when full width -->

    <div v-if="showSidebar || (props.depth != 0 && !showSidebar)">
      <div
        style="transition: 0.2s"
        class="items-container"
        :style="{
          maxHeight:
            containerHeight == 'fit-content'
              ? containerHeight
              : containerHeight + 'px',
        }"
        ref="container"
        v-if="props.item.children"
      >
        <template v-if="renderChildren">
          <SidebarItem
            v-for="(item, index) in props.item.children"
            :key="index"
            :item="props.item"
            :depth="props.depth + 1"
          />
        </template>
      </div>
    </div>

    <!--3  this container is for mini Menu Children -->

    <div
      v-if="!showSidebar && props.depth == 0"
      :class="{ topContainer: props.depth == 0, vasopacitiy: !expanded }"
      ref="topContainerRef"
      :style="{
        [makeSpace
          ? 'bottom'
          : 'top']: `calc(${containerOffsetYConputed} - 1px)`,
        left: '40px',
        maxHeight: topcontainerHeight,
        width: showChildren ? '200px' : '0px',
        zIndex: showChildren ? '850' : '849',
        animationDelay: seTAnimationTimeOut ? '0.2s' : '0',
      }"
    >
      <div
        @click="clickCompose"
        @mousewheel="mousewheelop"
        class="labelMini"
        :class="{
          activeClass: active,
          showLabelMini: props.depth == 0 && showChildren,
          unshowLabelMini: !(props.depth == 0 && showChildren),
        }"
        :style="{
          position: 'fixed',
          whiteSpace: 'nowrap',
          left: '0px',
          height: '40px',
          width: miniLabelWidth,
          [makeSpace ? 'bottom' : 'top']: containerOffsetYConputed,
          opacity: props.depth == 0 && showChildren ? '1' : '0',
        }"
      >
        <!--main menu btn-->
        <div
          v-if="showChildren"
          class="left"
          :class="{ marginAuto: !showSidebar && props.depth == 0 }"
          :style="{
            left: '40px',
            top: labelMiniYYofsset + 'px',
          }"
        >
          <span class="labelName">{{ props.item?.name }}</span>
        </div>
      </div>
      <div style="height: 40px" v-if="depth == 0 && !makeSpace"></div>
      <div
        class="items-container"
        :style="{
          maxHeight:
            containerHeight == 'fit-content'
              ? containerHeight
              : containerHeight + 'px',
          transition: '0.2s',
        }"
        ref="container"
        v-if="props.item.children"
      >
        <template v-if="renderChildren">
          <SidebarItem
            v-for="(item, index) in props.item.children"
            :key="index"
            :item="props.item"
            :depth="props.depth + 1"
            :setMaxHeightTopCProp="setMaxHeightTopC"
          />
        </template>
      </div>
      <div style="height: 40px" v-if="depth == 0 && makeSpace"></div>
    </div>
  </div>
</template>

<script setup>
import SidebarItem from "@/components/SidebarItem.vue";
import {
  computed,
  inject,
  nextTick,
  onActivated,
  onMounted,
  ref,
  watch,
} from "@vue/runtime-core";
import { useRouter } from "vue-router";

const props = defineProps(["item", "depth", "setMaxHeightTopCProp"]);
const router = useRouter();

const showSidebar = inject("showSidebar");
const currentItemHover = inject("currentItemHover");
const updateCurrentItemHover = inject("updateCurrentItemHover");
const updateId = inject("updateId");
const menuHover = inject("menuHover");
const menuScroll = inject("menuScroll");
const makeSpace = ref(false);
const hover = ref(false);
const active = ref(false);
const showChildren = ref(false);
const expanded = ref(false);
const renderChildren = ref(false);
const seTAnimationTimeOut = ref(false);
const containerHeight = ref("0");
const containerOffsetY = ref(0);
const labelMiniYYofsset = ref(0);
const topcontainerHeight = ref("fit-content");
const currentRoute = ref(window.location);
const menuItem = ref();
const topContainerRef = ref();
const labelRef = ref();
const container = ref();
let cacheHeight = null;
let id = null;
let heightTimeout = null;
let topConTime = null;
let renderTimeOut = null;

const labelName = computed(() => {
  if (!showSidebar.value) {
    return props.depth != 0 ? props.item?.name : false;
  } else {
    return props.item?.name;
  }
});
const shouldMouseEnterEvent = computed(() => {
  return !showSidebar.value && props.depth == 0 ? "mouseenter" : null;
});
const shouldMouseLeaveEvent = computed(() => {
  return !showSidebar.value && props.depth == 0 ? "mouseleave" : null;
});
const containerOffsetYConputed = computed(() => {
  return `${containerOffsetY.value}px`;
});
const miniLabelWidth = computed(() => {
  return expanded.value
    ? `calc(${menuItem.value.clientWidth}px + 205px - 1.5px)`
    : `40px`;
});

function mousewheelop(w) {
  document.querySelector(".sidebar").scrollBy(0, w.deltaY);
}
function clickCompose() {
  if (props.item?.href && router) router?.push(props.item?.href);
}
function toggleMenu() {
  if (!props.item?.children) return;
  clearTimeout(heightTimeout);
  clearTimeout(renderTimeOut);
  if (showChildren.value) {
    closeItemChildren();
  } else {
    openItemCildren();
  }
}
function labelClick() {
  clickCompose();
  if (!hover.value) {
    toggleMenu();
  }
}
function setMaxHeightTopC() {
  const x = topContainerRef?.value.getBoundingClientRect();
  if (makeSpace.value) {
    topcontainerHeight.value = x.height + "px";
  } else {
    topcontainerHeight.value = x.height - (x.top + x.height) - 2 + "px";
  }
}
function setItemOffsetHeight() {
  if (props.depth == 0) {
    const x = menuItem.value.getBoundingClientRect();
    containerOffsetY.value = x.top;
    makeSpace.value = false;
  }
}
function setSmallMenuDataForToggle(val) {
  clearTimeout(topConTime);
  clearTimeout(heightTimeout);
  clearTimeout(renderTimeOut);
  nextTick(() => {
    expanded.value = val;
  });
  showChildren.value = val;
}
function openItemCildren() {
  if (props.depth == 1 && !showSidebar.value) {
    props.setMaxHeightTopCProp();
  }
  if (!showSidebar.value && props.depth == 0) {
    showChildren.value = true;
    nextTick(() => {
      expanded.value = true;
    });
  }
  if (!props.item?.children) return;
  if (expanded.value) return;
  setSmallMenuDataForToggle(true);
  renderChildren.value = true;
  if (cacheHeight) {
    containerHeight.value = cacheHeight;
  } else {
    containerHeight.value =
      props.item?.children.length * menuItem.value.offsetHeight + 3;
  }
  cacheHeight = null;
  if (!showSidebar.value && props.depth == 0) {
    containerHeight.value = "fit-content";
  }
  //add animation
  heightTimeout = setTimeout(() => {
    containerHeight.value = "fit-content";
  }, 200);
}
function closeItemChildren() {
  seTAnimationTimeOut.value = false;
  if (!showSidebar.value && props.depth == 0) {
    setSmallMenuDataForToggle(false);
    topConTime = setTimeout(() => {
      containerHeight.value = 0;
      topConTime = null;
    }, 200);
    return;
  }
  setSmallMenuDataForToggle(false);
  if (!props.item?.children) return;
  if (!cacheHeight) {
    cacheHeight = container.value?.offsetHeight;
  }
  containerHeight.value = container.value?.offsetHeight;
  //this line must be pushed to top of call stack
  setTimeout(() => {
    containerHeight.value = 0;
  }, 0);
  renderTimeOut = setTimeout(() => {
    renderChildren.value = false;
    cacheHeight = null;
  }, 200);
}
function extractChildrenRoutes(obj, keyToFind) {
  if (!obj) return;
  return Object.entries(obj).reduce(
    (acc, [key, value]) =>
      key == keyToFind
        ? acc.concat(value)
        : typeof value == "object"
        ? acc.concat(extractChildrenRoutes(value, keyToFind))
        : acc,
    []
  );
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
    active.value = true;
  } else {
    active.value = false;
    if (!props.item?.children) return;
    let x = extractChildrenRoutes(props.item?.children, "href") || [];
    for (var i = 0; i < x.length; i++) {
      if (isCurrentUrl(resloveHref(x[i]))) {
        if (!showSidebar.value) break;
        openItemCildren();
        break;
      }
    }
  }
}

watch(hover, (newHover) => {
  if (!id) {
    id = updateId();
  }
  if (newHover) {
    seTAnimationTimeOut.value = true;
    updateCurrentItemHover(id);
    openItemCildren();
    nextTick(() => {
      setTimeout(() => {
        setItemOffsetHeight();
      }, 0);
      const y = labelRef.value.getBoundingClientRect();
      labelMiniYYofsset.value = y.top + 2;
    });
  } else {
    if (currentItemHover.value == id && menuHover) {
    } else {
      closeItemChildren();
    }
  }
});
watch(currentRoute, () => {
  checkActive();
});
watch(menuHover, (newMenuHover) => {
  if (!newMenuHover) {
    closeItemChildren();
  }
});
watch(currentItemHover, (newCurrentItemHover) => {
  if (newCurrentItemHover != id) {
    closeItemChildren();
  }
});
watch(menuScroll, () => {
  setItemOffsetHeight();
  const y = labelRef.value.getBoundingClientRect();
  labelMiniYYofsset.value = y.top + 2;
});
watch(showSidebar, () => {
  closeItemChildren();
  nextTick(() => {
    setItemOffsetHeight();
  });
});

onActivated(() => {
  checkActive();
});
onMounted(() => {
  setItemOffsetHeight();
});
</script>
<style lang="scss">
%hoverPointer {
  @media (hover: hover) and (pointer: fine) {
    cursor: pointer;
  }
  @media (hover: none) and (pointer: coarse) {
    cursor: none;
  }
}
.menu-item-base {
  align-self: center;
  width: 90%;
  .menu-icon,
  .labelName {
    transition: color 0.2s ease;
  }
  .label .left {
    &.marginAuto {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
  }
  .labelMini .left {
    align-items: center;
    &.marginAuto {
      position: fixed;
    }
  }
  //position: relative;
  .labelMini {
    transition: width 0.2s;
    //flex-direction: row;
    //justify-content: center;
    //display: flex;
    //align-items: center;
    //align-self: center;
    user-select: none;
    .white-theme & {
      background-color: #ffffff;
    }
    .black-theme & {
      background-color: #000000;
    }
    &.showLabelMini {
      transition: opacity 0s;
    }
    &.unshowLabelMini {
      transition: opacity 1s;
    }
    > .left {
      display: flex;
    }
    z-index: 851;
    @extend %hoverPointer;
  }
  .label {
    transform-style: preserve-3d;
    display: flex;
    user-select: none;
    position: relative;
    box-sizing: border-box;
    height: 40px;
    z-index: 853;
    .left {
      display: flex;
      align-items: center;
      .labelName {
        padding-left: 10px;
      }
    }

    @extend %hoverPointer;
  }
  .hoverClass {
    @extend %hoverPointer;
  }
  .topContainer {
    overflow-y: overlay;
    position: fixed;
    transition: width 0.2s ease;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
    .white-theme & {
      background: #ffffff;
      border-top: 1px solid rgb(0, 0, 0, 0.5);
      border-bottom: 1px solid rgb(0, 0, 0, 0.5);
      border-right: 1px solid rgb(0, 0, 0, 0.5);
    }
    .black-theme & {
      background: #000000;
      border-top: 1px solid rgb(255, 255, 255, 0.5);
      border-bottom: 1px solid rgb(255, 255, 255, 0.5);
      border-right: 1px solid rgb(255, 255, 255, 0.5);
    }
  }
  .vasopacitiy {
    animation: myOpac 0s;
    animation-fill-mode: forwards;
  }
  @keyframes myOpac {
    from {
      opacity: 1;
    }
    to {
      opacity: 0;
    }
  }

  &.MenuItemWidthOnMiniCollapse {
    margin-left: auto;
  }
  .icons {
    content: "";
    height: 1.25rem;
    min-width: 1.25rem;
    width: 1.25rem;
    margin-left: auto;
    -webkit-transform: rotate(90deg);
    transform: rotate(90deg);
  }
  .icons.opened {
    padding: auto;
    -webkit-transform: rotate(180deg) !important;
    transform: rotate(180deg) !important;
  }
}
.items-container {
  .sidebar & {
    height: fit-content;
    overflow: hidden;
  }
}
.TransitionC {
  .sidebar & {
    transition: background-color 0.2s;
  }
}
.postIconOpenAnima {
  .sidebar & {
    transition: -webkit-transform 200ms linear;
    transition: transform 200ms linear;
    transition: transform 200ms linear, -webkit-transform 200ms linear;
    height: 100%;
  }
}
</style>