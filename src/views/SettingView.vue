<template>
  <div class="settingView">
    <div class="settingsContainer">
      <div class="settingContainer">
        <div class="settingDesc">明暗模式</div>
        <div style="padding-right: 12px">
          <Switch1
            :bindValue="BAndWTheme"
            :switchText="BAndWText"
            :specialTheme="'BAndWSwitch'"
            @updateValue="updateTheme"
          />
        </div>
      </div>
      <div class="settingContainer">
        <div class="settingDesc">时钟样式</div>
        <div style="padding-right: 12px">
          <Select1
            :bindValue="store.state.clockStyle"
            :items="clockStyleItems"
            @updateValue="updateClockStyle"
          />
        </div>
      </div>
      <div class="settingContainer">
        <div class="settingDesc">test1</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Switch1 from "@/components/switches/Switch1.vue";
import Select1 from "@/components/select/Select1.vue";
import { computed } from "@vue/runtime-core";
import { useStore } from "vuex";

const store = useStore();

const BAndWText = {
  onText: "",
  offText: "",
  onIcon: "",
  offIcon: "",
};
const clockStyleItems = [{ value: "Clock1" }, { value: "Clock2" }];

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
function updateClockStyle(newStyle) {
  store.dispatch("updateClockStyle", newStyle);
}
</script>

<style lang="scss">
.settingView {
  transition: 0.2s;
  align-items: center;
  display: flex;
  flex-flow: column;
  padding-top: 20px;
  padding-bottom: 20px;
}
.settingsContainer {
  display: flex;
  width: 96%;
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
  width: 96%;
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