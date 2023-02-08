<template>
  <div class="tabs-component">
    <ul class="tabs-component-tabs">
      <li
        v-for="(tab, i) in props.childTabs"
        :key="i"
        :class="{ 'is-active': tab.hash == activeTabHash }"
        class="tabs-component-tab"
      >
        <a
          v-html="tab.header"
          @click="selectTab(tab.hash)"
          class="tabs-component-tab-a"
          :href="'#' + tab.hash"
        ></a>
      </li>
    </ul>
    <div class="tabs-component-panels">
      <div
        v-for="tab in props.childTabs"
        :key="tab.hash"
        v-show="tab.hash == activeTabHash"
        class="tabs-component-panel"
        :id="tab.hash"
      >
        <slot :name="tab.hash" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "@vue/reactivity";
import { onMounted } from "@vue/runtime-core";

const props = defineProps(["defaultTabHash", "childTabs"]);
const activeTabHash = ref("");

function findTab(hash) {
  return props.childTabs.find((tab) => tab.hash == hash);
}
function selectTab(selectedTabHash) {
  // See if we should store the hash in the url fragment.
  const selectedTab = findTab(selectedTabHash);
  if (!selectedTab) {
    return;
  }
  activeTabHash.value = selectedTab.hash;
}

onMounted(() => {
  window.addEventListener("hashchange", () => selectTab(window.location.hash));
  if (findTab(window.location.hash)) {
    selectTab(window.location.hash);
    return;
  }
  if (props.defaultTabHash !== null && findTab("#" + props.defaultTabHash)) {
    selectTab("#" + props.defaultTabHash);
    return;
  }
  if (props.childTabs.length) {
    selectTab(props.childTabs[0].hash);
  }
});
</script>

<style lang="scss">
.tabs-component {
  width: 96%;
  .tabs-component-tabs {
    list-style-type: none;
    align-items: stretch;
    display: flex;
    justify-content: flex-start;
    .tabs-component-tab {
      background: #fff;
      transition: transform 0.3s ease;
      border-top: solid 1px #000;
      z-index: 999;
      &:first-child {
        border-top-left-radius: 4px;
        border-left: solid 1px #000;
      }
      &:last-child {
        border-top-right-radius: 4px;
        border-right: solid 1px #000;
      }
      .tabs-component-tab-a {
        align-items: center;
        color: inherit;
        display: flex;
        padding: 6px 16px;
        text-decoration: none;
      }
    }
  }
}
.tabs-component-panels {
  border-top-left-radius: 0;
  background-color: #fff;
  border: solid 1px #000;
  border-radius: 0 4px 4px 4px;
  transform: translateY(-1px);
  z-index: 1000;
  .tabs-component-panel {
    align-items: center;
    display: flex;
    flex-flow: column;
  }
}
</style>