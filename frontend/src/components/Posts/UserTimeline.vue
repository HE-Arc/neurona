<script setup>
import Post from "@/components/Posts/Post.vue";
import { onMounted, ref } from "vue";
import ApiRequests from "@/api/ApiRequests";

const posts = ref([]);

const props = defineProps({
  username: String,
});

onMounted(() => {
  new ApiRequests().getUserPosts(props.username).then((response) => {
    response.sort((a, b) => {
      return new Date(b.created_at) - new Date(a.created_at);
    });
    posts.value = response;
  });
});
</script>

<template>
  <Post
    v-for="post in posts"
    :key="post.id"
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
    :image_urls="post.image_urls"
  />
</template>

<style scoped></style>
