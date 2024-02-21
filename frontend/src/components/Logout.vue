<script setup>
import router from "@/router";
import {set_current_auth_state, state} from "@/Authentication/store";

state.authenticated = false;
set_current_auth_state('false');
router.push({name: 'login'});
</script>

<template>

</template>

<style scoped>

</style>
