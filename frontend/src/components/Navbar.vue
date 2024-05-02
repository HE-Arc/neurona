<script setup>

import {computed, onMounted, reactive, ref, unref} from 'vue';
import {useDisplay} from 'vuetify';
import ApiRequests from "@/api/ApiRequests";
import EventBus from "@/tools/EventBus";
import {useSpaceStore} from "@/stores/SpaceStore";
import {useUserStore} from "@/stores/UserStore";

const userStore = useUserStore();
userStore.fetch();

const spaceStore = useSpaceStore();

const authenticated = computed(() => userStore.isLoggedIn);

const user = ref(null);
const mounted = ref(false);
const drawer = ref(false);
const items = [
  {title: 'Home', icon: 'mdi-home', to: {name: 'home'}},
  {title: 'Saved', icon: 'mdi-bookmark', to: {name: 'saved'}},
  {title: 'Spaces', icon: 'mdi-folder', to: {name: 'spaces'}},
];

const bottom_items = [
  {title: 'About us', icon: 'mdi-information', to: {name: 'about'}},
]

const logout_route = {title: 'Log out', icon: 'mdi-logout', to: {name: 'logout'}};
const login_route = {title: 'Login', icon: 'mdi-login', to: {name: 'login'}};

spaceStore.fetchSpaces();
const spaces = computed(() => spaceStore.joinedSpaces);

const is_mobile = useDisplay().smAndDown;

drawer.value = !is_mobile.value;

function mount() {
  if (!authenticated.value) {
    return;
  }
  spaceStore.fetchSpaces();
  const req = new ApiRequests();
  (async () => {
    user.value = await req.getProfile();
    mounted.value = true;
  })();
  EventBus.on('refresh', refresh);
}

onMounted(() => {
  mount();
});

function refresh() {
  mounted.value = false;
  mount();
}

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

    <v-tooltip v-if="authenticated" text="Create a new post" location="bottom">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" icon="mdi-plus-thick" :to="{name: 'posts.create'}"/>
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
      <v-list-item v-if="authenticated && mounted" to="/profile" value="profile">
        <template v-slot:prepend>
          <v-avatar :image="userStore.user?.image_url"></v-avatar>
        </template>
        <v-list-item-title>{{ userStore.user?.display_name }}</v-list-item-title>
        <v-list-item-subtitle>@{{ userStore.user?.username }}</v-list-item-subtitle>
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
        :to="'/spaces/' + item.id"
        :key="index"
        :value="item.id"
        :prepend-avatar="item.avatar"
        nav>
        <v-list-item-title>{{ item.name }}</v-list-item-title>
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
