<template>
  <div class="settingView sidebarExpanded white-theme">
    <div class="settingsContainer">
      <div class="settingContainer">
        <div class="settingDesc">明暗模式</div>
        <div style="padding-right: 12px">
          <Switch1
            :bindValue="BAndWTheme"
            :bindValueUpdate="updateTheme"
            :switchText="BAndWText"
            :specialTheme="'BAndWSwitch'"
          />
        </div>
      </div>
      <div class="settingContainer">
        <div class="settingDesc">test1</div>
      </div>
      <div class="settingContainer">
        <div class="settingDesc">test1</div>
      </div>
      <div class="settingContainer">
        <div class="settingDesc">test1</div>
      </div>
      <div class="settingContainer">
        <div class="settingDesc">test1</div>
      </div>
      <div class="settingContainer">
        <div class="settingDesc">test1</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Switch1 from "@/components/Switches/Switch1.vue";
import { computed } from "@vue/runtime-core";
import { useStore } from "vuex";

const store = useStore();

const BAndWText = {
  onText: "",
  offText: "",
  onIcon: "clear_day",
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
  align-items: center;
  display: flex;
  flex-flow: column;
  &.sidebarExpanded {
    padding-left: 200px;
  }
  &.sidebarCollapsed {
    padding-left: 40px;
  }
}
.settingsContainer {
  display: flex;
  width: 80%;
  border-radius: 10px;
  flex-flow: column;
  align-items: center;
  .white-theme & {
    box-shadow: 0px 0px 4px 0px #000000;
  }
  .black-theme & {
    box-shadow: 0px 0px 4px 0px #ffffff;
  }
}
.settingContainer {
  display: flex;
  width: 100%;
  padding-block-start: 6px;
  padding-block-end: 6px;
  align-items: center;
  &:nth-child(n + 2) {
    .white-theme & {
      border-top: 1px solid rgb(0, 0, 0, 0.5);
    }
    .black-theme & {
      border-top: 1px solid rgb(255, 255, 255, 0.5);
    }
  }
}
.settingDesc {
  width: 100%;
  display: flex;
  padding-left: 12px;
}
</style>