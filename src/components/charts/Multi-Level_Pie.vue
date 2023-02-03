<template>
  <div
    id="multi-level_pie_container"
    :style="{
      width: props.width + 'px',
      height: props.width + 'px',
    }"
    class="multiLevelPieContainer"
  ></div>
  <span
    v-show="labelVVisible"
    class="centerLabel"
    :style="{ top: -props.width / 2 - 20 + 'px' }"
    >{{ labelName }}<br />liveCount:{{ labelValue }}<br />percent:{{
      labelPercent
    }}%</span
  >
</template>

<script setup>
import { onMounted, ref } from "@vue/runtime-core";
import * as d3 from "d3";

const props = defineProps(["data", "width"]);
const labelName = ref("");
const labelVVisible = ref(false);
const labelValue = ref(0);
const labelPercent = ref(0);
let radius = props.width / 6;
let circleNode = { data: { name: "" }, value: 0 };
const color = d3.scaleOrdinal(
  d3.quantize(d3.interpolateRainbow, props.data.children.length + 1)
);
const arc = d3
  .arc()
  .startAngle((d) => d.x0)
  .endAngle((d) => d.x1)
  .padAngle((d) => Math.min((d.x1 - d.x0) / 2, 0.005))
  .padRadius(radius * 1.5)
  .innerRadius((d) => d.y0 * radius)
  .outerRadius((d) => Math.max(d.y0 * radius, d.y1 * radius - 1));
const format = d3.format(",d");

function partition(data) {
  const root = d3
    .hierarchy(data)
    .sum((d) => d.value)
    .sort((a, b) => b.value - a.value);
  return d3.partition().size([2 * Math.PI, root.height + 1])(root);
}
function renderChart(data, width) {
  const root = partition(data);
  root.each((d) => (d.current = d));
  circleNode = root;
  const svg = d3
    .select("#multi-level_pie_container")
    .append("svg")
    .attr("viewBox", [0, 0, width, width])
    .style("font", "10px sans-serif");
  const element = svg.node();
  element.value = { sequence: [], percentage: 0.0 };
  const g = svg
    .append("g")
    .attr("transform", `translate(${width / 2},${width / 2})`);
  const path = g
    .append("g")
    .selectAll("path")
    .data(root.descendants().slice(1))
    .join("path")
    .attr("fill", (d) => {
      return d.data.color ? d.data.color : color(d.data.name);
    })
    .attr("fill-opacity", (d) =>
      arcVisible(d.current) ? (d.children ? 0.6 : 0.4) : 0
    )
    .attr("pointer-events", (d) => (arcVisible(d.current) ? "auto" : "none"))
    .attr("d", (d) => arc(d.current))
    .on("mouseenter", (event, d) => {
      // Get the ancestors of the current segment, minus the root
      const sequence = d.ancestors().reverse().slice(1);
      // Highlight the ancestors
      path.attr("fill-opacity", (node) =>
        sequence.indexOf(node) >= 0 ? 1.0 : 0.4
      );
      const percentage = ((100 * d.value) / root.value).toPrecision(3);
      // Update the value of this view with the currently hovered sequence and percentage
      element.value = { sequence, percentage };
      labelName.value = d.data.name;
      labelVVisible.value = true;
      labelValue.value = d.value;
      labelPercent.value = percentage;
      element.dispatchEvent(new CustomEvent("input"));
    });
  path
    .filter((d) => d.children)
    .style("cursor", "pointer")
    .on("click", clicked);
  const label = g
    .append("g")
    .attr("pointer-events", "none")
    .attr("text-anchor", "middle")
    .style("user-select", "none")
    .selectAll("text")
    .data(root.descendants().slice(1))
    .join("text")
    .attr("dy", "0.35em")
    .attr("fill-opacity", (d) => +labelVisible(d.current))
    .attr("transform", (d) => labelTransform(d.current))
    .text((d) => d.data.name);
  const parent = g
    .append("circle")
    .datum(root)
    .attr("r", radius)
    .attr("fill", "none")
    .attr("pointer-events", "all")
    .on("click", clicked)
    .on("mouseenter", (event, d) => {
      const percentage = ((100 * circleNode.value) / root.value).toPrecision(3);
      labelName.value = circleNode.data.name;
      labelVVisible.value = true;
      labelValue.value = circleNode.value;
      labelPercent.value = percentage;
    });
  function clicked(event, p) {
    parent.datum(p.parent || root);
    circleNode = p ? p : root;
    root.each(
      (d) =>
        (d.target = {
          x0:
            Math.max(0, Math.min(1, (d.x0 - p.x0) / (p.x1 - p.x0))) *
            2 *
            Math.PI,
          x1:
            Math.max(0, Math.min(1, (d.x1 - p.x0) / (p.x1 - p.x0))) *
            2 *
            Math.PI,
          y0: Math.max(0, d.y0 - p.depth),
          y1: Math.max(0, d.y1 - p.depth),
        })
    );
    const t = g.transition().duration(750);
    // Transition the data on all arcs, even the ones that aren’t visible,
    // so that if this transition is interrupted, entering arcs will start
    // the next transition from the desired position.
    path
      .transition(t)
      .tween("data", (d) => {
        const i = d3.interpolate(d.current, d.target);
        return (t) => (d.current = i(t));
      })
      .filter(function (d) {
        return +this.getAttribute("fill-opacity") || arcVisible(d.target);
      })
      .attr("fill-opacity", (d) =>
        arcVisible(d.target) ? (d.children ? 0.6 : 0.4) : 0
      )
      .attr("pointer-events", (d) => (arcVisible(d.target) ? "auto" : "none"))
      .attrTween("d", (d) => () => arc(d.current));
    label
      .filter(function (d) {
        return +this.getAttribute("fill-opacity") || labelVisible(d.target);
      })
      .transition(t)
      .attr("fill-opacity", (d) => +labelVisible(d.target))
      .attrTween("transform", (d) => () => labelTransform(d.current));
  }

  function arcVisible(d) {
    return d.y1 <= 3 && d.y0 >= 1 && d.x1 > d.x0;
  }

  function labelVisible(d) {
    return d.y1 <= 3 && d.y0 >= 1 && (d.y1 - d.y0) * (d.x1 - d.x0) > 0.03;
  }

  function labelTransform(d) {
    const x = (((d.x0 + d.x1) / 2) * 180) / Math.PI;
    const y = ((d.y0 + d.y1) / 2) * radius;
    return `rotate(${x - 90}) translate(${y},0) rotate(${x < 180 ? 0 : 180})`;
  }

  return svg.node();
}

onMounted(() => {
  renderChart(props.data, props.width);
});
</script>
<style lang="scss">
.centerLabel {
  position: relative;
  height: 0px;
  font-size: 8px;
}
</style>