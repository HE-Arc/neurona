<script setup>

import Post from "@/components/Posts/Post.vue";
import {computed, onMounted, ref} from "vue";
import ApiRequests from "@/api/ApiRequests";
import {usePostStore} from "@/stores/PostStore";

const posts = ref([]);

const store = usePostStore();
store.fetchNextPostsHome();


async function loadNext({ done }) {
  try{
    await store.fetchNextPostsHome();

    if(store.reachedEndHome){
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
    <div>
      <template
        v-for="post in store.homePosts"
        :key=post.id
      >
        <Post
          v-bind="post"
          :post="post"
        />
      </template>
    </div>
  </v-infinite-scroll>

</template>

<style scoped>

</style>
