<template>
  <svg>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2.5" result="coloredBlur" />
      <feMerge>
        <feMergeNode in="coloredBlur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="3" result="shadow" />
      <feOffset dx="1" dy="1" />
      <feMerge>
        <feMergeNode />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <!-- <circle :cx="100" :cy="50" :r="60" style="--clr:#7f7f7f;"></circle> -->
    <path
      id="arcHour"
      class="clockArc"
      stroke-width="3"
      stroke-linecap="round"
      filter="url(#glow)"
    />
    <circle id="hourDot" class="clockDot" r="3" filter="url(#glow)" />
    <!-- <circle :cx="100" :cy="50" :r="50" style="--clr:#7f7f7f;"></circle> -->
    <path
      id="arcMinute"
      class="clockArc"
      stroke-width="3"
      stroke-linecap="round"
      filter="url(#glow)"
    />
    <circle id="minuteDot" class="clockDot" r="3" filter="url(#glow)" />
    <!-- <circle :cx="100" :cy="50" :r="40" style="--clr:#7f7f7f;"></circle> -->
    <path
      id="arcSecond"
      class="clockArc"
      stroke-width="3"
      stroke-linecap="round"
      filter="url(#glow)"
    />
    <circle id="secondDot" class="clockDot" r="3" filter="url(#glow)" />
  </svg>
  <div class="clockTextContainer">
    <span class="clockText">
      <span class="hourText">
        <span class="digitText">
          <span class="showingText"></span>
          <span class="belowText"></span>
        </span>
        <span class="digitText">
          <span class="showingText"></span>
          <span class="belowText"></span>
        </span>
      </span>
      <span class="minuteText">
        <span class="digitText">
          <span class="showingText"></span>
          <span class="belowText"></span>
        </span>
        <span class="digitText">
          <span class="showingText"></span>
          <span class="belowText"></span>
        </span>
      </span>
      <span class="secondText">
        <span class="digitText">
          <span class="showingText"></span>
          <span class="belowText"></span>
        </span>
        <span class="digitText">
          <span class="showingText"></span>
          <span class="belowText"></span>
        </span>
      </span>
    </span>
  </div>
  <!-- <div style="font-size: 1px">{{ hour }}:{{ minute }}:{{ second }}</div> -->
</template>

<script setup>
import { onMounted, ref } from "@vue/runtime-core";
import $ from "jquery";

const hour = ref(0);
const minute = ref(0);
const second = ref(0);

function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
  var angleInRadians;
  angleInRadians = ((angleInDegrees - 90) * Math.PI) / 180.0;
  return {
    x: centerX + radius * Math.cos(angleInRadians),
    y: centerY + radius * Math.sin(angleInRadians),
  };
}

function describeArc(x, y, radius, startAngle, endAngle) {
  var arcSweep, end, start;
  start = polarToCartesian(x, y, radius, endAngle);
  end = polarToCartesian(x, y, radius, startAngle);
  arcSweep = endAngle - startAngle <= 180 ? "0" : "1";
  return [
    "M",
    start.x,
    start.y,
    "A",
    radius,
    radius,
    0,
    arcSweep,
    0,
    end.x,
    end.y,
  ].join(" ");
}

function initTime() {
  var currentDate = new Date();
  hour.value = currentDate.getHours();
  minute.value = currentDate.getMinutes();
  second.value = currentDate.getSeconds();
  //表盘时钟
  var secondArc = (second.value / 60) * 360;
  var hourArc = ((hour.value * 60 + minute.value) / (24 * 60)) * 360;
  var minArc = (minute.value / 60) * 360;
  $("#arcHour").attr("d", describeArc(100, 50, 60, 0, hourArc));
  $("#arcMinute").attr("d", describeArc(100, 50, 50, 0, minArc));
  $("#arcSecond").attr("d", describeArc(100, 50, 40, 0, secondArc));
  $("#hourDot").attr("d", describeArc(100, 50, 60, hourArc - 1, hourArc));
  $("#minuteDot").attr("d", describeArc(100, 50, 50, minArc - 1, minArc));
  $("#secondDot").attr("d", describeArc(100, 50, 40, secondArc - 1, secondArc));
  var dot = $("#hourDot");
  var pos = polarToCartesian(100, 50, 60, hourArc);
  dot.attr("cx", pos.x);
  dot.attr("cy", pos.y);
  dot = $("#minuteDot");
  pos = polarToCartesian(100, 50, 50, minArc);
  dot.attr("cx", pos.x);
  dot.attr("cy", pos.y);
  dot = $("#secondDot");
  pos = polarToCartesian(100, 50, 40, secondArc);
  dot.attr("cx", pos.x);
  dot.attr("cy", pos.y);
  //数字时钟
  var dateArray = [hour.value, minute.value, second.value];
  dateArray.forEach(function (number, i) {
    if (String(number).length == 1) {
      var output = "0" + String(number);
    } else {
      var output = String(number);
    }

    $(
      ".clockText > span:nth-child(" +
        (i + 1) +
        ") .digitText:nth-child(1) .showingText"
    ).html(output[0]);
    $(
      ".clockText > span:nth-child(" +
        (i + 1) +
        ") .digitText:nth-child(2) .showingText"
    ).html(output[1]);
  });
}
function setTime() {
  var currentDate = new Date();
  hour.value = currentDate.getHours();
  minute.value = currentDate.getMinutes();
  second.value = currentDate.getSeconds();
  //表盘时钟
  var secondArc = (second.value / 60) * 360;
  var hourArc = ((hour.value * 60 + minute.value) / (24 * 60)) * 360;
  var minArc = (minute.value / 60) * 360;
  $("#arcHour").attr("d", describeArc(100, 50, 60, 0, hourArc));
  $("#arcMinute").attr("d", describeArc(100, 50, 50, 0, minArc));
  $("#arcSecond").attr("d", describeArc(100, 50, 40, 0, secondArc));
  $("#hourDot").attr("d", describeArc(100, 50, 60, hourArc - 1, hourArc));
  $("#minuteDot").attr("d", describeArc(100, 50, 50, minArc - 1, minArc));
  $("#secondDot").attr("d", describeArc(100, 50, 40, secondArc - 1, secondArc));
  var dot = $("#hourDot");
  var pos = polarToCartesian(100, 50, 60, hourArc);
  dot.attr("cx", pos.x);
  dot.attr("cy", pos.y);
  dot = $("#minuteDot");
  pos = polarToCartesian(100, 50, 50, minArc);
  dot.attr("cx", pos.x);
  dot.attr("cy", pos.y);
  dot = $("#secondDot");
  pos = polarToCartesian(100, 50, 40, secondArc);
  dot.attr("cx", pos.x);
  dot.attr("cy", pos.y);
  //数字时钟
  var dateArray = [hour.value, minute.value, second.value];
  dateArray.forEach(function (number, i) {
    if (String(number).length == 1) {
      var output = "0" + String(number);
    } else {
      var output = String(number);
    }

    var digitOne = $(
      ".clockText > span:nth-child(" +
        (i + 1) +
        ") .digitText:nth-child(1) .showingText"
    ).html();
    if (digitOne != output[0]) {
      $(
        ".clockText > span:nth-child(" +
          (i + 1) +
          ") .digitText:nth-child(1) .belowText"
      ).html(output[0]);
      $(
        ".clockText > span:nth-child(" +
          (i + 1) +
          ") .digitText:nth-child(1) .showingText"
      )
        .removeClass("showingText")
        .addClass("aboveText");

      setTimeout(function () {
        $(
          ".clockText > span:nth-child(" +
            (i + 1) +
            ") .digitText:nth-child(1) .belowText"
        )
          .removeClass("belowText")
          .addClass("showingText");
      }, 400);

      setTimeout(function () {
        $(
          ".clockText > span:nth-child(" +
            (i + 1) +
            ") .digitText:nth-child(1) .aboveText"
        )
          .removeClass("aboveText")
          .addClass("belowText");
      }, 600);
    }

    var digitTwo = $(
      ".clockText > span:nth-child(" +
        (i + 1) +
        ") .digitText:nth-child(2) .showingText"
    ).html();
    if (digitTwo != output[1]) {
      $(
        ".clockText > span:nth-child(" +
          (i + 1) +
          ") .digitText:nth-child(2) .belowText"
      ).html(output[1]);
      $(
        ".clockText > span:nth-child(" +
          (i + 1) +
          ") .digitText:nth-child(2) .showingText"
      )
        .removeClass("showingText")
        .addClass("aboveText");

      setTimeout(function () {
        $(
          ".clockText > span:nth-child(" +
            (i + 1) +
            ") .digitText:nth-child(2) .belowText"
        )
          .removeClass("belowText")
          .addClass("showingText");
      }, 400);

      setTimeout(function () {
        $(
          ".clockText > span:nth-child(" +
            (i + 1) +
            ") .digitText:nth-child(2) .aboveText"
        )
          .removeClass("aboveText")
          .addClass("belowText");
      }, 600);
    }
  });
}

onMounted(() => {
  initTime();
  setInterval(() => {
    setTime();
  }, 1000);
});
</script>

<style lang="scss">
.clockTextContainer {
  position: absolute;
  top: 46px;
  left: 61px;
  align-items: center;
  opacity: 0.5;
  user-select: none;
}
.clockText {
  color: #ffffff;
  font-size: 1px;
}
.hourText,
.minuteText {
  &:after {
    content: " ";
    color: #000000;
  }
}
.digitText {
  display: inline-block;
  position: relative;
  margin: 5px;
}
.showingText,
.belowText,
.aboveText {
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  background-color: #000000;
  border: 2px solid #000000;
  border-radius: 15px;
}
.showingText {
  transform: perspective(100vh) rotateX(0) translateY(0%);
  transform-origin: 50% 100%;
  transition: transform 200ms cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.belowText {
  transform: perspective(100vh) rotateX(-90deg) translateY(140%);
  transition: transform 0s;
}
.aboveText {
  transform: perspective(100vh) rotateX(90deg) translateY(-140%);
  transform-origin: 50% 0%;
  transition: transform 200ms cubic-bezier(0.6, -0.28, 0.735, 0.045);
}
.clockArc {
  fill: none;
  stroke: #000000;
  transform: translate(0px, 15px);
}
.clockDot {
  fill: lighten(#ffffff, 50%);
  opacity: 0.5;
  transform: translate(0px, 15px);
}
</style>