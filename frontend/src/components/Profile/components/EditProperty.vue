<script setup>

import {ref} from "vue";
import ApiRequests from "@/api/ApiRequests";
import MessageManager from "@/tools/MessageManager";

const props = defineProps({
  name: String,
  attribute_name: String,
  value: String,
  open: Boolean,
  area: Boolean
})

const value_ = ref(props.value);
const emit = defineEmits(['update:open', 'refresh']);

function submit(){
  emit('refresh', value_.value);
  emit('update:open', false);
}

</script>

<template>
  <v-dialog
    v-model="props.open"
    width="400"
  >
    <v-form>

      <v-card>
        <v-card-title>
          Edit {{ name }}
        </v-card-title>
        <v-card-text>

          <v-text-field
            v-model="value_"
            :label="name"
            v-if="!props.area"
          >
          </v-text-field>

          <v-textarea
            v-model="value_"
            :label="name"
            v-else
          >
          </v-textarea>

        </v-card-text>
        <v-card-actions
          class="d-flex justify-end"
        >
          <v-btn
            prepend-icon="mdi-close"
            @click="() => emit('update:open', false)"
            color="error"
          >
            Cancel
          </v-btn>
          <v-btn
            prepend-icon="mdi-check"
            color="primary"
            @click="submit"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
  </v-dialog>
</template>
<style scoped>
</style>
