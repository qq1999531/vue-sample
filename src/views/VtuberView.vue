<template>
  <div>vtuber</div>
  <button @click="test">test</button>
  <div class="vtuberView">
    <div class="chartContainer">
      <MultiLevelPie :data="pieChartData" :width="pieChartWidth" />
    </div>
    <div class="livesContainer">
      <VtuberLiveEntry
        v-for="(item, index) in liveData"
        :key="item.videoKey"
        :item="item"
        :index="index"
        :channelData="channelData[item.channelKey]"
        :brandColor="brandColor(item.channelKey)"
        :brandAvatar="brandAvatar(item.channelKey)"
      />
    </div>
  </div>
</template>

<script setup>
import VtuberLiveEntry from "@/components/entries/VtuberLiveEntry.vue";
import MultiLevelPie from "@/components/charts/Multi-Level_Pie.vue";
const { ref } = require("@vue/reactivity");
const { onMounted } = require("@vue/runtime-core");
const brandData = require("@/data/youtubeChannels/brands.json");
const channelData = require("@/data/youtubeChannels/channels.json");

const liveData = ref([]);
liveData.value = require("@/data/youtubeChannels/realtime.json");
console.log(liveData.value);
let pieChartData = {
  name: "live",
  children: [
    {
      name: "hololive",
      children: [
        { name: "hololive", value: 10000 },
        { name: "fubuki", value: 2000 },
      ],
    },
    {
      name: "nijisanji",
      children: [
        { name: "nijisanji", value: 8000 },
        { name: "mito", value: 5000 },
      ],
    },
  ],
};
multiPieChartData(liveData.value);
console.log(pieChartData);
const pieChartWidth = ref(360);

function test() {
  multiPieChartData();
  console.log(pieChartData);
  console.log(liveData.value);
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
function brandColor(channelKey) {
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
function multiPieChartData(liveData) {
  let tempChildren = [];
  let isExist = false;
  for (var i = 0; i < liveData.length; i++) {
    let tempChild = {};
    let tempBrand = {};
    tempChild["name"] = channelData[liveData[i].channelKey]
      ? channelData[liveData[i].channelKey].channelName
      : "anonymous";
    tempChild["color"] = channelData[liveData[i].channelKey]
      ? channelData[liveData[i].channelKey].color
      : "#000000";
    tempChild["value"] = liveData[i].liveViewerCount;
    for (var j = 0; j < tempChildren.length; j++) {
      if (
        tempChildren[j]["name"] ==
        (channelData[liveData[i].channelKey]
          ? channelData[liveData[i].channelKey].group
          : "Independent")
      ) {
        tempChildren[j]["children"].push(tempChild);
        isExist = true;
        break;
      } else {
        isExist = false;
      }
    }
    if (!isExist) {
      tempBrand["name"] = channelData[liveData[i].channelKey]
        ? channelData[liveData[i].channelKey].group
        : "Independent";
      tempBrand["color"] = brandData[channelData[liveData[i].channelKey].group]
        ? brandData[channelData[liveData[i].channelKey].group].color
        : brandData["Independent"].color;
      tempBrand["children"] = [];
      tempChildren.push(tempBrand);
      tempChildren[tempChildren.length - 1]["children"].push(tempChild);
      console.log(tempChild);
    }
  }
  pieChartData.children = tempChildren;
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
.chartContainer,
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
.rank {
  display: flex;
  flex-flow: column;
  .avatarContainer {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    display: flex;
    flex-flow: column;
    align-items: center;
    justify-content: center;
    background: rgb(0, 0, 0, 0.5);
    .channelAvatar {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      user-select: none;
    }
    svg {
      width: 40px;
      height: 40px;
    }
  }
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
    border-radius: 16px;
    .brandAvatarContainer {
      width: 30px;
      height: 30px;
      border-radius: 50%;
      display: flex;
      flex-flow: column;
      align-items: center;
      justify-content: center;
      background: rgb(0, 0, 0, 0.5);
      img {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        user-select: none;
        margin-right: 2px;
      }
      svg {
        width: 10px;
        height: 10px;
      }
    }
  }
}
.liveInfo {
  width: calc(70% - 80px);
  .liveInfoDetail {
    display: flex;
  }
  .rightInfo {
    display: flex;
    flex-flow: column;
    padding-left: 20px;
    text-align: start;
    width: calc(100% - 320px);
    > div {
      height: 100%;
    }
    > div:nth-child(n + 2) {
      display: flex;
      span:nth-child(1) {
        width: 30%;
      }
    }
    span:nth-child(2) {
      font-weight: bold;
    }
    .liveCountGroup {
      display: flex;
      flex-flow: column;
      padding-top: 10px;
      padding-bottom: 10px;
      > div:nth-child(1) {
        text-align: center;
        font-size: 24px;
        line-height: 36px;
      }
      > div:nth-child(2) {
        display: flex;
        div {
          width: 50%;
        }
      }
    }
  }
  .liveCover {
    height: 180px;
    width: 320px;
    border-radius: 6px;
    display: flex;
    flex-flow: column;
    align-items: center;
    justify-content: center;
    background: rgb(0, 0, 0, 0.5);
    img {
      object-fit: cover;
      border-radius: 6px;
      height: 180px;
      aspect-ratio: 16/9;
    }
    svg {
      width: 90px;
      height: 90px;
    }
  }
  .liveTitle {
    display: flex;
    text-align: start;
    white-space: nowrap;
    overflow: hidden;
    line-height: 2em;
    height: 2em;
    .loopText {
      animation: textLoop 10s linear infinite;
    }
  }
}
@keyframes textLoop {
  0% {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }
  100% {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
  }
}
</style>>
