<template>
  <!-- main codes start -->
  <div class="signboard outer">
    <div class="signboard front inner anim04c">
      <span class="year anim04c">{{ year }}</span>
      <div class="calendarMain anim04c">
        <span class="month anim04c">{{ month }}</span>
        <span class="date anim04c">{{ date }}</span>
        <span class="day anim04c">{{ day }}</span>
      </div>
      <span class="clock minute anim04c">{{ minute }}</span>
      <span class="calendarNormal date2 anim04c">{{ date }}</span>
    </div>
    <div class="signboard left inner anim04c">
      <span class="clock hour anim04c">{{ hour }}</span>
      <span class="calendarNormal day2 anim04c">{{ day }}</span>
    </div>
    <div class="signboard right inner anim04c">
      <span class="clock second anim04c">{{ second }}</span>
      <span class="calendarNormal month2 anim04c">{{ month }}</span>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "@vue/runtime-core";

const monthNames = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];
const dayNames = [
  "Sunday",
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
];
const hour = ref("");
const second = ref("");
const minute = ref("");
const month = ref("");
const date = ref("");
const day = ref("");
const year = ref("");

function updateTime() {
  var currentDate = new Date();
  var hours = currentDate.getHours();
  hour.value = (hours < 10 ? "0" : "") + hours;
  var seconds = currentDate.getSeconds();
  second.value = (seconds < 10 ? "0" : "") + seconds;
  var minutes = currentDate.getMinutes();
  minute.value = (minutes < 10 ? "0" : "") + minutes;
  month.value = monthNames[currentDate.getMonth()];
  date.value = currentDate.getDate();
  day.value = dayNames[currentDate.getDay()];
  year.value = currentDate.getFullYear();
}

onMounted(() => {
  updateTime();
  setInterval(() => {
    updateTime();
  }, 1000);
});
</script>

<style lang="scss">
/* -- usable codes start -- */
.anim04c {
  -webkit-transition: all 0.4s cubic-bezier(0.5, 0.35, 0.15, 1.4);
  transition: all 0.4s cubic-bezier(0.5, 0.35, 0.15, 1.4);
}
/*-----*/

.outer {
  position: relative;
  top: 50%;
  z-index: 1;
  -webkit-transform: translateY(-50%);
  -moz-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  -o-transform: translateY(-50%);
  transform: translateY(-50%);
  cursor: pointer;
}
/*-----*/

.signboard {
  width: 100px;
  height: 100px;
  margin: auto;
  border-radius: 10px;
  display: flex;
  user-select: none;
  .white-theme & {
    color: #ffffff;
  }
  .black-theme & {
    color: #000000;
  }
  .outer:active & {
    width: 70px;
    height: 70px;
  }
}
/*-----*/

.front {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 3;
  text-align: center;

  .white-theme & {
    color: #ffffff;
    background: #000000;
  }
  .black-theme & {
    color: #000000;
    background: #ffffff;
  }
}
.outer .right {
  position: absolute;
  right: 0;
  z-index: 2;

  .white-theme & {
    color: #ffffff;
    background: #000000;
  }
  .black-theme & {
    color: #000000;
    background: #ffffff;
  }
}
.outer .left {
  position: absolute;
  left: 0;
  z-index: 1;

  .white-theme & {
    color: #ffffff;
    background: #000000;
  }
  .black-theme & {
    color: #000000;
    background: #ffffff;
  }
}
/*-----*/

.outer:active .inner {
  -webkit-transform: rotate(0) translate(0) scale(0.9);
  -moz-transform: rotate(0) translate(0) scale(0.9);
  -ms-transform: rotate(0) translate(0) scale(0.9);
  -o-transform: rotate(0) translate(0) scale(0.9);
  transform: rotate(0) translate(0) scale(0.9);
}
.outer:active .front .date {
  transform: scale(2);
}
.outer:active .front .day,
.outer:active .front .month {
  visibility: hidden;
  opacity: 0;
  -webkit-transform: scale(0);
  -moz-transform: scale(0);
  -ms-transform: scale(0);
  -o-transform: scale(0);
  transform: scale(0);
}
.outer:active .right {
  -webkit-transform: translateX(50px) scale(0.9);
  -moz-transform: translateX(50px) scale(0.9);
  -ms-transform: translateX(50px) scale(0.9);
  -o-transform: translateX(50px) scale(0.9);
  transform: translateX(50px) scale(0.9);
}
.outer:active .left {
  -webkit-transform: translateX(-50px) scale(0.9);
  -moz-transform: translateX(-50px) scale(0.9);
  -ms-transform: translateX(-50px) scale(0.9);
  -o-transform: translateX(-50px) scale(0.9);
  transform: translateX(-50px) scale(0.9);
}
.outer:active .front {
  -webkit-transform: translateX(15px) scale(0.9);
  -moz-transform: translateX(15px) scale(0.9);
  -ms-transform: translateX(15px) scale(0.9);
  -o-transform: translateX(15px) scale(0.9);
  transform: translateX(15px) scale(0.9);
}
/*-----*/

.outer:active .calendarMain {
  transform: scale(1.8);
  opacity: 0;
  visibility: hidden;
}
.outer:active .clock {
  transform: scale(1.4);
  opacity: 1;
  visibility: visible;
}
.outer:active .calendarNormal {
  bottom: -30px;
  opacity: 1;
  visibility: visible;
}
.outer:active .year {
  top: -30px;
  opacity: 1;
  visibility: visible;
  letter-spacing: 3px;
}
/*-----*/

.calendarMain {
  width: 100%;
  height: 100%;
  position: absolute;
  opacity: 1;
  display: flex;
  flex-flow: column;
}
.month,
.day {
  font-size: 14px;
  line-height: 30px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 3px;
}
.date {
  font-size: 40px;
  line-height: 40px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 3px;
}
/*-----*/

.outer .clock {
  width: 100%;
  height: 100%;
  position: absolute;
  font-size: 20px;
  line-height: 70px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 3px;
  text-align: center;
  opacity: 0;
  visibility: hidden;
}
/*-----*/

.year {
  width: 100%;
  position: absolute;
  top: 0;
  font-size: 14px;
  line-height: 40px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0;
  text-align: center;
  opacity: 0;
  visibility: hidden;
  .white-theme & {
    color: #000000;
  }
  .black-theme & {
    color: #ffffff;
  }
}
.calendarNormal {
  width: 100%;
  position: absolute;
  bottom: 0;
  font-size: 2px;
  line-height: 30px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 3px;
  text-align: center;
  opacity: 0;
  visibility: hidden;
}
.date2,
.day2,
.month2 {
  .white-theme & {
    color: #000000;
  }
  .black-theme & {
    color: #ffffff;
  }
}
/* -- usable codes end -- */
</style>