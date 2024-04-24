import {createRouter, createWebHistory} from "vue-router";
import HelloWorld from "@/components/HelloWorld.vue";
import Test from "@/views/Test.vue";
import Timeline from "@/components/Posts/Timeline.vue";
import PostWriting from "@/components/Posts/PostWriting.vue";
import Profile from "@/components/Profile/Profile.vue";
import PostDetails from "@/components/Posts/PostDetails.vue";
import Login from "@/components/Authentication/Login.vue";
import Logout from "@/components/Authentication/Logout.vue";
import Register from "@/components/Authentication/Register.vue";
import SavedPosts from "@/components/Posts/SavedPosts.vue";
import UserProfile from "@/components/Profile/UserProfile.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: Timeline,
      meta: {
        title: "Home",
      },
    },
    {
      path: "/about",
      name: "about",
      component: HelloWorld,
      meta: {
        title: "About",
      },
    },
    {
      path: "/posts/create",
      name: "posts.create",
      component: PostWriting,
      meta: {
        title: "New post",
      },
    },
    {
      path: "/profile",
      name: "profile",
      component: Profile,
      meta: {
        title: "Profile",
      },
    },
    {
      path: "/profile/:username",
      name: "profile.show",
      component: UserProfile,
      props: true,
      meta: {
        title: "User profile",
      },
    },
    {
      path: "/posts/:id",
      name: "posts.show",
      component: PostDetails,
      props: true,
      meta: {
        title: "Post details",
      },
    },
    {
      path: "/login",
      name: "login",
      component: Login,
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
      component: Register,
      meta: {
        title: "Register",
      },
    },
    {
      path: "/saved",
      name: "saved",
      component: SavedPosts,
      meta: {
        title: "Saved posts",
      },
    },
    {
      path: "/settings",
      name: "settings",
      component: HelloWorld,
      meta: {
        title: "Settings",
      },
    }

  ]
});

router.beforeEach((to, from, next) => {
  document.title = `Neurona | ${to.meta.title}` || 'Neurona';
  next();
});

export default router;
