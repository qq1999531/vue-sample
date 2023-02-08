<template>
  <!--<div class="calendarContainer"><FullCalendar /></div>-->
  <div class="testView">
    <Tabs
      :childTabs="[
        { hash: 'live', header: 'live' },
        { hash: 'test', header: 'test' },
      ]"
      :defaultTabHash="'live'"
    ></Tabs>
  </div>
</template>

<script setup>
import FullCalendar from "@/components/calendars/fullCalendar.vue";
import Tabs from "@/components/tabs/Tabs.vue";
</script>

<style lang="scss">
.testView {
  transition: 0.2s;
  align-items: center;
  display: flex;
  flex-flow: column;
}
</style>