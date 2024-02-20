<script setup>

import router from "@/router";
</script>

<template>
  <v-btn
      prepend-icon="mdi-arrow-left"
      class="ma-5"
      @click="router.go(-1)"
  >
    Back
  </v-btn>
</template>

<style scoped>

</style>
