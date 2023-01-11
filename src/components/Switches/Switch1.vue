<template>
  <div class="switchContainer">
    <input type="checkbox" class="switchInput" />
    <span
      class="switchMain"
      @click="props.bindValueUpdate(!bindValue)"
      :class="{ checked: props.bindValue, [props.specialTheme]: true }"
    >
      <div
        class="switchContent"
        :style="{
          [!props.bindValue ? 'paddingLeft' : 'paddingRight']: '26px',
          [props.bindValue ? 'paddingLeft' : 'paddingRight']: '2px',
        }"
      >
        <span class="material-symbols-outlined switchIcon">{{
          showText.icon
        }}</span>
        <span class="switchText">{{ showText.text }}</span>
      </div>
      <div
        class="switchButton"
        :style="{ left: props.bindValue ? `calc(100% - 25px)` : '1px' }"
      ></div>
    </span>
  </div>
</template>

<script setup>
const { computed } = require("@vue/runtime-core");

const props = defineProps([
  "bindValue",
  "bindValueUpdate",
  "switchText",
  "specialTheme",
]); //switchText 结构   onText,offText,onIcon,offIcon
const showText = computed(() => {
  let sText = props.switchText.offText;
  let sIcon = props.switchText.offIcon;
  if (props.bindValue) {
    sText = props.switchText.onText;
    sIcon = props.switchText.onIcon;
  }
  return { text: sText, icon: sIcon };
});
</script>

<style lang="scss">
.switchContainer {
  display: inline-flex;
  height: 30px;
  position: relative;
  align-items: center;
  .switchInput {
    width: 0%;
    height: 0%;
    display: none;
  }
  .switchButton {
    border-radius: 100%;
    position: absolute;
    left: 1px;
    transition: all 0.4s;
    width: 24px;
    height: 24px;
    display: flex;
    justify-content: center;
    align-items: center;
    .white-theme & {
      background-color: #ffffff;
    }
    .black-theme & {
      background-color: #000000;
    }
  }
  .switchMain {
    display: inline-flex;
    position: relative;
    align-items: center;
    min-width: 40px;
    height: 28px;
    outline: none;
    border-radius: 14px;
    box-sizing: border-box;
    cursor: pointer;
    transition: border-color 0.2s, background-color 0.2s;
    .white-theme & {
      border: 1px solid #ff8080;
      background: #ff8080;
      color: #ffffff;
      &.BAndWSwitch {
        border: 1px solid #000000;
        background: #000000;
      }
    }
    .white-theme &.checked {
      border: 1px solid #8080ff;
      background: #8080ff;
      color: #ffffff;
    }
    .black-theme & {
      border: 1px solid #800000;
      background: #800000;
      color: #000000;
    }
    .black-theme &.checked {
      border: 1px solid #000080;
      background: #000080;
      color: #000000;
      &.BAndWSwitch {
        border: 1px solid #ffffff;
        background: #ffffff;
      }
    }
  }
  .switchContent {
    width: 100%;
    transition: all 0.2s;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    height: 25px;
  }
  .switchText {
    font-size: 16px;
    user-select: none;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
}
.switchIcon {
  vertical-align: middle;
  user-select: none;
}
</style>