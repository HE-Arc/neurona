<script setup>
import router from "@/router";
import store from "@/Authentication/store";
import ApiRequests from "@/api/ApiRequests";
import MessageManager from "@/tools/MessageManager";

function logout() {
  store.commit('logout');
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
