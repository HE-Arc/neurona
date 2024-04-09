<script setup>
import router from "@/router";
import {set_current_auth_state, state} from "@/Authentication/store";
import axios from "axios";
import routes from "@/api/routes";

axios.post(routes.authentication.logout, {}, {
  headers: {
    Authorization: sessionStorage.getItem('token')
  }
}).then(()=>{
  set_current_auth_state(false);
  sessionStorage.clear();
  router.push({name: 'login'});
}).catch(()=>{
  set_current_auth_state(false);
  sessionStorage.clear();
  router.push({name: 'login'});
});
</script>

<template>

</template>

<style scoped>

</style>
