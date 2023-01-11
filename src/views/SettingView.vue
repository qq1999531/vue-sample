<template>
  <div class="settingView sidebarExpanded white-theme">
    <Switch1
      :bindValue="BAndWTheme"
      :bindValueUpdate="updateTheme"
      :switchText="BAndWText"
    />
  </div>
</template>

<script setup>
import Switch1 from "@/components/Switches/Switch1.vue";
import { computed } from "@vue/runtime-core";
import { useStore } from "vuex";

const store = useStore();

const BAndWText = {
  onText: "bbblllaaaccckkk",
  offText: "white",
  onIcon: "",
  offIcon: "clear_night",
};

const BAndWTheme = computed(() => {
  return store.state.appTheme == "black-theme";
});

function updateTheme(BAndWTheme) {
  if (BAndWTheme) {
    store.dispatch("updateAppTheme", "black-theme");
  } else {
    store.dispatch("updateAppTheme", "white-theme");
  }
}
</script>

<style lang="scss">
.settingView {
  transition: 0.2s;
  height: 100%;
  &.sidebarExpanded {
    padding-left: 200px;
  }
  &.sidebarCollapsed {
    padding-left: 40px;
  }
}
</style>