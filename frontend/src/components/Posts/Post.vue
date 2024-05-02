<script setup>
import {onMounted, ref} from "vue";
import router from "@/router";
import axios from "axios";
import {formatDistanceToNow} from "date-fns";
import ApiRequests from "@/api/ApiRequests";
import {usePostStore} from "@/stores/PostStore";

const props = defineProps({
  post: Object,
});

const store = usePostStore();

const saved = ref(props.post.is_saved ? 0 : null);

const mounted = ref(true);
const vote = ref(props.post.votes_and_comments.has_upvoted ? 0 : props.post.votes_and_comments.has_downvoted ? 1 : null);
const snackbar = ref(false);

const req = new ApiRequests();

function toggle_upvote() {
  store.toggleUpvote(props.post);
}

function toggle_downvote() {
  store.toggleDownvote(props.post);
}

function toggle_save() {
  store.toggleSave(props.post);
}

function open_post() {
  router.push({name: 'posts.show', params: {id: props.post.id}});
}

function open_user() {
  router.push({name: 'profile.show', params: {username: props.post.user.username}});
}

</script>

<template>

  <v-card
    v-if="mounted"
    @click="open_post"
    class="ma-4"
    :ripple="false"
  >
    <template v-slot:prepend>

      <v-avatar
        :image="props.post.user.image_url"
        :size="40"
        @click.stop="open_user"
      >
      </v-avatar>
    </template>

    <template
      v-slot:title
    >
      <span
        @click.stop="open_user"
      >
        {{ props.post.user.display_name }}
      </span>
    </template>

    <template
      v-slot:subtitle
    >
      <span
        @click.stop="open_user"
      >
        {{ `@${props.post.user.username} \u00B7 ${formatDistanceToNow(props.post.created_at, {addSuffix: true})}` }}
      </span>
    </template>

    <v-card-text class="text-body-1">
      <span>{{ props.post.content }}</span>
    </v-card-text>
    <v-card-actions>
      <v-btn-toggle
        v-model="vote"
      >
        <v-btn
          prepend-icon="mdi-arrow-up-bold"
          :color="props.post.votes_and_comments.has_upvoted ? 'green' : ''"
          @click.stop="toggle_upvote"
        >
          {{ props.post.votes_and_comments.votes }}
        </v-btn>

        <v-btn
          icon="mdi-arrow-down-bold"
          :color="props.post.votes_and_comments.has_downvoted ? 'red' : ''"
          @click.stop="toggle_downvote"
        />

      </v-btn-toggle>

      <v-btn-toggle
        class="mx-2"
      >
        <v-btn
          prepend-icon="mdi-comment"
          :text="props.post.votes_and_comments.comments"
        />
      </v-btn-toggle>

      <v-spacer/>

      <v-btn-toggle
        v-model="saved"
      >
        <v-btn
          icon="mdi-bookmark"
          @click.stop="toggle_save"
          :color="props.post.is_saved ? 'primary' : ''"
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
