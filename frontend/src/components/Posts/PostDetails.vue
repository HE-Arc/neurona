<script setup>

import Post from "@/components/Posts/Post.vue";
import ReturnBtn from "@/components/ReturnBtn.vue";
import {onMounted, ref} from "vue";
import ApiRequests from "@/api/ApiRequests";
import MessageManager from "@/tools/MessageManager";
import router from "@/router";
import NewComment from "@/components/Posts/NewComment.vue";
import Comment from "@/components/Posts/Comment.vue";
import {usePostStore} from "@/stores/PostStore";
import {useUserStore} from "@/stores/UserStore";

const props = defineProps({
  id: String,
})

const removeDialog = ref(false);
const commentDialog = ref(false);
const comments = ref([]);
const postMounted = ref(false);
const commentsMounted = ref(false);
const is_author = ref(false);
const postStore = usePostStore();
const post = ref(null);

const req = new ApiRequests();

async function fetchComments() {
  const response = (await req.getComments(props.id));
  response.sort((a, b) => {
    return new Date(b.created_at) - new Date(a.created_at);
  });

  comments.value = response;
  post.value.votes_and_comments.comments = comments.value.length;
}

onMounted(() => {
  (async () => {
    window.scrollTo(0, 0);
    post.value = await postStore.fetchPost(props.id);
    postMounted.value = true;

    is_author.value = post.value.user.username === useUserStore().user.username;

    await fetchComments();
    commentsMounted.value = true;
  })();
});

async function deletePost() {
  await postStore.deletePost(post.value);
  MessageManager.getInstance().snackbar('Post deleted successfully.', 5000);
  await router.push({name: 'home'});
}

function refreshComments() {
  console.log("refreshing comments");
  (async () => {
    await fetchComments();
  })();
}

function openProfile() {
  console.log('open profile');
}

</script>

<template>


  <div
    class="d-flex justify-space-between align-center"
  >
    <ReturnBtn/>
    <v-btn
      v-if="is_author"
      prepend-icon="mdi-delete"
      color="error"
      class="ma-5"
    >
      Delete

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
              @click="removeDialog = false"
              prepend-icon="mdi-close"
            >
              Cancel
            </v-btn>
            <v-btn
              color="error"
              @click="deletePost"
              prepend-icon="mdi-delete"
            >
              Delete
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

    </v-btn>
  </div>

  <Post
    v-if="postMounted"
    :post="post"
  />

  <v-skeleton-loader v-else type="card" class="ma-4" />

  <v-divider/>

  <div
    class="d-flex justify-space-between align-center"
  >
    <h2
      class="text-h6 ma-4"
    >
      Comments
    </h2>
    <v-btn
      v-if="commentsMounted"
      color="primary"
      class="ma-4"
      prepend-icon="mdi-comment"
      @click="commentDialog = true"
    >
      New comment
    </v-btn>
  </div>
  <p
    class="text-body-1 ma-4"
    v-if="comments.length === 0 && commentsMounted"
  >
    There are no comments yet :(
  </p>


  <Comment
    v-if="commentsMounted"
    v-for="comment in comments" :key="comment.id"
    v-bind="comment"
    :id="comment.id"
    :content="comment.content"
    :timestamp="`${new Date(comment.created_at)}`"
    :author_id="comment.user.id"
    :author_username="comment.user.username"
    :author_name="comment.user.display_name"
    :author_avatar="comment.user.image_url"
    :votes="comment.votes.votes"
    :has_upvoted="comment.votes.has_upvoted"
    :has_downvoted="comment.votes.has_downvoted"
    :post="post"
    @refresh="refreshComments"
  />

  <v-skeleton-loader v-else type="card" class="ma-4" />

  <NewComment
    v-if="commentsMounted"
    title="Add a new comment"
    :post-id="post.id"
    :open="commentDialog"
    :post="post"
    @update:open="commentDialog = $event"
    @refresh="refreshComments"
  />

</template>

<style scoped>

</style>
