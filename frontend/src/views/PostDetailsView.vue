<script setup lang="ts">

import PostDetails from "@/components/Posts/PostDetails.vue";

const props = defineProps<{
  id: string;
}>();

</script>

<template>
  <PostDetails :id="id" />
</template>

<style scoped>

</style>
