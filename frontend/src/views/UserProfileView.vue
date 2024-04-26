<script setup lang="ts">

import UserProfile from "@/components/Profile/UserProfile.vue";

const props = defineProps<{
  username: string;
}>();

</script>

<template>
  <UserProfile :username="username" />
</template>

<style scoped>

</style>
