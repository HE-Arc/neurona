<template>
  <v-app>
    <Navbar />
    <v-main>
      <AlertBanner :messages="messages"/>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script setup>
//
import Navbar from "@/components/Navbar.vue";
import AlertBanner from "@/components/AlertBanner.vue";
import MessageManager from "@/tools/MessageManager";
const messages = MessageManager.getInstance().get();

</script>
