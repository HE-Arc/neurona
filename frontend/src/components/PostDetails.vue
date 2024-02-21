<script setup>

import Post from "@/components/Post.vue";
import Comment from "@/components/Comment.vue";
import ReturnBtn from "@/components/ReturnBtn.vue";
import {ref} from "vue";

const dialog = ref(false);

</script>

<template>


  <div
      class="d-flex justify-space-between align-center"
  >
    <ReturnBtn/>
    <v-btn
        prepend-icon="mdi-delete"
        color="error"
        class="ma-5"
    >
      Delete

      <v-dialog
          v-model="dialog"
          activator="parent"
          width="auto"
      >
        <v-card
            class="pa-1"
        >
          <v-card-title
          >
            Delete post
          </v-card-title>
          <v-card-text>
            Are you sure you want to delete this post? This action cannot be undone.
          </v-card-text>
          <v-spacer/>
          <v-card-actions
              class="d-flex justify-end"
          >
            <v-btn
                @click="dialog = false"
                prepend-icon="mdi-close"
            >
              Cancel
            </v-btn>
            <v-btn
                color="error"
                @click="dialog = false"
                prepend-icon="mdi-delete"
            >
              Delete
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

    </v-btn>
  </div>

  <Post/>

  <v-divider/>

  <h2
      class="text-h6 ma-4"
  >
    Comments
  </h2>

  <Comment/>
  <Comment/>
  <Comment/>
  <Comment/>

</template>

<style scoped>

</style>
