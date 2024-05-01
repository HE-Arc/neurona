<script setup>

import {onMounted, ref} from "vue";
import ApiRequests from "@/api/ApiRequests";

const props = defineProps({
  query: String,
});

const spaces = ref([]);
const req = new ApiRequests();

onMounted(() => {
  (async () => {
    spaces.value = await req.searchSpaces(query);
    console.log(spaces.value);
  })();
});

</script>

<template>

</template>

<style scoped>

</style>
