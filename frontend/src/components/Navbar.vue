<script setup>

import {computed, onMounted, ref} from 'vue';
import {useDisplay} from 'vuetify';
import ApiRequests from "@/api/ApiRequests";
import store from "@/Authentication/store";

store.subscribe((mutation) => {
  if(mutation.type === 'login') {
    user.value = null;
    mounted.value = false;
    if(store.state.authenticated) {
      (async () => {
        user.value = await new ApiRequests().getProfile();
        mounted.value = true;
      })();
    }
  }
});

const authenticated = computed(() => store.state.authenticated);

const user = ref(null);
const mounted = ref(false);
const drawer = ref(false);
const items = [
  {title: 'Home', icon: 'mdi-home', to: {name: 'home'}},
  {title: 'Saved', icon: 'mdi-bookmark', to: {name: 'saved'}},
];

const bottom_items = [
  {title: 'Settings', icon: 'mdi-cog', to: {name: 'settings'}},
  {title: 'About us', icon: 'mdi-information', to: {name: 'about'}},
]

const logout_route = {title: 'Log out', icon: 'mdi-logout', to: {name: 'logout'}};
const login_route = {title: 'Login', icon: 'mdi-login', to: {name: 'login'}};

const spaces = [
  //{title: 'ISC1', avatar: 'mdi-account', id: 1, to: 'spaces/1'},
  //{title: 'ISC2', avatar: 'mdi-account', id: 2, to: 'spaces/2'},
]

const is_mobile = useDisplay().smAndDown;

drawer.value = !is_mobile.value;

onMounted(() => {
  if(!authenticated.value) {
    return;
  }
  const req = new ApiRequests();
  (async () => {
    user.value = await req.getProfile();
    mounted.value = true;
  })();
});

</script>

<template>
  <!-- <v-system-bar color="deep-purple darken-3"></v-system-bar> -->

  <v-app-bar
      color="primary"
      prominent
      app
  >
    <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

    <v-toolbar-title>
      {{ $route.meta.title }}
    </v-toolbar-title>

    <v-spacer></v-spacer>

    <v-btn v-if="authenticated" variant="text" icon="mdi-magnify"></v-btn>

    <v-tooltip v-if="authenticated" text="Create a new post" location="bottom">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" icon="mdi-pencil" :to="{name: 'posts.create'}"/>
      </template>
    </v-tooltip>

  </v-app-bar>

  <v-navigation-drawer
      v-model="drawer"
      app
      :permanent="!is_mobile"
      :temporary="is_mobile"
  >
    <v-list nav>
      <v-list-item v-if="authenticated && mounted"  to="/profile" value="profile">
        <template v-slot:prepend>
          <v-avatar :image="user.image_url"></v-avatar>
        </template>
        <v-list-item-title>{{user.display_name}}</v-list-item-title>
        <v-list-item-subtitle>@{{user.username}}</v-list-item-subtitle>
      </v-list-item>

      <v-divider v-if="authenticated"/>

      <v-list-item
          v-if="authenticated"
          v-for="(item, index) in items"
          :key="index"
          :value="item"
          :to="item.to"
      >
        <template v-slot:prepend>
          <v-icon>{{ item.icon }}</v-icon>
        </template>
        <v-list-item-title>{{ item.title }}</v-list-item-title>
      </v-list-item>

      <v-divider v-if="authenticated"/>

      <v-list-item
          v-if="authenticated"
          v-for="(item, index) in spaces"
          :to="item.to"
          :key="index"
          :value="item.id"
          :prepend-avatar="item.avatar"
          nav>
        <v-list-item-title>{{ item.title }}</v-list-item-title>
      </v-list-item>

      <v-divider v-if="authenticated"/>

      <v-list-item
        v-if="!authenticated"
        :value="login_route"
        :to="login_route.to"
      >
        <template v-slot:prepend>
          <v-icon>{{ login_route.icon }}</v-icon>
        </template>
        <v-list-item-title>{{ login_route.title }}</v-list-item-title>
      </v-list-item>

      <v-divider v-if="!authenticated"/>

      <v-list-item
          v-for="(item, index) in bottom_items"
          :key="index"
          :value="item"
          :to="item.to">
        <template v-slot:prepend>
          <v-icon>{{ item.icon }}</v-icon>
        </template>
        <v-list-item-title>{{ item.title }}</v-list-item-title>
      </v-list-item>
      <v-list-item
        v-if="authenticated"
        :value="logout_route"
        :to="logout_route.to"
        >
        <template v-slot:prepend>
          <v-icon>{{ logout_route.icon }}</v-icon>
        </template>
        <v-list-item-title>{{ logout_route.title }}</v-list-item-title>
      </v-list-item>

    </v-list>
  </v-navigation-drawer>
</template>

<style scoped>

</style>
