<template>
  <div class="liveContainer" v-if="props.item.videoKey">
    <div class="rank">
      <div class="avatarContainer">
        <img
          v-if="avatarState"
          @error="avatarState = false"
          :src="
            props.channelData
              ? props.channelData.avatar_url
              : 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'
          "
          class="channelAvatar"
          alt="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png"
        />
        <i v-if="!avatarState"
          ><svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg">
            <path
              fill="currentColor"
              d="M160 160v704h704V160H160zm-32-64h768a32 32 0 0 1 32 32v768a32 32 0 0 1-32 32H128a32 32 0 0 1-32-32V128a32 32 0 0 1 32-32z"
            ></path>
            <path
              fill="currentColor"
              d="M384 288q64 0 64 64t-64 64q-64 0-64-64t64-64zM185.408 876.992l-50.816-38.912L350.72 556.032a96 96 0 0 1 134.592-17.856l1.856 1.472 122.88 99.136a32 32 0 0 0 44.992-4.864l216-269.888 49.92 39.936-215.808 269.824-.256.32a96 96 0 0 1-135.04 14.464l-122.88-99.072-.64-.512a32 32 0 0 0-44.8 5.952L185.408 876.992z"
            ></path></svg
        ></i>
      </div>
      <span>{{ parseInt(props.index) + 1 }}</span>
    </div>
    <div class="channelInfo">
      <span class="channelName">
        {{ props.channelData ? props.channelData.channelName : "anonymous" }}
      </span>
      <div
        class="brand"
        :style="{
          background: props.brandColor,
        }"
      >
        <div class="brandAvatarContainer">
          <img
            v-if="brandAvatarState"
            :src="props.brandAvatar"
            @error="brandAvatarState = false"
          />
          <i v-if="!brandAvatarState"
            ><svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg">
              <path
                fill="currentColor"
                d="M160 160v704h704V160H160zm-32-64h768a32 32 0 0 1 32 32v768a32 32 0 0 1-32 32H128a32 32 0 0 1-32-32V128a32 32 0 0 1 32-32z"
              ></path>
              <path
                fill="currentColor"
                d="M384 288q64 0 64 64t-64 64q-64 0-64-64t64-64zM185.408 876.992l-50.816-38.912L350.72 556.032a96 96 0 0 1 134.592-17.856l1.856 1.472 122.88 99.136a32 32 0 0 0 44.992-4.864l216-269.888 49.92 39.936-215.808 269.824-.256.32a96 96 0 0 1-135.04 14.464l-122.88-99.072-.64-.512a32 32 0 0 0-44.8 5.952L185.408 876.992z"
              ></path></svg
          ></i>
        </div>
        <span>{{
          props.channelData ? props.channelData.group : "anonymous"
        }}</span>
      </div>
    </div>
    <div class="liveInfo">
      <div class="liveTitle">
        <span class="loopText">{{ props.item.videoName }}</span
        ><span class="loopText">{{ props.item.videoName }}</span
        ><span class="loopText">{{ props.item.videoName }}</span
        ><span class="loopText">{{ props.item.videoName }}</span>
      </div>
      <div class="liveInfoDetail">
        <div class="liveCover">
          <img
            v-if="liveCoverState"
            @error="liveCoverState = false"
            :src="
              'https://i.ytimg.com/vi/' +
              props.item.videoKey +
              '/hqdefault_live.jpg'
            "
          />
          <i v-if="!liveCoverState"
            ><svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg">
              <path
                fill="currentColor"
                d="M160 160v704h704V160H160zm-32-64h768a32 32 0 0 1 32 32v768a32 32 0 0 1-32 32H128a32 32 0 0 1-32-32V128a32 32 0 0 1 32-32z"
              ></path>
              <path
                fill="currentColor"
                d="M384 288q64 0 64 64t-64 64q-64 0-64-64t64-64zM185.408 876.992l-50.816-38.912L350.72 556.032a96 96 0 0 1 134.592-17.856l1.856 1.472 122.88 99.136a32 32 0 0 0 44.992-4.864l216-269.888 49.92 39.936-215.808 269.824-.256.32a96 96 0 0 1-135.04 14.464l-122.88-99.072-.64-.512a32 32 0 0 0-44.8 5.952L185.408 876.992z"
              ></path></svg
          ></i>
        </div>
        <div class="rightInfo">
          <div class="liveCountGroup">
            <div>
              <span>live viewer count:</span
              ><span>{{ props.item.liveViewerCount }}</span>
            </div>
            <div>
              <div>
                <span>avg live viewer count:</span
                ><span>{{ props.item.avgLiveViewerCount }}</span>
              </div>
              <div>
                <span>max live viewer count:</span
                ><span>{{ props.item.maxLiveViewerCount }}</span>
              </div>
            </div>
          </div>
          <div>
            <span>start date:</span> <span>{{ props.item.startDate }}</span>
          </div>
          <div>
            <span>lasting time:</span> <span>{{ props.item.lastingTime }}</span>
          </div>
          <div>
            <span>play count:</span> <span>{{ props.item.playCount }}</span>
          </div>
          <div>
            <span>like count:</span> <span>{{ props.item.likeCount }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const { ref } = require("@vue/reactivity");

const props = defineProps([
  "item",
  "index",
  "channelData",
  "brandColor",
  "brandAvatar",
]);

const avatarState = ref(true);
const brandAvatarState = ref(true);
const liveCoverState = ref(true);
</script>