<script setup>

import { ref } from 'vue';

const comment = ref(null);
const vote = ref(null);

//TODO fetch content from API
comment.value = {
  id: 1,
  user: {
    username: 'admin',
    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
    name: 'a random user',
  },
  content: 'Thank you for your post, I also like penguins!',
  vote_count: 1,
  user_upvoted: true,
  user_downvoted: false,
}
vote.value = comment.value.user_upvoted ? 0 : comment.value.user_downvoted ? 1 : null;

function toggle_upvote(){
  comment.value.user_upvoted = !comment.value.user_upvoted;
  comment.value.vote_count += comment.value.user_upvoted ? 1 : -1;
  comment.value.vote_count += comment.value.user_downvoted ? 1 : 0;
  comment.value.user_downvoted = false;
}

function toggle_downvote(){
  comment.value.user_downvoted = !comment.value.user_downvoted;
  comment.value.vote_count += comment.value.user_downvoted ? -1 : 1;
  comment.value.vote_count += comment.value.user_upvoted ? -1 : 0;
  comment.value.user_upvoted = false;
}

</script>

<template>
  <v-card
      class="ma-4"
      :title="comment.user.name"
      :subtitle="comment.user.username"
      :prepend-avatar="comment.user.avatar"
  >
    <v-card-text>
      Thank you for your comment, I also like penguins!
      Maybe we can discuss more about them?
      I think they are very interesting animals.
    </v-card-text>
    <v-card-actions
    >
      <v-btn-toggle
          v-model="vote"
      >
        <v-btn
            prepend-icon="mdi-arrow-up-bold"
            :color="comment.user_upvoted ? 'green' : ''"
            @click="toggle_upvote"
            class="h-75"
        >
          {{ comment.vote_count }}
        </v-btn>

        <v-btn
            icon="mdi-arrow-down-bold"
            :color="comment.user_downvoted ? 'red' : ''"
            @click="toggle_downvote"
            class="h-75"
        />

      </v-btn-toggle>
    </v-card-actions>
  </v-card>
</template>

<style scoped>

</style>
