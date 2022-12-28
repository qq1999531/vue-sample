<template>
    <svg>
        <circle :cx="50 * showSidebarFactor" :cy="50 * showSidebarFactor" :r="50 * showSidebarFactor"></circle>
    </svg>
    {{50 * showSidebarFactor}}
</template>

<script setup>
    const { computed }=require("@vue/runtime-core")

    defineProps({
        showSidebarFactor : Number
    })
</script>

<style lang="scss">

</style>