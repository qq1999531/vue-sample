<template>
    
    <nav class="sidebar white-theme" :style="{ width: (200 * showSidebarFactor)+'px' }" @mouseenter="toggleSidebar" @mouseleave="toggleSidebar">
        {{showSidebar}}{{(200 * showSidebarFactor)+'px'}}
        <div class="clock" :style="{ width: (200 * showSidebarFactor)+'px' }">
            <Clock1 :showSidebarFactor="showSidebarFactor"/>
        </div>
    </nav>
</template>

<script setup>
import Clock1 from '@/components/clocks/Clock1.vue'
import { computed, ref } from 'vue'
const showSidebar = ref(true)
const showSidebarFactor = computed(() => {return showSidebar.value ? 1 : 0.2})
function toggleSidebar() {
    showSidebar.value = !showSidebar.value
}
</script>

<style lang="scss">
.sidebar{
    height: 100%;
    left: 0px;
    padding: 0px;
    position: fixed;
    border-right: 1px solid rgb(127, 127, 127);
    transition: 0.2s;
    .white-theme{
        background-color: rgb(255, 255, 255);
    }
    .black-theme{
        background-color: rgb(0, 0, 0);
    }
}

.clock{
    position: fixed;
    overflow: hidden;
    transition: 0.2s;
}
</style>