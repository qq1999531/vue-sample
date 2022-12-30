<template>
  <div ref="menuItem" class="menu-item-base alignCenter">
    <!--<div v-if="active" class="BlockBack"></div> -->
    <!-- ========================= -->
    <!-- ========================= -->
    <!-- 1 this is the menu label  -->
    <!-- ========================= -->
    <!-- ========================= -->

    <div class="label TransBG">
      <div
        class="left"
        ref="labelRef"
        :class="{ marginAuto: miniMenu && depth === 0, collapseEnd: miniMenu }"
      >
        <template
          v-if="!removeIconSpace || (removeIconSpace && siblingsHaveIconProp)"
        >
          <MenuItemIconVue :icon="item?.icon" />
        </template>
        <span class="labelName">{{ labelName }}</span>
      </div>
      <template v-if="(miniMenu && depth != 0) || !miniMenu">
        <div
          v-if="item.children && !itemApendIcon"
          class="icons postIconOpenAnima"
          :class="{ opened: showChildren }"
        ></div>
      </template>
    </div>

    <!-- ========================= -->
    <!-- ========================= -->
    <!--2 this container is for when menu Children when full width -->
    <!-- ========================= -->
    <!-- ========================= -->
    <div v-if="!miniMenu || (depth != 0 && miniMenu)">
      <div
        class="items-container"
        :style="{ maxHeight: heifOfContainer, transition: transitionTime }"
        ref="container"
        v-if="item.children"
      >
        <template v-if="renderChildren">
          <SidebarItem
            v-for="(item, index) in item.children"
            :siblingsHaveIconProp="siblingsHaveIcon"
            :isParentFlat="siblingsHaveIconProp"
            :key="index"
            :item="item"
            :depth="depth + 1"
          />
        </template>
      </div>
    </div>

    <!-- ========================= -->
    <!-- ========================= -->
    <!--3  this container is for mini Menu Children -->
    <!-- ========================= -->
    <!-- ========================= -->

    <div
      v-if="miniMenu && depth === 0 && !collapsed"
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
          left: menuType === 'fully' ? '0px' : miniLabelDirection,
          width: miniLabelWidth,
          [MakeSpace ? 'bottom' : 'top']: ContainerOffsetYConputed,
          opacity: depth === 0 && showChildren ? '1' : '0',
        }"
      >
        <!--main menu btn-->
        <div
          v-if="showChildren"
          class="left"
          :class="{ marginAuto: miniMenu && depth === 0 }"
          :style="{
            left: widthMiniMenu,
            top: labelMiniYYofsset + 'px',
          }"
        >
          <span v-if="!menuItemLabel" class="labelName">{{ item?.name }}</span>
          <component
            v-else
            :labelName="item?.name"
            :active="active"
            :miniActive="miniActive"
            :isChildrenMenuOpen="showChildren"
            :is="menuItemLabel"
          />
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
            :siblingsHaveIconProp="siblingsHaveIcon"
            :isParentFlat="siblingsHaveIconProp"
            :key="index"
            :item="item"
            :depth="depth + 1"
            :setMaxHeightTopCProp="setMaxHeightTopC"
            :isMakeSpace="MakeSpace"
          />
        </template>
      </div>
      <div class="labelminiSub" v-if="depth == 0 && MakeSpace"></div>
    </div>
  </div>
</template>

<script setup>
    import SidebarItem from "@/components/SidebarItem.vue";
</script>