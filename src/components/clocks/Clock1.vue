<template>
    <svg>
        <filter id="glow">
				<feGaussianBlur stdDeviation="2.5" result="coloredBlur"/>
				<feMerge>
						<feMergeNode in="coloredBlur"/>
						<feMergeNode in="SourceGraphic"/>
				</feMerge>
		</filter>		
		
		<filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
			<feGaussianBlur in="SourceAlpha" stdDeviation="3" result="shadow"/>
			<feOffset dx="1" dy="1"/>
			<feMerge>
				<feMergeNode/>
				<feMergeNode in="SourceGraphic"/>
			</feMerge>
		</filter>		
        <circle :cx="100" :cy="50" :r="50" style="--clr:#7f7f7f;"></circle>
    </svg>
</template>

<script setup>
    import { computed } from "@vue/runtime-core"

    defineProps({
        showSidebarFactor : Number
    })
</script>

<style lang="scss">

</style>