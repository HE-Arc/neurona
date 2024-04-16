<script setup>
import {ref} from 'vue';
import router from "@/router";
import ApiRequests from "@/api/ApiRequests";
import MessageManager from "@/tools/MessageManager";

const rules = ref([]);
const content = ref('');
const spaces = ref([]);
const valid = ref(false);

rules.value = [v => v.length <= 1000 || 'Max 1000 characters'];

// TODO fetch spaces from API
spaces.value = []

function submit() {
  new ApiRequests().createPost(content.value)
    .then(
      () => {
        MessageManager.getInstance().snackbar('Post created successfully', 5000);
        router.push({name: 'home'});
      }
    );
}

</script>

<template>
  <v-container>
    <v-form v-model="valid">
      <!-- TODO remove v-if attribute once spaces are fetched -->
      <v-autocomplete
        :items="spaces"
        prepend-icon="mdi-account"
        label="Space"
        v-if="false"
      >
      </v-autocomplete>

      <v-textarea
        counter
        label="What's on your mind?"
        :rules="rules"
        v-model="content"
        prepend-icon="mdi-text-box-edit"
        auto-grow
        clearable
      ></v-textarea>

      <div
        class="d-flex flex-row-reverse my-5"
      >

        <v-btn
          :disabled="!valid"
          prepend-icon="mdi-check"
          color="primary"
          class="mx-2"
          @click="submit"
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
