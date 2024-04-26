<script setup >

import Post from "@/components/Posts/Post.vue";
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { usePostStore } from '@/stores/PostStore';

const route = useRoute();
const postStore = usePostStore();

const spaceId = computed(() => Number(route.params.id));
const posts = computed(() => postStore.getPostsBySpaceId(spaceId.value));

</script>
<template>
  <Post
    v-if="posts.length" :posts="posts"
    v-for="post in posts.reverse()" :key="post.id"
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
</template>

<style scoped>
</style>
