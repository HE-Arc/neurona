<template>
  <v-app>
    <Navbar :logged-in="state.authenticated"/>
    <v-main>
      <AlertBanner :messages="messages"/>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script setup>
//
import Navbar from "@/components/Navbar.vue";
import {state} from "@/Authentication/store";
import AlertBanner from "@/components/AlertBanner.vue";
import MessageManager from "@/tools/MessageManager";
const messages = MessageManager.getInstance().get();

</script>
