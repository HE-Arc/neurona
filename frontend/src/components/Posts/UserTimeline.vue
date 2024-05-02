<script setup>

import Post from "@/components/Posts/Post.vue";
import {onMounted, ref} from "vue";
import {usePostStore} from "@/stores/PostStore";

const postStore = usePostStore();

const props = defineProps({
  username: String,
})

async function loadNext({done}) {
  try {
    await postStore.fetchNextPostsUser(props.username);
    if(postStore.reachedEndUser[props.username]){
      done('empty');
    } else {
      done('ok');
    }
  } catch (e) {
    done('error');
    console.error(e);
  }
}
</script>

<template>
  <v-infinite-scroll
    side="end"
    @load="loadNext"
  >
    <Post
      v-for="post in postStore.userPosts[props.username]" :key="post.id"
      v-bind="post"
      :post="post"
    />
  </v-infinite-scroll>

</template>

<style scoped>

</style>
