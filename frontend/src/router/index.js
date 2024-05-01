import {createRouter, createWebHistory} from "vue-router";

import Logout from "@/components/Authentication/Logout.vue";
import HomeView from "@/views/HomeView.vue";
import AboutView from "@/views/AboutView.vue";
import PostCreationView from "@/views/PostCreationView.vue";
import ProfileView from "@/views/ProfileView.vue";
import UserProfileView from "@/views/UserProfileView.vue";
import PostDetailsView from "@/views/PostDetailsView.vue";
import SpaceView from "@/views/SpaceView.vue";
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import SavedPostsView from "@/views/SavedPostsView.vue";
import SpacesListView from "@/views/SpacesListView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      meta: {
        title: "Home",
      },
    },
    {
      path: "/about",
      name: "about",
      component: AboutView,
      meta: {
        title: "About",
      },
    },
    {
      path: "/posts/create",
      name: "posts.create",
      component: PostCreationView,
      meta: {
        title: "New post",
      },
    },
    {
      path: "/profile",
      name: "profile",
      component: ProfileView,
      meta: {
        title: "Profile",
      },
    },
    {
      path: "/profile/:username",
      name: "profile.show",
      component: UserProfileView,
      props: true,
      meta: {
        title: "User profile",
      },
    },
    {
      path: "/posts/:id",
      name: "posts.show",
      component: PostDetailsView,
      props: true,
      meta: {
        title: "Post details",
      },
    },
    {
      path: "/spaces" ,
      name: "spaces",
      component: SpacesListView,
      meta: {
        title: "Spaces",
      },
    },
    {
      path: "/spaces/:id",
      name: "spaces.show",
      component: SpaceView,
      props: true,
      meta: {
        title: "Space",
      },
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
      meta: {
        title: "Login",
      },
    },
    {
      path: "/logout",
      name: "logout",
      component: Logout,
    },
    {
      path: "/register",
      name: "register",
      component: RegisterView,
      meta: {
        title: "Register",
      },
    },
    {
      path: "/saved",
      name: "saved",
      component: SavedPostsView,
      meta: {
        title: "Saved posts",
      },
    },
  ]
});

router.beforeEach((to, from, next) => {
  document.title = `Neurona | ${to.meta.title}` || 'Neurona';
  next();
});

export default router;
