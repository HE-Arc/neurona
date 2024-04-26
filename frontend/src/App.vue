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
import Navbar from "@/components/Navbar.vue";
import AlertBanner from "@/components/alerts/AlertBanner.vue";
import MessageManager from "@/tools/MessageManager";
import SnackbarMessage from "@/components/alerts/SnackbarMessage.vue";

const messages = MessageManager.getInstance().get();
const snack = MessageManager.getInstance().getSnackbar();

</script>
