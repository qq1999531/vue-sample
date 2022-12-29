<template>
  <h1>Demo App</h1>
  <FullCalendar :options='calendarOptions' />
</template>

<script setup>
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import { reactive } from '@vue/reactivity'

const calendarOptions = reactive({
    plugins: [dayGridPlugin],
    initialView: 'dayGridMonth',
    weekends: false,
    events: [
        { title: 'Meeting', start: new Date() }
    ]
})
</script>