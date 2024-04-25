<template>
  <v-app>
    <Navbar />
    <v-main>
      <AlertBanner :messages="messages"/>
      <SnackbarMessage :message="snack.message" :timeout="snack.timeout"/>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
//
import { onBeforeMount } from "vue";
import Navbar from "@/components/Navbar.vue";
import AlertBanner from "@/components/alerts/AlertBanner.vue";
import MessageManager from "@/tools/MessageManager";
import SnackbarMessage from "@/components/alerts/SnackbarMessage.vue";
import { useSpaceStore } from "@/stores/SpaceStore";
import { usePostStore } from "@/stores/PostStore";

const messages = MessageManager.getInstance().get();
const snack = MessageManager.getInstance().getSnackbar();

onBeforeMount(() => {
  const spaceStore = useSpaceStore();
  const postStore = usePostStore();
  spaceStore.fetchSpaces();
  postStore.fetchPosts();
});

</script>
