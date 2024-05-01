<script setup lang="ts">
import SpaceTimeline from "@/components/spaces/SpaceTimeline.vue";

const props = defineProps<{
  id: string,
}>();

</script>
<template>

  <SpaceTimeline :space-id="id" />

</template>

<style scoped>
</style>
