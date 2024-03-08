<template>
  <v-card
    v-if="mounted"
    :title="post.title"
    :subtitle="'Posted in ' + post.space.title + ' on ' + new Date(post.created_at).toLocaleDateString()"
    :text="post.content"
    class="ma-4"
    :ripple="false"
    @click="open_post"
  >
    <v-card-text>
      {{ post.content }}
    </v-card-text>
    <v-card-actions>
      <!-- Placeholder for actions like upvote, downvote, comment, etc. -->
    </v-card-actions>
  </v-card>

  <v-skeleton-loader v-else type="card" class="mx-4"></v-skeleton-loader>
</template>

<script setup>
import { ref } from 'vue';
import router from '@/router';

const props = defineProps({
  post: Object,
});

const mounted = ref(true); 

function open_post() {
  router.push({ name: 'PostDetail', params: { postId: props.post.id } });
}
</script>

<style scoped>

</style>
