<script setup>

import {ref, watch} from "vue";
import MessageManager from "@/tools/MessageManager";

const props = defineProps({
  message: String,
  timeout: Number
})

const snackbar = ref(false);

watch(() => props.message, (newVal) => {
  if (newVal !== null) {
    snackbar.value = true;

    setTimeout(() => {
      clear();
    }, props.timeout);
  }
});

function clear(){
  snackbar.value = false;
  MessageManager.getInstance().clearSnackbar();
}

</script>

<template>
  <v-snackbar
    :timeout="timeout"
    v-model="snackbar"
  >
    {{ message }}

    <template v-slot:actions>
      <v-btn
        color="blue"
        variant="text"
        @click="clear"
      >
        Close
      </v-btn>
    </template>
  </v-snackbar>
</template>

<style scoped>

</style>
