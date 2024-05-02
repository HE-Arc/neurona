<script setup lang="ts">

import router from "@/router";
import {useSpaceStore} from "@/stores/SpaceStore";

const props = defineProps<{
  id: string,
  title: string,
  about: string,
  joined: boolean,
}>();

const store = useSpaceStore();

function openSpace(){
  router.push({name: 'spaces.show', params: {id: props.id}});
}

</script>

<template>
<v-card
  :title="title"
  :text="about"
  :append-icon="joined ? 'mdi-check': ''"
  @click="openSpace"
>
  <v-card-actions>
    <v-spacer/>
      <v-btn
        v-if="!joined"
        prepend-icon="mdi-account-plus"
        @click.stop="store.joinSpace(props.id)"
      >
        Join
      </v-btn>
  </v-card-actions>

</v-card>
</template>

<style scoped>

</style>
