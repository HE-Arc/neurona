<script setup>

import Post from "@/components/Posts/Post.vue";
import {computed, onMounted, ref} from "vue";
import ApiRequests from "@/api/ApiRequests";

const posts = ref([]);

const req = new ApiRequests();

onMounted(() => {
  (async () => {
    const response = await req.getPosts();
    response.sort((a, b) => {
      return new Date(b.created_at) - new Date(a.created_at);
    });
    posts.value = response;
  })();
});

</script>

<template>
  <Post
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
  />
</template>

<style scoped>

</style>
