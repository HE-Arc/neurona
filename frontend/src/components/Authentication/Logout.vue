<script setup>
import router from "@/router";
import ApiRequests from "@/api/ApiRequests";
import MessageManager from "@/tools/MessageManager";
import {useUserStore} from "@/stores/UserStore";

const userStore = useUserStore();

function logout() {
  userStore.logout();

  router.push({name: 'login'});
  MessageManager.getInstance().add('success', 'Logged out successfully');
}

new ApiRequests().logout()
  .then(() => {
    logout();
  })
  .catch(() => {
    logout();
  });
</script>

<template>

</template>

<style scoped>

</style>
