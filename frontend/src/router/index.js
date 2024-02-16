import {createRouter, createWebHistory} from "vue-router";
import HelloWorld from "@/components/HelloWorld.vue";
import Test from "@/views/Test.vue";
import Timeline from "@/components/Timeline.vue";
import PostWriting from "@/components/PostWriting.vue";
import Profile from "@/components/Profile.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: Timeline,
            meta: {
                title: "Neurona",
            },
        },
        {
            path: "/test",
            name: "test",
            component: Test,
            meta: {
                title: "Test",
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
    ]
});

export default router;
