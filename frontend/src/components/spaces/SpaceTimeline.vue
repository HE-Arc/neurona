<script setup lang="ts">

import Post from "@/components/Posts/Post.vue";
import {computed, onMounted, ref, watch} from 'vue';
import ApiRequests from "@/api/ApiRequests";
import MessageManager from "@/tools/MessageManager";
import EventBus from "@/tools/EventBus";
import router from "@/router";
import {useSpaceStore} from "@/stores/SpaceStore";

const spaceStore = useSpaceStore();
const quitDialog = ref(false);

const space = computed(() => spaceStore.getSpace(props.spaceId));
const posts = ref([]);
const req = new ApiRequests();

const props = defineProps<{
  spaceId: string,
}>();

onMounted(() => {
  spaceStore.fetchSpaceIfNecessary(props.spaceId);
});


function refreshPosts() {
  req.getPostsFromSpace(props.spaceId).then((response) => {
    response.sort((a, b) => {
      return new Date(b.created_at) - new Date(a.created_at);
    });
    posts.value = response;
  });
}

async function quitSpace() {
  await spaceStore.quitSpace(props.spaceId);
  quitDialog.value = false;
  EventBus.emit('refresh');
  MessageManager.getInstance().snackbar("You have quit the space");
}

async function joinSpace(){
  await spaceStore.joinSpace(props.spaceId);
  EventBus.emit('refresh');
  MessageManager.getInstance().snackbar("You have joined the space");
}

onMounted(() => {
  refreshPosts();
});

watch(() => props.spaceId, () => {
  refreshPosts();
});


</script>
<template>
  <div
  >
    <p
      class="text-h3 text-center ma-5"
    >
      {{ space?.name }}
    </p>

    <p
      class="text-body-2 text-center ma-5"
    >
      {{ space?.about }}
    </p>

    <v-btn
      class="ma-5"
      prepend-icon="mdi-account-minus"
      color="error"
      v-if="space?.joined"
      @click="quitDialog = true"
    >
      Quit
    </v-btn>
    <v-btn
      class="ma-5"
      prepend-icon="mdi-account-plus"
      color="primary"
      v-else
      @click="joinSpace"
    >
      Join
    </v-btn>

    <v-divider/>

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
      :is-saved="post.is_saved"
    />

    <v-dialog
      v-model="quitDialog"
      width="auto"
    >
      <v-card
        class="pa-1"
      >
        <v-card-title
        >
          Quit space
        </v-card-title>
        <v-card-text>
          Are you sure you want to quit the space
        </v-card-text>
        <v-spacer/>
        <v-card-actions
          class="d-flex justify-end"
        >
          <v-btn
            @click="quitDialog = false"
            prepend-icon="mdi-close"
          >
            Cancel
          </v-btn>
          <v-btn
            color="error"
            @click="quitSpace"
            prepend-icon="mdi-account-minus"
          >
            Quit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<style scoped>
</style>
