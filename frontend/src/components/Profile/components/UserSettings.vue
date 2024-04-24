<script setup>
import MessageManager from "@/tools/MessageManager";
import EventBus from "@/tools/EventBus";
import store from "@/Authentication/store";
import router from "@/router";
import {ref} from "vue";
import EditProperty from "@/components/Profile/EditProperty.vue";
import ConfirmationDialog from "@/components/Profile/ConfirmationDialog.vue";

const usernameDialog = ref(false);
const displayNameDialog = ref(false);
const aboutDialog = ref(false);
const deleteDialog = ref(false);

function editImage() {
  MessageManager.getInstance().add('warning', 'You cannot edit your profile image yet.');
}

function refreshUsername(username) {
  user.value.username = username;
  EventBus.emit('refresh');
}

function refreshDisplayName(display_name) {
  EventBus.emit('refresh');
  (async () => {
    user.value = await req.getProfile();
  })();
}

function refreshAbout(about) {
  user.value.about = about;
}

function deleteAccount() {
  req.deleteAccount().then(() => {
    MessageManager.getInstance().add('info', 'Your account has been deleted. We are sorry to see you go but we hope to see you again soon :)');
    store.commit('logout');
    router.push({name: 'register'})
  });
}

</script>

<template>

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
          prepend-icon="mdi-text-account"
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
          @click="deleteDialog = true"
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

  <ConfirmationDialog
    v-if="mounted"
    header="DANGER ZONE"
    message="Are you sure you want to delete your account? This action cannot be undone. All your data will be lost. There is no way to recover your account. Are you sure you want to proceed?"
    confirm-label="Yes, delete my account"
    confirm-icon="mdi-alert"
    :open="deleteDialog"
    @update:open="deleteDialog = $event"
    @confirm="deleteAccount"
  />
</template>

<style scoped>

</style>
