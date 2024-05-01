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
