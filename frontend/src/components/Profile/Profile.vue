<script setup>

import {useDisplay} from "vuetify";
import Post from "@/components/Posts/Post.vue";
import {onMounted, ref} from "vue";
import ApiRequests from "@/api/ApiRequests";
import MessageManager from "@/tools/MessageManager";
import EditProperty from "@/components/Profile/EditProperty.vue";
import EventBus from "@/tools/EventBus";

const is_mobile = useDisplay().smAndDown;
const mounted = ref(false);
const user = ref(null);

const usernameDialog = ref(false);
const displayNameDialog = ref(false);

onMounted(() => {
  const req = new ApiRequests();
  (async () => {
    user.value = await req.getProfile();
    mounted.value = true;
  })();
});

function editUsername() {
  usernameDialog.value = true;
}

function editDisplayName() {
  displayNameDialog.value = true;
}

function editImage() {
  MessageManager.getInstance().add('warning', 'You cannot edit your profile image yet.');
}

function formSubmit() {
  console.log('submit');
}

function refreshUsername(username){
  user.value.username = username;
  EventBus.emit('refresh');
}

function refreshDisplayName(display_name){
  user.value.display_name = display_name;
  EventBus.emit('refresh');
}

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
    <div class="align-self-end">
      <v-btn
        icon
        size="x-small"
        @click="editImage"
      >
        <v-icon>mdi-pencil</v-icon>
      </v-btn>
    </div>

    <div
      class="d-flex flex-column justify-center align-center"
    >
      <h1 class="mx-12 text-h5 text-sm-h5 text-md-h4 text-lg-h2 text-xl-h2">
        {{ user.display_name }}
      </h1>

      <h2 class="text-body-1 text-md-h6 text-lg-h5 text-xl-h5 text-grey-darken-1">
        @{{ user.username }}
      </h2>
    </div>
  </div>

  <v-container>
    <v-row class="flex-column flex-sm-row justify-center">
      <v-col cols="12" sm="4" class="d-flex justify-center">
        <v-btn
          class="ma-2"
          color="primary"
          width="200px"
          prepend-icon="mdi-account-edit"
          @click="editDisplayName"
        >
          Edit name
        </v-btn>
      </v-col>

      <v-col cols="12" sm="4" class="d-flex justify-center">
        <v-btn
          class="ma-2"
          color="primary"
          width="200px"
          prepend-icon="mdi-account-edit"
          @click="editUsername"
        >
          Edit username
        </v-btn>
      </v-col>

      <v-col cols="12" sm="4" class="d-flex justify-center">
        <v-btn
          class="ma-2"
          color="error"
          width="200px"
          prepend-icon="mdi-account-remove"
          @click="editDisplayName"
        >
          Delete account
        </v-btn>
      </v-col>
    </v-row>
  </v-container>

  <EditProperty
    v-if="mounted"
    name="username"
    attribute_name="username"
    :value="user.username"
    :open="usernameDialog"
    @update:open="usernameDialog = $event"
    @refresh="refreshUsername"
  />

  <EditProperty
    v-if="mounted"
    name="Name"
    attribute_name="display_name"
    :value="user.display_name"
    :open="displayNameDialog"
    @update:open="displayNameDialog = $event"
    @refresh="refreshDisplayName"
  />

</template>

<style scoped>

</style>
