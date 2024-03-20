<script setup>

import Post from "@/components/Post.vue";
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
    posts.value = response.data;
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
    :timestamp="post.timestamp"
    :author_id="post.user.id"
    :author_username="post.user.username"
    :author_name="post.user.display_name"
    :author_avatar="post.user.avatar"
  />
</template>

<style scoped>

</style>
