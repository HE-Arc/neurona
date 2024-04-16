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

<script setup>
//
import Navbar from "@/components/Navbar.vue";
import AlertBanner from "@/components/AlertBanner.vue";
import MessageManager from "@/tools/MessageManager";
import SnackbarMessage from "@/components/SnackbarMessage.vue";
const messages = MessageManager.getInstance().get();
const snack = MessageManager.getInstance().getSnackbar();

</script>
