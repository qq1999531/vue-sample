<template>
  <div ref="menuItem" class="menu-item-base alignCenter">
    <div v-if="active" class="BlockBack"></div>
    <!-- ======================== -->
    <!-- ======================== -->
    <!-- 1 this is the menu label -->
    <!-- ======================== -->
    <!-- ======================== -->

    <div
      class="label TransBG"
      @[shouldMouseEnterEvent]="hover = true"
      @[shouldMouseLeaveEvent]="hover = false"
      @click="labelClick"
      :style="{
        paddingLeft: `${props.depth * 18}px`,
      }"
      :class="{
        TransitionC: showSidebar || (!showSidebar && !showChildren),
        menuexpand: showChildren,
        activeClass: active,
        miniActiveClass: miniActive,
        labelHoverClass: (props.depth != 0 && !showSidebar) || showSidebar,
      }"
    >
      <div
        class="left"
        ref="labelRef"
        :class="{
          marginAuto: !showSidebar && props.depth == 0,
          collapseEnd: !showSidebar,
        }"
      >
        <i aria-hidden="true" class="material-symbols-outlined">{{
          props.item.icon.text
        }}</i>
        <span class="labelName">{{ labelName }}</span>
      </div>
      <template v-if="(!showSidebar && props.depth != 0) || showSidebar">
        <div
          v-if="props.item.children"
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
            :item="item"
            :depth="props.depth + 1"
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
      v-if="!showSidebar && props.depth == 0"
      :class="{ topContainer: props.depth == 0, vasopacitiy: !expanded }"
      ref="topContainerRef"
      :style="{
        [makeSpace
          ? 'bottom'
          : 'top']: `calc(${containerOffsetYConputed} - 1px)`,
        left: '39px',
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
          miniActiveClass: miniActive,
          activeClass: active,
        }"
        :style="{
          position: 'fixed',
          whiteSpace: 'nowrap',
          left: '0px',
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
            left: widthMiniMenu,
            top: labelMiniYYofsset + 'px',
          }"
        >
          <span class="labelName">{{ item?.name }}</span>
        </div>
      </div>
      <div class="labelminiSub" v-if="props.depth == 0 && !makeSpace"></div>
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
            :depth="props.depth + 1"
            :setMaxHeightTopCProp="setMaxHeightTopC"
          />
        </template>
      </div>
      <div class="labelminiSub" v-if="props.depth == 0 && makeSpace"></div>
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
  ref,
  watch,
} from "@vue/runtime-core";
import { useRouter } from "vue-router";

const props = defineProps(["item", "depth", "setMaxHeightTopCProp"]);
const router = useRouter();

const showSidebar = inject("showSidebar");
const currantItemHover = inject("currantItemHover");
const updateCurrantItemHover = inject("updateCurrantItemHover");
const updateId = inject("updateId");
const menuHover = inject("menuHover");
const makeSpace = ref(false);
const hover = ref(false);
const active = ref(false);
const miniActive = ref(false);
const showChildren = ref(false);
const expanded = ref(false);
const renderChildren = ref(false);
const seTAnimationTimeOut = ref(false);
const containerHeight = ref("0");
const containerOffsetY = ref(0);
const labelMiniYYofsset = ref(0);
const topcontainerHeight = ref("fit-content");
const menuItem = ref();
const topContainerRef = ref();
const labelRef = ref();
const container = ref();
const cacheHeight = null;
const id = null;
const heightTimeout = null;
const topConTime = null;
const renderTimeOut = null;

const labelName = computed(() => {
  if (!showSidebar) {
    return props.depth != 0 ? props.item?.name : false;
  }
  return props.item?.name;
});
const shouldMouseEnterEvent = computed(() => {
  return !showSidebar && props.depth == 0 ? "mouseenter" : null;
});
const shouldMouseLeaveEvent = computed(() => {
  return !showSidebar && props.depth == 0 ? "mouseleave" : null;
});
const containerOffsetYConputed = computed(() => {
  return `${containerOffsetY.value}px`;
});
const miniLabelWidth = computed(() => {
  return expanded.value
    ? `calc(${menuItem.clientWidth}px + 250px - 1.5px)`
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
  const x = topContainerRef?.getBoundingClientRect();
  if (makeSpace.value) {
    topcontainerHeight.value = x.height + "px";
  } else {
    topcontainerHeight.value = x.height - (x.top + x.height) - 2 + "px";
  }
}
function setItemOffsetHeight() {
  if (props.depth == 0) {
    const x = menuItem.getBoundingClientRect();
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
  if (props.depth == 1 && !showSidebar) {
    props.setMaxHeightTopCProp();
  }
  if (!showSidebar && props.depth == 0) {
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
      props.item?.children.length * menuItem.offsetHeight + 3;
  }
  cacheHeight = null;
  if (!showSidebar && props.depth == 0) {
    containerHeight.value = "fit-content";
  }
  //add animation
  heightTimeout = setTimeout(() => {
    containerHeight.value = "fit-content";
  }, 200);
}
function closeItemChildren() {
  seTAnimationTimeOut.value = false;
  if (!showSidebar && props.depth == 0) {
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
    cacheHeight = container?.offsetHeight;
  }
  containerHeight.value = container?.offsetHeight;
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
    miniActive.value = false;
  } else {
    active.value = false;
    if (!props.item?.children) return;
    let hasFound = false;
    let x = extractChildrenRoutes(props.item?.children, "href") || [];
    for (var i = 0; i < x.length; i++) {
      if (isCurrentUrl(resloveHref(x[i]))) {
        hasFound = true;
        miniActive.value = true;
        if (!showSidebar) break;
        openItemCildren();
        break;
      }
    }
    miniActive.value = hasFound;
  }
}

watch(hover, (newHover) => {
  if (!id) {
    id = updateId();
  }
  if (newHover) {
    seTAnimationTimeOut.value = true;
    updateCurrantItemHover(id);
    openItemCildren();
    nextTick(() => {
      setTimeout(() => {
        setItemOffsetHeight();
      }, 0);
      const y = labelRef.getBoundingClientRect();
      labelMiniYYofsset.value = y.top;
    });
  } else {
    if (currantItemHover == id && menuHover) {
    } else {
      closeItemChildren();
    }
  }
});

onActivated(() => {
  checkActive();
});
</script>