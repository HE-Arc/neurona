<script setup>

import {ref} from "vue";
import ApiRequests from "@/api/ApiRequests";
import EventBus from "@/tools/EventBus";
import {useSpaceStore} from "@/stores/SpaceStore";

const props = defineProps({
});

const name = ref('');
const about = ref('');
const open = ref(false);
const store = useSpaceStore();

async function submit(){
  open.value = false;
  await store.createSpace(name.value, about.value);
}

</script>

<template>
  <v-btn
    color="primary"
    class="ma-4"
    @click="() => open = true"
  >
    Create a new space
  </v-btn>

  <v-dialog
    v-model="open"
    width="400"
  >
    <v-form>

      <v-card>
        <v-card-title>
          Create a new space
        </v-card-title>
        <v-card-text>

          <v-text-field
            v-model="name"
            label="Space name"
          />

          <v-textarea
            v-model="about"
            label="About this space"
          />

        </v-card-text>
        <v-card-actions
          class="d-flex justify-end"
        >
          <v-btn
            prepend-icon="mdi-close"
            @click="() => open = false"
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
