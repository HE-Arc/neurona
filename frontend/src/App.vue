<template>
  <v-app>
    <Navbar :logged-in="state.authenticated"/>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script setup>
//
import Navbar from "@/components/Navbar.vue";
import {state} from "@/Authentication/store";

</script>
