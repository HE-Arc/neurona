<template>
  <!-- Your template for listing posts -->
</template>

<script>
import ApiService from '@/services/api';

export default {
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
