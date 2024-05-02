<script setup>

import {onMounted, ref} from "vue";
import ApiRequests from "@/api/ApiRequests";
import EventBus from "@/tools/EventBus";
import UserTimeline from "@/components/Posts/UserTimeline.vue";
import UserHeader from "@/components/Profile/components/UserHeader.vue";
import UserSettings from "@/components/Profile/components/UserSettings.vue";
import {useUserStore} from "@/stores/UserStore";

const store = useUserStore();
store.fetch();

const mounted = ref(false);
const user = ref(null);

const req = new ApiRequests();

async function refresh(){
  user.value = await req.getProfile();
}

onMounted(() => {
  (async () => {
    await refresh();
    mounted.value = true;
    EventBus.on('refresh', refresh);
  })();
});

</script>

<template>

  <UserHeader
    v-if="mounted"
    :username="store.user.username"
    :display-name="store.user.display_name"
    :image-url="store.user.image_url"
    :about="store.user.about"
  />

  <UserSettings
    v-if="mounted"
    :username="user.username"
    :display-name="user.display_name"
    :about="user.about"
  />

  <v-skeleton-loader
    v-else
    type="card"
    class="ma-4"
  />

  <UserTimeline
    v-if="mounted"
    :username="store.user.username"
  />

  <v-skeleton-loader
    v-else
    v-for="_ in 5"
    type="card"
    class="ma-4"
  />

</template>

<style scoped>

</style>
