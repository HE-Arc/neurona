<script setup lang="ts">

import SpaceElement from "@/components/spaces/SpaceElement.vue";
import {useSpaceStore} from "@/stores/SpaceStore";

const store = useSpaceStore();

</script>

<template>
  <v-text-field
    v-model="store.query"
    label="Search for a space"
    prepend-icon="mdi-magnify"
    class="ma-4"
    @input="store.search"
  />
</template>

<style scoped>

</style>
