<template>
  <div class="selectMain" :class="{ focused: focused }" @click="focusSelect">
    <input
      class="selectFocus"
      ref="selectFocus"
      readonly
      @blur="focused = false"
      :style="{ width: maxLength + 'em' }"
      placeholder="test"
      :value="currentValue"
    />
    <div class="dropdownIcon" :class="{ rotateIcon: focused }">
      <i>
        <svg viewBox="0 0 1024 1024">
          <path
            d="M 831.872 340.864 L 512 652.672 L 192.128 340.864 a 30.592 30.592 0 0 0 -42.752 0 a 29.12 29.12 0 0 0 0 41.6 L 489.664 714.24 a 32 32 0 0 0 44.672 0 l 340.288 -331.712 a 29.12 29.12 0 0 0 0 -41.728 a 30.592 30.592 0 0 0 -42.752 0 Z"
          ></path>
        </svg>
      </i>
    </div>
  </div>
  <transition name="selectItemsSlide">
    <ul
      v-show="focused"
      class="selectItemsContainer"
      :style="{ width: `calc(${maxLength}em + 28px)` }"
    >
      <template v-for="(item, index) in props.items" :key="index">
        <li
          class="selectItem"
          :class="{ itemSelected: item.value == currentValue }"
          @click="updateValue(item.value)"
        >
          <span class="itemText">{{ item.value }}</span>
        </li>
      </template>
    </ul>
  </transition>
</template>

<script setup>
const { ref } = require("@vue/reactivity");
const { computed } = require("@vue/runtime-core");

const props = defineProps(["items", "bindValue"]);
const emit = defineEmits(["updateValue"]);

const maxLength = computed(() => {
  let temp = 0;
  for (const item of props.items) {
    temp = item.value.length > temp ? item.value.length : temp;
  }
  return temp;
});

const selectFocus = ref();
const focused = ref(false);
const currentValue = ref(props.bindValue);

function focusSelect() {
  if (!focused.value) {
    selectFocus.value.focus();
    focused.value = true;
  } else {
    selectFocus.value.blur();
    focused.value = false;
  }
}

function updateValue(val) {
  currentValue.value = val;
  emit("updateValue", val);
}
</script>


<style lang="scss">
.selectMain {
  cursor: pointer;
  height: 28px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  transition: 0.2s;
  .white-theme & {
    border: 1px solid #000000;
  }
  .black-theme & {
    border: 1px solid #ffffff;
  }
  &.focused {
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    .white-theme & {
      box-shadow: 0px 0px 6px #000000;
    }
    .black-theme & {
      box-shadow: 0px 0px 6px #ffffff;
    }
  }
}
.dropdownIcon {
  height: 1em;
  width: 1em;
  margin-right: 6px;
  transition: 0.4s;
  &.rotateIcon {
    transform: rotate(-180deg);
  }
  svg {
    height: 1em;
    width: 1em;
    path {
      .white-theme & {
        fill: #000000;
      }
      .black-theme & {
        fill: #ffffff;
      }
    }
  }
}
.selectFocus {
  cursor: pointer;
  border: none;
  outline: none;
  margin-left: 6px;
  height: 100%;
  transition: 0.2s;
  font-size: 16px;
  user-select: none;
  font-weight: bold;
  .black-theme & {
    background-color: #000000;
    color: #ffffff;
  }
}
.selectItemsContainer {
  max-height: 40vh;
  overflow-y: hidden;
  border-bottom-left-radius: 6px;
  border-bottom-right-radius: 6px;
  transform: translateY(-7px);
  list-style: none;
  .white-theme & {
    background-color: #ffffff;
    border-left: 1px solid #000000;
    border-right: 1px solid #000000;
    border-bottom: 1px solid #000000;
  }
  .black-theme & {
    background-color: #000000;
    border-left: 1px solid #ffffff;
    border-right: 1px solid #ffffff;
    border-bottom: 1px solid #ffffff;
  }
}
.selectItemsSlide-enter-from,
.selectItemsSlide-leave-to {
  max-height: 6px;
}
.selectItemsSlide-enter-active,
.selectItemsSlide-leave-active {
  transition: all 0.4s ease;
}
.selectItemsContainer {
  position: absolute;
}
.selectItem {
  height: 30px;
  display: flex;
  cursor: pointer;
  color: #808080;
  transition: 0.2s;
  &:first-child {
    padding-top: 7px;
  }
  &.itemSelected {
    .white-theme & {
      color: #000000;
    }
    .black-theme & {
      color: #ffffff;
    }
    font-weight: bold;
  }
}
.itemText {
  padding-left: 6px;
  font-size: 16px;
  line-height: 30px;
  user-select: none;
}
</style>