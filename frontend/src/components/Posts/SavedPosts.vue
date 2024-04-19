<script setup>

import Post from "@/components/Posts/Post.vue";
import {computed, onMounted, ref} from "vue";
import ApiRequests from "@/api/ApiRequests";

const posts = ref([]);
const mounted = ref(false);

const req = new ApiRequests();

onMounted(() => {
  (async () => {
    const response = await req.getSavedPosts();
    response.sort((a, b) => {
      return new Date(b.created_at) - new Date(a.created_at);
    });
    posts.value = response;
    mounted.value = true;
  })();
});

</script>

<template>
  <Post
    v-if="mounted"
    v-for="post in posts" :key="post.id"
    v-bind="post"
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
    :is-saved="post.is_saved"
  />

  <v-skeleton-loader
    v-else
    v-for="i in 5"
    type="card"
    class="ma-4"
  />
</template>

<style scoped>

</style>
