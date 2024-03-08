<template>
  <v-card
    v-if="mounted"
    :title="post.author.name"
    :subtitle="post.author.username + ' on ' + post.space.title"
    :text="post.content"
    :prepend-avatar="post.author.avatar"
    @click="open_post"
    class="ma-4"
    :ripple="false"
  >
    <v-card-actions>
      <v-btn-toggle v-model="vote">
        <v-btn
          prepend-icon="mdi-arrow-up-bold"
          :color="post.user_upvoted ? 'green' : ''"
          @click.stop="toggle_upvote"
        >
          {{ post.vote_count }}
        </v-btn>

        <v-btn
          icon="mdi-arrow-down-bold"
          :color="post.user_downvoted ? 'red' : ''"
          @click.stop="toggle_downvote"
        />
      </v-btn-toggle>

      <v-btn-toggle class="mx-2">
        <v-btn prepend-icon="mdi-comment">
          {{ post.comments }}
        </v-btn>
      </v-btn-toggle>

      <v-spacer></v-spacer>

      <v-btn-toggle v-model="saved">
        <v-btn
          icon="mdi-bookmark"
          @click.stop="toggle_save"
          :color="post.saved ? 'primary' : ''"
        >
        </v-btn>
      </v-btn-toggle>
    </v-card-actions>
  </v-card>

  <v-skeleton-loader v-else type="card" class="mx-4"></v-skeleton-loader>

  <v-snackbar
    v-model="snackbar"
    timeout="2000"
    text="Post saved"
  />
</template>

<script setup>
import { ref } from 'vue';
import router from '@/router';

const props = defineProps({
  post: Object,
});

const mounted = ref(true); // Assuming dynamic data, you may handle loading state differently.
const vote = ref(null);
const saved = ref(props.post.saved);
const snackbar = ref(false);

function toggle_upvote() {
  //  TODO Implement API call 
}

function toggle_downvote() {
  // Implement API call 
}

function toggle_save() {
  // Implement API call
}

function open_post() {
  router.push({ path: props.post.link });
}
</script>

<style scoped>
/* Your styles here */
</style>
