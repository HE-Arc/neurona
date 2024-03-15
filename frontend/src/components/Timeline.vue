<template>
  <div>
    <!-- Iterate over posts and pass post data to the Post component -->
    <Post 
      v-for="post in posts" 
      :key="post.id" 
      :post="post" 
    />
  </div>
</template>

<script>
import ApiService from '@/services/api';
import Post from "@/components/Post.vue";

export default {
  components: {
    Post,
  },
  data() {
    return {
      posts: [],
    };
  },
  async created() {
    try {
      const response = await ApiService.getPosts();
      this.posts = response.data;
    } catch (error) {
      console.error("There was an error fetching the posts:", error);
    }
  },
};
</script>
