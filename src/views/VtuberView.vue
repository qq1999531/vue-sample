<template>
  <div>vtuber</div>
  <button @click="test">test</button>
  <div class="vtuberView">
    <div class="livesContainer">
      <template v-for="(item, index) in liveData" :key="item.videoKey"
        ><div class="liveContainer" v-if="item.videoKey">
          <div class="rank">
            <img
              :src="
                channelData[item.channelKey]
                  ? channelData[item.channelKey].avatar_url
                  : 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'
              "
              class="channelAvatar"
              alt="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png"
            />
            <span>{{ parseInt(index) + 1 }}</span>
          </div>
          <div class="channelInfo">
            <span class="channelName">
              {{
                channelData[item.channelKey]
                  ? channelData[item.channelKey].channelName
                  : "anonymous"
              }}
            </span>
            <div
              class="brand"
              :style="{
                background: brandcolor(item.channelKey),
              }"
            >
              <img :src="brandAvatar(item.channelKey)" /><span>{{
                channelData[item.channelKey]
                  ? channelData[item.channelKey].group
                  : "anonymous"
              }}</span>
            </div>
          </div>
          <div class="liveInfo">
            <div class="liveCover">
              <img
                :src="
                  'https://i.ytimg.com/vi/' +
                  item.videoKey +
                  '/hqdefault_live.jpg'
                "
              />
            </div>
            <div class="rightInfo"></div>
          </div></div
      ></template>
    </div>
  </div>
</template>

<script setup>
const { ref } = require("@vue/reactivity");
const { onMounted } = require("@vue/runtime-core");
const brandData = require("@/data/youtubeChannels/brands.json");
const channelData = require("@/data/youtubeChannels/channels.json");

const liveData = ref([]);
import("@/data/youtubeChannels/realtime.json").then((data) => {
  liveData.value = data;
});

function test() {
  for (var i = 0; i < liveData.value.length; i++) {
    console.log(liveData.value[i]);
    console.log(channelData[liveData.value[i].channelKey]);
  }
  console.log(brandData);
}
function brandAvatar(channelKey) {
  if (channelData[channelKey]) {
    if (channelData[channelKey].group == "Independent") {
      return channelData[channelKey].avatar_url;
    }
    if (brandData[channelData[channelKey].group]) {
      return brandData[channelData[channelKey].group].avatar_url;
    }
    return brandData["Independent"].avatar_url;
  }
  return "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png";
}
function brandcolor(channelKey) {
  if (channelData[channelKey]) {
    if (channelData[channelKey].group == "Independent") {
      return channelData[channelKey].color;
    }
    if (brandData[channelData[channelKey].group]) {
      return brandData[channelData[channelKey].group].color;
    }
  }
  return brandData["Independent"].color;
}

onMounted(() => {
  setInterval(() => {
    import("@/data/youtubeChannels/realtime.json").then((data) => {
      liveData.value = data;
      console.log("get realtime successfully");
    });
  }, 1800000);
});
</script>

<style lang="scss">
.vtuberView {
  transition: 0.2s;
  align-items: center;
  display: flex;
  flex-flow: column;
  padding-top: 20px;
  padding-bottom: 20px;
}
.livesContainer {
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
.liveContainer {
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
.channelAvatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  user-select: none;
}
.rank {
  display: flex;
  flex-flow: column;
  span {
    background: #000000;
    color: #ffffff;
    font-weight: bold;
    border-radius: 6px;
    padding-top: 2px;
    padding-bottom: 2px;
    margin-top: 6px;
  }
}
.channelInfo {
  flex-flow: column;
  width: 30%;
  height: 100%;
  .channelName {
    align-items: center;
    justify-content: center;
    display: flex;
    font-weight: bold;
  }
  .brand {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    margin-top: 10px;
    color: #ffffff;
    padding: 2px;
    border-radius: 17px;
    img {
      width: 30px;
      height: 30px;
      border-radius: 50%;
      user-select: none;
      margin-right: 2px;
    }
  }
}
.liveInfo {
  .liveCover {
    img {
      object-fit: cover;
      border-radius: 6px;
      height: 150px;
      aspect-ratio: 16/9;
    }
  }
}
</style>>
