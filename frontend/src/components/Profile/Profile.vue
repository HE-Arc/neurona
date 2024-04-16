<script setup>

import {useDisplay} from "vuetify";
import {onMounted, ref} from "vue";
import ApiRequests from "@/api/ApiRequests";
import MessageManager from "@/tools/MessageManager";
import EditProperty from "@/components/Profile/EditProperty.vue";
import EventBus from "@/tools/EventBus";
import store from "@/Authentication/store";
import router from "@/router";

const is_mobile = useDisplay().smAndDown;
const mounted = ref(false);
const user = ref(null);

const usernameDialog = ref(false);
const displayNameDialog = ref(false);
const aboutDialog = ref(false);

onMounted(() => {
  const req = new ApiRequests();
  (async () => {
    try{
      user.value = await req.getProfile();
      mounted.value = true;
    } catch (e) {
      store.commit('logout');
      await router.push({name: "login"});
    }
  })();
});

function editImage() {
  MessageManager.getInstance().add('warning', 'You cannot edit your profile image yet.');
}

function refreshUsername(username){
  user.value.username = username;
  EventBus.emit('refresh');
}

function refreshDisplayName(display_name){
  EventBus.emit('refresh');
  (async () => {
    const req = new ApiRequests();
    user.value = await req.getProfile();
  })();
}

function refreshAbout(about){
  user.value.about = about;
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

  <div
    class="d-flex justify-center align-center my-10"
    v-if="mounted"
  >
    <p
      class="text-body-1"
    >
      {{ user.about }}
    </p>
  </div>

  <v-container>
    <v-row class="flex-column flex-sm-row justify-center">
      <v-col cols="12" sm="3" class="d-flex justify-center">
        <v-btn
          class="ma-1 px-2"
          color="primary"
          width="250px"
          prepend-icon="mdi-account-edit"
          @click="displayNameDialog = true"
        >
          Edit name
        </v-btn>
      </v-col>

      <v-col cols="12" sm="3" class="d-flex justify-center">
        <v-btn
          class="ma-1 px-2"
          color="primary"
          width="250px"
          prepend-icon="mdi-account-edit"
          @click="usernameDialog = true"
        >
          Edit username
        </v-btn>
      </v-col>


      <v-col cols="12" sm="3" class="d-flex justify-center">
        <v-btn
          class="ma-1 px-2"
          color="primary"
          width="250px"
          prepend-icon="mdi-account-edit"
          @click="aboutDialog = true"
        >
          Edit about
        </v-btn>
      </v-col>

      <v-col cols="12" sm="3" class="d-flex justify-center">
        <v-btn
          class="ma-1 px-2"
          color="error"
          width="250px"
          prepend-icon="mdi-account-remove"
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
    :area="false"
    @update:open="usernameDialog = $event"
    @refresh="refreshUsername"
  />

  <EditProperty
    v-if="mounted"
    name="name"
    attribute_name="display_name"
    :value="user.display_name"
    :open="displayNameDialog"
    :area="false"
    @update:open="displayNameDialog = $event"
    @refresh="refreshDisplayName"
  />

  <EditProperty
    v-if="mounted"
    name="about"
    attribute_name="about"
    :value="user.about"
    :open="aboutDialog"
    :area="true"
    @update:open="aboutDialog = $event"
    @refresh="refreshAbout"
  />


</template>

<style scoped>

</style>
