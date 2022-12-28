<template>
    
    <nav class="sidebar white-theme" :style="{ width: (200 * showSidebarFactor)+'px' }" @mouseenter="toggleSidebar" @mouseleave="toggleSidebar">
        {{showSidebar}}{{(200 * showSidebarFactor)+'px'}}
        <transition name="fade">
            <div v-show="showSidebar" class="clock" :style="{ width: (200 * showSidebarFactor)+'px' }">
                <Clock1 :showSidebarFactor="showSidebarFactor" />
            </div>
        </transition>
    </nav>
</template>

<script setup>
import Clock1 from '@/components/clocks/Clock1.vue'
import { computed, ref } from 'vue'
const showSidebar = ref(false)
const showSidebarFactor = computed(() => {return showSidebar.value ? 1 : 0.2})
function toggleSidebar() {
    showSidebar.value = !showSidebar.value
}
</script>

<style lang="scss">
.sidebar{
    overflow: hidden;
    height: 100%;
    left: 0px;
    padding: 0px;
    position: fixed;
    border-right: 1px solid rgb(127, 127, 127);
    transition: 0.2s;
}
.white-theme{
    background-color: rgb(255, 255, 255);
}
.black-theme{
    background-color: rgb(0, 0, 0);
}
.clock{
    position: fixed;
    overflow: hidden;
    transition: 0.2s;
    justify-content: center;
    align-items: center;
    svg circle{
        fill: transparent;
        stroke-width: 6;
        //stroke: var(--clr);
        stroke: #7f7f7f;
        stroke-linecap: round;
        stroke-dasharray: 440;
        stroke-dashoffset: 440;
    }
}
.fade-enter-from{
    opacity: 0;
}
.fade-enter-to{
    opacity: 1;
}
.fade-enter-active{
    transition: all 0.2s ease ;
}
.fade-leave-from{
    opacity: 1;
}
.fade-leave-to{
    opacity: 0;
}
.fade-leave-active{
    transition: all 0.2s ease ;
}
</style>