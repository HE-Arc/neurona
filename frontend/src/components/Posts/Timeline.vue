<script setup>

import Post from "@/components/Posts/Post.vue";
import {onMounted, ref} from "vue";
import axios from "axios";
import routes from "@/api/routes";
import router from "@/router";

const posts = ref([]);

onMounted(() => {
  console.log(sessionStorage.getItem('token'));
  axios.get(routes.posts.show, {
    headers: {
      Authorization: sessionStorage.getItem('token')
    }
  }).then((response) => {
    const all_posts = response.data;
    console.log(all_posts);
    all_posts.sort((a, b) => {
      return new Date(b.created_at) - new Date(a.created_at);
    });
    posts.value = all_posts;
  }).catch((e) => {
    sessionStorage.clear();
    router.push({name: "login"});
  });
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
