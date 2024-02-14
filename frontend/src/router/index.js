import {createRouter, createWebHistory} from "vue-router";
import HelloWorld from "@/components/HelloWorld.vue";
import Test from "@/views/Test.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HelloWorld
    },
    {
      path: "/test",
      name: "test",
      component: Test
    },
  ]
});

export default router;
