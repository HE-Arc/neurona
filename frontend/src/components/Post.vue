<script setup>
import {onMounted, ref} from "vue";
import router from "@/router";

const props = defineProps({
  id: Number,
});

const post = ref({});
const mounted = ref(false);
const vote = ref(null);
const saved = ref(null);
const snackbar = ref(false);

onMounted(async () => {
  await new Promise(resolve => setTimeout(resolve, 500));
  post.value = {
    id: props.id,
    link: "/posts/" + props.id,
    title: "Hello world",
    content: "Hello everyone, this is my first post on this platform. " +
        "I hope you like it. I'm a big fan of penguins, so I'll be posting " +
        "a lot of penguin-related content. I hope you enjoy it!",
    vote_count: 12,
    user_upvoted: false,
    user_downvoted: true,
    comments: 3,
    saved: true,
    timestamp: "2021-10-10T12:00:00Z",
    author: {
      id: 1,
      username: "kingpenguin",
      avatar: "https://nzbirdsonline.org.nz/sites/all/files/2X2A1697%20King%20Penguin%20bol.jpg",
    },
    space: {
      id: 1,
      title: "ISC1",
      avatar: "",
    },
  };
  vote.value = post.value.user_upvoted ? 0 : post.value.user_downvoted ? 1 : null;
  saved.value = post.value.saved ? 0 : null;
  mounted.value = true;
});

function toggle_upvote(){
  post.value.user_upvoted = !post.value.user_upvoted;
  post.value.vote_count += post.value.user_upvoted ? 1 : -1;
  post.value.vote_count += post.value.user_downvoted ? 1 : 0;
  post.value.user_downvoted = false;
}

function toggle_downvote(){
  post.value.user_downvoted = !post.value.user_downvoted;
  post.value.vote_count += post.value.user_downvoted ? -1 : 1;
  post.value.vote_count += post.value.user_upvoted ? -1 : 0;
  post.value.user_upvoted = false;
}

function toggle_save(){
  post.value.saved = !post.value.saved;
  snackbar.value = post.value.saved;
}

function open_post(){
  router.push({ path: post.value.link });
}

</script>

<template>

  <v-card
      v-if="mounted"
      :title="post.title"
      :subtitle="post.author.username + ' on ' + post.space.title"
      :text="post.content"
      :prepend-avatar="post.author.avatar"
      @click="open_post"
      class="mx-4 my-4"
      :ripple="false"
  >
    <v-card-actions>
      <v-btn-toggle
          v-model="vote"
      >
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

      <v-btn-toggle
          class="mx-2"
      >
        <v-btn
            prepend-icon="mdi-comment"
        >
          {{ post.comments }}
        </v-btn>
      </v-btn-toggle>

      <v-spacer/>

      <v-btn-toggle
          v-model="saved"
      >
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

<style scoped>

</style>
