<script setup>
import {ref, computed} from 'vue';
import router from "@/router";
import ApiRequests from "@/api/ApiRequests";
import MessageManager from "@/tools/MessageManager";
import { useSpaceStore } from "@/stores/SpaceStore";
import { usePostStore } from '@/stores/PostStore';

const spaceStore = useSpaceStore();
const postStore = usePostStore();
const rules = ref([]);
const content = ref('');
const selectedSpace = ref(null);
const valid = ref(false);

rules.value = [v => v.length <= 1000 || 'Max 1000 characters'];

const spaces = computed(() => spaceStore.joinedSpaces);

async function submit(){
  await postStore.createPost(content.value, selectedSpace.value);
  MessageManager.getInstance().snackbar('Post created successfully', 5000);
  await router.push({name: 'home'});
}

</script>

<template>
  <v-container>
    <v-form v-model="valid">
      <v-autocomplete
        :items="spaces"
        item-title="name"
        item-value="id"
        prepend-icon="mdi-account"
        label="Space"
        v-model="selectedSpace"
      ></v-autocomplete>

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
