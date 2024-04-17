<script setup>

import {onMounted, ref} from 'vue';
import {formatDistanceToNow} from "date-fns";
import MessageManager from "@/tools/MessageManager";
import ApiRequests from "@/api/ApiRequests";

const vote = ref(null);
const removeDialog = ref(false);
const req = new ApiRequests();
const is_author = ref(false);

const emit = defineEmits(['refresh']);

const props = defineProps({
  id: Number,
  content: String,
  timestamp: String,
  author_id: Number,
  author_username: String,
  author_name: String,
  author_avatar: String,
  space_id: Number,
  votes: Number,
  has_upvoted: Boolean,
  has_downvoted: Boolean,
});

onMounted(() => {
  (async () => {
    const username = (await req.getProfile()).username;
    is_author.value = props.author_username === username;
  })();
});

vote.value = props.has_upvoted ? 0 : props.has_downvoted ? 1 : null;

const comment = ref({
  user_upvoted: props.has_upvoted,
  user_downvoted: props.has_downvoted,
  vote_count: props.votes,
});

function toggle_upvote() {
  comment.value.user_upvoted = !comment.value.user_upvoted;
  comment.value.vote_count += comment.value.user_upvoted ? 1 : -1;
  comment.value.vote_count += comment.value.user_downvoted ? 1 : 0;
  comment.value.user_downvoted = false;

  (async () => {
    if (comment.value.user_upvoted) {
      await req.upvoteComment(props.id);
    } else {
      await req.unvoteComment(props.id);
    }
  })();
}

function toggle_downvote() {
  comment.value.user_downvoted = !comment.value.user_downvoted;
  comment.value.vote_count += comment.value.user_downvoted ? -1 : 1;
  comment.value.vote_count += comment.value.user_upvoted ? -1 : 0;
  comment.value.user_upvoted = false;

  (async () => {
    if (comment.value.user_downvoted) {
      await req.downvoteComment(props.id);
    } else {
      await req.unvoteComment(props.id);
    }
  })();
}

function deleteComment() {
  (async () => {
    removeDialog.value = false;
    await req.deleteComment(props.id);
    MessageManager.getInstance().snackbar('Comment deleted successfully');
    emit('refresh');
  })();
}

</script>

<template>
  <v-card
    class="ma-4"
    :title="props.author_name"
    :subtitle="`@${props.author_username} \u00B7 ${formatDistanceToNow(props.timestamp, { addSuffix: true })}`"
    :prepend-avatar="props.author_avatar"
  >
    <v-card-text>
      {{ props.content }}
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
      <v-spacer/>

      <v-btn
        color="error"
        v-if="is_author"
      >
        <v-icon
          icon="mdi-delete"
        />
        <v-dialog
          v-model="removeDialog"
          activator="parent"
          width="auto"
        >
          <v-card
            class="pa-1"
          >
            <v-card-title
            >
              Delete comment
            </v-card-title>
            <v-card-text>
              Are you sure you want to delete this comment? This action cannot be undone.
            </v-card-text>
            <v-spacer/>
            <v-card-actions
              class="d-flex justify-end"
            >
              <v-btn
                @click="removeDialog = false"
                prepend-icon="mdi-close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="error"
                @click="deleteComment"
                prepend-icon="mdi-delete"
              >
                Delete
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<style scoped>

</style>
