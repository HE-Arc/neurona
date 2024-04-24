<script setup>

import {useDisplay} from "vuetify";
import {onMounted, ref} from "vue";
import ApiRequests from "@/api/ApiRequests";
import EventBus from "@/tools/EventBus";
import UserTimeline from "@/components/Posts/UserTimeline.vue";
import UserHeader from "@/components/Profile/components/UserHeader.vue";
import UserSettings from "@/components/Profile/components/UserSettings.vue";
import UserNotFound from "@/components/Profile/components/UserNotFound.vue";
import ReturnBtn from "@/components/ReturnBtn.vue";

const props = defineProps({
  username: String,
});

const mounted = ref(false);
const not_found = ref(false);
const user = ref(null);

const req = new ApiRequests();

async function refresh() {
  try {
    user.value = await req.getProfileFromUsername(props.username);
  } catch (e) {
    not_found.value = true;
  }
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
  <ReturnBtn/>

  <UserNotFound
    v-if="not_found"
    :username="username"
  />

  <UserHeader
    v-if="mounted"
    :username="user.username"
    :display-name="user.display_name"
    :image-url="user.image_url"
    :about="user.about"
  />

  <v-skeleton-loader
    v-else-if="!not_found"
    type="card"
    class="ma-4"
  />

  <UserTimeline
    v-if="mounted"
    :username="user.username"
  />

  <v-skeleton-loader
    v-else-if="!not_found"
    v-for="_ in 5"
    type="card"
    class="ma-4"
  />

</template>

<style scoped>

</style>
