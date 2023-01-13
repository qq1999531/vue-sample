<template>
  <div class="selectMain" @click="focusSelect">
    <input class="selectFocus" ref="selectFocus" readonly />
    <span class="dropdownIcon">
      <i>
        <svg viewBox="0 0 1024 1024">
          <path
            fill="#000000"
            d="M 831.872 340.864 L 512 652.672 L 192.128 340.864 a 30.592 30.592 0 0 0 -42.752 0 a 29.12 29.12 0 0 0 0 41.6 L 489.664 714.24 a 32 32 0 0 0 44.672 0 l 340.288 -331.712 a 29.12 29.12 0 0 0 0 -41.728 a 30.592 30.592 0 0 0 -42.752 0 Z"
          ></path>
        </svg>
      </i>
    </span>
  </div>
  <div class="selectItemsContainer">
    <template> </template>
  </div>
</template>

<script setup>
const { ref } = require("@vue/reactivity");

const selectFocus = ref();

function focusSelect(e) {
  console.log(selectFocus.value);
  selectFocus.value.focus();
  console.log(document.activeElement);
}
</script>


<style lang="scss">
.selectMain {
  height: 30px;
  border: 1px solid #000000;
  border-radius: 6px;
  display: flex;
  align-items: center;
  &:focus {
    box-shadow: 0 0 0 #000000;
    background: #000000;
  }
}
.dropdownIcon {
  height: 1em;
  width: 1em;
  margin-right: 6px;
  svg {
    height: 1em;
    width: 1em;
  }
}
.selectFocus {
  cursor: pointer;
  border: none;
  outline: none;
  margin-left: 6px;
  height: 100%;
}
</style>