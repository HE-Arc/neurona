<script setup>
import router from "@/router";
import store from "@/Authentication/store";

axios.post(routes.authentication.logout, {}, {
  headers: {
    Authorization: sessionStorage.getItem('token')
  }
}).then(()=>{
  store.commit('logout');
  router.push({name: 'login'});
}).catch(()=>{
  store.commit('logout');
  router.push({name: 'login'});
});
</script>

<template>

</template>

<style scoped>

</style>
