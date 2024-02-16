<script setup>
import {ref} from 'vue';

const rules = ref([]);
const value = ref('');
const spaces = ref([]);
const valid = ref(false);

rules.value = [v => v.length <= 1000 || 'Max 1000 characters'];
spaces.value = [
  'ISC1',
  'ISC2',
  'ISC3',
  'apero!!!',
  'admin',
]

</script>

<template>
  <v-container>
    <v-form v-model="valid">
      <v-autocomplete
          :items="spaces"
          prepend-icon="mdi-account"
          label="Space"
      >
      </v-autocomplete>
      <v-textarea
          counter
          label="Post content"
          :rules="rules"
          :model-value="value"
          prepend-icon="mdi-text-box-edit"
          auto-grow
          clearable
      ></v-textarea>

      <div
          class="d-flex flex-row-reverse my-5"
      >

        <v-btn
            type="submit"
            :disabled="!valid"
            prepend-icon="mdi-check"
            color="primary"
            class="mx-2"
        >
          Submit
        </v-btn>

        <v-btn
          prepend-icon="mdi-close"
          text="Cancel"
          class="mx-2"
          @click="() => $router.go(-1)"
          />
      </div>
    </v-form>
  </v-container>
</template>

<style scoped>

</style>
