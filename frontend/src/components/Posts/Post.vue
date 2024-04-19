<script setup>
import {onMounted, ref} from "vue";
import router from "@/router";
import axios from "axios";
import {formatDistanceToNow} from "date-fns";
import ApiRequests from "@/api/ApiRequests";

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
  is_saved: Boolean,
});

const saved = ref(props.is_saved ? 0 : null);

const post = ref({
  user_upvoted: props.has_upvoted,
  user_downvoted: props.has_downvoted,
  vote_count: props.votes,
  saved: props.is_saved,
});

const mounted = ref(true);
const vote = ref(post.value.user_upvoted ? 0 : post.value.user_downvoted ? 1 : null);
const snackbar = ref(false);

const req = new ApiRequests();

function upvote(postId) {
  req.upvote(postId);
}

function downvote(postId) {
  req.downvote(postId);
}

function unvote(postId) {
  req.unvote(postId);
}

function toggle_upvote() {
  post.value.user_upvoted = !post.value.user_upvoted;

  if (post.value.user_upvoted) {
    post.value.vote_count += 1;
    upvote(props.id);
  } else {
    post.value.vote_count -= 1;
    unvote(props.id);
  }

  if (post.value.user_downvoted) {
    post.value.vote_count += 1;
  }

  post.value.user_downvoted = false;
}

function toggle_downvote() {
  post.value.user_downvoted = !post.value.user_downvoted;

  if (post.value.user_downvoted) {
    post.value.vote_count -= 1;
    downvote(props.id);
  } else {
    post.value.vote_count += 1;
    unvote(props.id);
  }

  if (post.value.user_upvoted) {
    post.value.vote_count -= 1;
  }

  post.value.user_upvoted = false;
}

function toggle_save() {
  post.value.saved = !post.value.saved;
  (async () => {
    if (post.value.saved) {
      await req.savePost(props.id);
      snackbar.value = true;
    } else {
      await req.unsavePost(props.id);
    }
  })();
}

function open_post() {
  router.push({name: 'posts.show', params: {id: props.id}});
}

</script>

<template>

  <v-card
    v-if="mounted"
    :title="props.author_name"
    :subtitle="`@${props.author_username} \u00B7 ${formatDistanceToNow(props.timestamp, { addSuffix: true })}`"
    :prepend-avatar="props.author_avatar"
    @click="open_post"
    class="ma-4"
    :ripple="false"
  >
    <v-card-text class="text-body-1">
      <span>{{ props.content }}</span>
    </v-card-text>
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
          :text="props.comments"
        />
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


  <v-snackbar
    v-model="snackbar"
    timeout="2000"
    text="Post saved"
  />

</template>

<style scoped>

</style>
