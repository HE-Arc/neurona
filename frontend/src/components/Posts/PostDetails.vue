<script setup>

import Post from "@/components/Posts/Post.vue";
import ReturnBtn from "@/components/ReturnBtn.vue";
import {onMounted, ref} from "vue";
import ApiRequests from "@/api/ApiRequests";
import MessageManager from "@/tools/MessageManager";
import router from "@/router";
import NewComment from "@/components/Posts/NewComment.vue";

const props = defineProps({
  id: String,
})

const removeDialog = ref(false);
const commentDialog = ref(false);
const post = ref(null);
const comments = ref([]);
const mounted = ref(false);
const is_author = ref(false);

const req = new ApiRequests();

onMounted(() => {
  (async () => {
    window.scrollTo(0, 0);
    post.value = await req.getPost(props.id);

    const username = (await req.getProfile()).username;
    is_author.value = post.value.user.username === username;

    const comments = (await req.getComments(props.id));
    console.log(comments);

    mounted.value = true;
  })();
});

function deletePost() {
  req.deletePost(post.value.id).then(() => {
    MessageManager.getInstance().snackbar('Post deleted successfully.', 5000);
    router.push({name: 'home'});
  });
}

function refreshComments(){
  console.log('Refreshing comments');
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
    v-if="mounted"
    :id="post.id"
    :title="post.title"
    :content="post.content"
    :timestamp="`${new Date(post.created_at)}`"
    :author_id="post.user.id"
    :author_username="post.user.username"
    :author_name="post.user.display_name"
    :author_avatar="post.user.image_url"
    :comments="post.votes_and_comments.comments"
    :votes="post.votes_and_comments.votes"
    :has_upvoted="post.votes_and_comments.has_upvoted"
    :has_downvoted="post.votes_and_comments.has_downvoted"
  />

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
      color="primary"
      class="ma-4"
      prepend-icon="mdi-comment"
      @click="commentDialog = true"
    >
      Add comment
    </v-btn>
  </div>
  <p
    class="text-body-1 ma-4"
  >
    There are no comments yet :(
  </p>


  <NewComment
    v-if="mounted"
    title="Add a new comment"
    :post-id="post.id"
    :open="commentDialog"
    @update:open="commentDialog = $event"
    @refresh="refreshComments"
  />

</template>

<style scoped>

</style>
