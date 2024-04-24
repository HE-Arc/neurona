<script setup>

import {onMounted, ref} from "vue";
import ApiRequests from "@/api/ApiRequests";
import {useDisplay} from "vuetify";
import EventBus from "@/tools/EventBus";

const props = defineProps({
  username: String,
  displayName: String,
  about: String,
  imageUrl: String,
});

const is_mobile = useDisplay().smAndDown;

</script>

<template>
    <div
      class="d-flex justify-center align-center my-10"
    >
      <v-avatar
        :image="imageUrl"
        :size="is_mobile ? 100 : 150"
      >
      </v-avatar>

      <div
        class="d-flex flex-column justify-center align-center"
      >
        <h1 class="mx-12 text-h5 text-sm-h5 text-md-h4 text-lg-h2 text-xl-h2">
          {{ displayName }}
        </h1>

        <h2 class="text-body-1 text-md-h6 text-lg-h5 text-xl-h5 text-grey-darken-1">
          @{{ username }}
        </h2>
      </div>
    </div>

    <div
      class="d-flex justify-center align-center my-10"
    >
      <p
        class="text-body-1"
      >
        {{ about }}
      </p>
    </div>
</template>

<style scoped>

</style>
