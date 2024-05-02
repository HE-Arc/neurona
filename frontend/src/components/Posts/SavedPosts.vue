<script setup>

import Post from "@/components/Posts/Post.vue";
import {computed, onMounted, ref} from "vue";
import {usePostStore} from "@/stores/PostStore";

const store = usePostStore();

async function loadNext({ done }) {
    try{
      await store.fetchNextPostsSaved();
      if(store.reachedEndSaved){
        done('empty');
      } else {
        done('ok');
      }
    } catch (e) {
      console.error(e);
      done('error');
    }
}

</script>

<template>
  <v-infinite-scroll
    side="end"
    @load="loadNext"
  >
    <Post
      v-for="post in store.savedPosts" :key="post.id"
      v-bind="post"
      :post="post"
    />
  </v-infinite-scroll>

</template>

<style scoped>

</style>
