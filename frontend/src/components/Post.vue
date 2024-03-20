<script setup>
import {onMounted, ref} from "vue";
import router from "@/router";
import axios from "axios";
import routes from "@/api/routes";

const props = defineProps({
  id: Number,
  title: String,
  content: String,
  timestamp: String,
  author_id: Number,
  author_username: String,
  author_name: String,
  author_avatar: String,
  space_id: Number,
  space_title: String,
  comments: Number,
  votes: Number,
  has_upvoted: Boolean,
  has_downvoted: Boolean,
});

const post = ref({
  user_upvoted: props.has_upvoted,
  user_downvoted: props.has_downvoted,
  vote_count: props.votes,
});

const mounted = ref(true);
const vote = ref(post.value.user_upvoted ? 0 : post.value.user_downvoted ? 1 : null);
const saved = ref(null);
const snackbar = ref(false);

onMounted(()=>{
  if(post.value.user_upvoted){
    console.log(`User has upvoted post ${props.id}`);
  }
});


function vote_(url){
  axios.post(url, {}, {
    headers: {
      Authorization: sessionStorage.getItem('token')
    }
  }).then(()=>{
    console.log('Voted');
  }).catch((e)=>{
    console.log(e);
  });
}

function toggle_upvote(){
  post.value.user_upvoted = !post.value.user_upvoted;

  if(post.value.user_upvoted){
    post.value.vote_count += 1;
    const url = routes.posts.upvote(props.id);
    vote_(url);
  } else {
    post.value.vote_count -= 1;
    const url = routes.posts.unvote(props.id);
    vote_(url);
  }

  if(post.value.user_downvoted){
    post.value.vote_count += 1;
  }

  post.value.user_downvoted = false;
}

function toggle_downvote(){
  post.value.user_downvoted = !post.value.user_downvoted;

  if(post.value.user_downvoted){
    post.value.vote_count -= 1;
    const url = routes.posts.downvote(props.id);
    vote_(url);
  } else {
    post.value.vote_count += 1;
    const url = routes.posts.unvote(props.id);
    vote_(url);
  }

  if(post.value.user_upvoted){
    post.value.vote_count -= 1;
  }

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
      :title="props.title"
      :subtitle="props.author_username"
      :text="props.content"
      :prepend-avatar="props.author_avatar"
      @click="open_post"
      class="ma-4"
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
