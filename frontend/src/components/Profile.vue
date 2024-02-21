<script setup>

import {useDisplay} from "vuetify";
import Post from "@/components/Post.vue";

const is_mobile = useDisplay().smAndDown;

</script>

<template>
  <div
      class="d-flex justify-center align-center my-10"
  >
    <v-avatar
        image="https://nzbirdsonline.org.nz/sites/all/files/2X2A1697%20King%20Penguin%20bol.jpg"
        :size="is_mobile ? 100 : 150"
    >
    </v-avatar>

    <div
        class="d-flex flex-column justify-center align-center"
    >
      <h1 class="mx-12 text-h5 text-sm-h5 text-md-h4 text-lg-h2 text-xl-h2">
        John Doe
      </h1>

      <h2 class="text-body-1 text-md-h6 text-lg-h5 text-xl-h5 text-grey-darken-1">
        @kingpenguin
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


  <Post :id="5" />
  <Post :id="5" />
  <Post :id="5" />
  <Post :id="5" />
  <Post :id="5" />


</template>

<style scoped>

</style>
