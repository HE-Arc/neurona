<script setup>

import {ref} from "vue";
import ApiRequests from "@/api/ApiRequests";
import MessageManager from "@/tools/MessageManager";

const props = defineProps({
  header: String,
  message: String,
  open: Boolean,
  confirmLabel: String,
  confirmIcon: String,
})

const emit = defineEmits(['update:open', 'confirm']);

</script>

<template>
  <v-dialog
    v-model="props.open"
    width="400"
  >
    <v-form>

      <v-card
        color="error"
      >
        <v-card-title>
          {{ header }}
        </v-card-title>
        <v-card-text>

          <p
            class="text-body-1"
          >
            {{ message }}
          </p>

        </v-card-text>
        <v-card-actions>
          <v-btn
            prepend-icon="mdi-arrow-left"
            @click="() => emit('update:open', false)"
          >
            Cancel
          </v-btn>
          <v-btn
            :prepend-icon="confirmIcon"
            @click="emit('confirm')"
          >
            {{ confirmLabel }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
  </v-dialog>
</template>
<style scoped>
</style>
