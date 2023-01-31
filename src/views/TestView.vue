<template>
  <div class="calendarContainer"><FullCalendar /></div>
</template>

<script setup>
import FullCalendar from "@/components/calendars/fullCalendar.vue";
</script>

<style lang="scss">
.calendarContainer {
  width: 96%;
  display: flex;
  flex-flow: column;
}
</style>