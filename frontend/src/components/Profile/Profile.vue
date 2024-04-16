<script setup>

import {useDisplay} from "vuetify";
import Post from "@/components/Posts/Post.vue";
import {onMounted, ref} from "vue";
import ApiRequests from "@/api/ApiRequests";

const is_mobile = useDisplay().smAndDown;
const mounted = ref(false);
const user = ref(null);

onMounted(() => {
  const req = new ApiRequests();
  (async () => {
    user.value = await req.getProfile();
    mounted.value = true;
  })();
});

</script>

<template>
  <div
      class="d-flex justify-center align-center my-10"
      v-if="mounted"
  >
    <v-avatar
        :image="user.image_url"
        :size="is_mobile ? 100 : 150"
    >
    </v-avatar>

    <div
        class="d-flex flex-column justify-center align-center"
    >
      <h1 class="mx-12 text-h5 text-sm-h5 text-md-h4 text-lg-h2 text-xl-h2">
        {{user.display_name}}
      </h1>

      <h2 class="text-body-1 text-md-h6 text-lg-h5 text-xl-h5 text-grey-darken-1">
        @{{user.username}}
      </h2>
    </div>
  </div>

  <div
      class="d-flex justify-center align-center my-16"
  >

    <v-btn
        class="mx-6"
        color="primary"
        prepend-icon="mdi-account-edit"
    >
      Edit profile
    </v-btn>

    <v-btn
        class="mx-6"
        color="primary"
        prepend-icon="mdi-logout"
        :to="{name: 'logout'}"
    >
      Log out
    </v-btn>

  </div>

</template>

<style scoped>

</style>
