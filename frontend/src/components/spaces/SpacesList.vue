<script setup>

import SpaceElement from "@/components/spaces/SpaceElement.vue";
import {useSpaceStore} from "@/stores/SpaceStore";
import {onMounted} from "vue";

const store = useSpaceStore();

onMounted(() => {
  store.searchResults = store.joinedSpaces;
});

</script>

<template>

  <v-container>
    <v-row>
      <v-col
          v-for="space in store.searchResults"
          :key="space.id"
          cols="12"
          md="6"
          lg="4"
      >
        <SpaceElement
            :about="space.about"
            :id="space.id"
            :title="space.name"
            :joined="space.joined"
        />
      </v-col>
    </v-row>
  </v-container>

</template>

<style scoped>

</style>
