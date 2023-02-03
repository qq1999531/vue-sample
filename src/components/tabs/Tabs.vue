<template>
  <div class="tabs-component">
    <ul class="tabs-component-tabs">
      <li
        v-for="(tab, i) in tabs"
        :key="i"
        :class="{ 'is-active': tab.isActive }"
        class="tabs-component-tab"
      >
        <a
          v-html="tab.header"
          @click="selectTab(tab.hash)"
          class="tabs-component-tab-a"
        ></a>
      </li>
    </ul>
    <div class="tabs-component-panels">
      <slot />
    </div>
  </div>
</template>

<script setup>
import { ref } from "@vue/reactivity";
import { onMounted } from "@vue/runtime-core";

const props = defineProps(["defaultTabHash", "childTabs"]);
const tabs = props.childTabs;
const activeTabHash = ref("");
const activeTabIndex = ref(0);
const lastActiveTabHash = ref("");

function findTab(hash) {
  return props.childTabs.find((tab) => tab.hash == hash);
}
function selectTab(selectedTabHash) {
  // See if we should store the hash in the url fragment.
  const selectedTab = findTab(selectedTabHash);
  if (!selectedTab) {
    return;
  }
  if (lastActiveTabHash.value == selectedTab.hash) {
    return;
  }
  props.childTabs.forEach((tab) => {
    tab.isActive = tab.hash == selectedTab.hash;
  });
  activeTabHash.value = selectedTab.hash;
  activeTabIndex.value = getTabIndex(selectedTabHash);
  lastActiveTabHash.value = activeTabHash.value = selectedTab.hash;
}
function getTabIndex(hash) {
  const tab = findTab(hash);
  return props.childTabs.indexOf(tab);
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