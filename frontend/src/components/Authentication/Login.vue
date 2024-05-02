<script setup>

import {onMounted, ref} from "vue";
import {login as passkeyLogin} from "@/Authentication/Passkey";
import router from "@/router";
import MessageManager from "@/tools/MessageManager";
import { useSpaceStore } from "@/stores/SpaceStore";
import { usePostStore } from "@/stores/PostStore";
import {useUserStore} from "@/stores/UserStore";

const spaceStore = useSpaceStore();
const postStore = usePostStore();
const userStore = useUserStore();

const username = ref('');

const messages = MessageManager.getInstance();

onMounted(()=>{
  if(userStore.isLoggedIn){
    router.push({name: 'home'});
  }
});

async function login(){
  messages.value = [];
  passkeyLogin(username.value).then((r)=>{
    messages.add('success', 'Logged in successfully');
    const token = r.data.token.key;
    const user = r.data.user;

    userStore.login(user, token);

    spaceStore.fetchSpaces();
    postStore.fetchPosts();
    router.push({name: 'home'})
  }).catch((e)=>{
    if (e.isAxiosError){
      if(e.response.status >= 400 && e.response.status < 500){
        messages.add('warning', e.response.data.message);
      } else {
        messages.add('error', 'An unexpected error occurred while trying to log in');
      }
    } else {
      messages.add('warning', e.message);
    }
  });
}

function recover(){
  messages.add('warning', 'This feature is not yet implemented. Contact the administrator for help.');
}

</script>

<template>

  <v-form
    class="d-flex justify-center align-center"
    @submit.prevent="login"
  >
    <v-container fill-height>
      <v-row
        justify="center"
        align="center"
      >
        <v-col cols="12" md="10" lg="8">
          <v-sheet
            elevation="4"
            rounded
            class="ma-2 pa-5"
          >
            <h2
              class="text-h6 mb-5 mx-2"
            >
              Login
            </h2>

            <p
              class="text-body-1 mx-2 mb-5"
            >
              Sign in to Neurona using your passkey.
            </p>

            <v-text-field
              v-model="username"
              label="Username"
              required
            />

            <v-spacer/>

            <v-container>
              <v-row>
                <v-col cols="12" sm="6">
                  <v-btn
                    @click="() => $router.push('/register')"
                    prepend-icon="mdi-account-plus"
                    class="mt-2 mb-2 mx-2"
                    block
                  >
                    Register
                  </v-btn>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-btn
                    color="primary"
                    @click="login"
                    prepend-icon="mdi-account-key"
                    class="mt-2 mb-2 mx-2"
                    block
                  >
                    Sign in with passkey
                  </v-btn>
                </v-col>

              </v-row>
            </v-container>
            <v-divider class="my-5"/>

            <p
              class="text-body-2 ma-2"
            >
              Don't have access to your passkey?
              <a
                href="#"
                @click="recover"
                class="text-grey-darken-2"
              >
                Use a recovery code instead
              </a>
            </p>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<style scoped>

</style>
