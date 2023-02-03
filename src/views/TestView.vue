<template>
  <!--<div class="calendarContainer"><FullCalendar /></div>-->
  <div>
    <Tabs
      :childTabs="[{ hash: 'live', header: 'live' }]"
      :defaultTabHash="'live'"
    />
  </div>
</template>

<script setup>
import FullCalendar from "@/components/calendars/fullCalendar.vue";
import Tabs from "@/components/tabs/Tabs.vue";
</script>

<style lang="scss">
.calendarContainer {
  width: 96%;
  display: flex;
  flex-flow: column;
}
</style>