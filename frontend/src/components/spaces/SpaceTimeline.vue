<script setup lang="ts">

import Post from "@/components/Posts/Post.vue";
import {computed, onMounted, ref, watch} from 'vue';
import ApiRequests from "@/api/ApiRequests";
import MessageManager from "@/tools/MessageManager";
import EventBus from "@/tools/EventBus";
import router from "@/router";
import {useSpaceStore} from "@/stores/SpaceStore";
import {usePostStore} from "@/stores/PostStore";

const spaceStore = useSpaceStore();
const postStore = usePostStore();

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

watch(() => props.spaceId, () => {
  if(!postStore.spacePosts[props.spaceId]){
    postStore.fetchNextPostsSpace(props.spaceId);
  }
});


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

async function loadNext({ done }) {
  try{
    await postStore.fetchNextPostsSpace(props.spaceId);
    if(postStore.reachedEndSpace){
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

    <v-infinite-scroll
      side="end"
      @load="loadNext"
    >
      <Post
          v-for="post in postStore.spacePosts[props.spaceId]" :key="post.id"
          v-bind="post"
          :post="post"
      />
    </v-infinite-scroll>


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
