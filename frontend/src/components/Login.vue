<script setup>

import {onMounted, ref} from "vue";
import {login as passkeyLogin} from "@/Authentication/Passkey";
import AlertBanner from "@/components/AlertBanner.vue";
import router from "@/router";
import {set_current_auth_state} from "@/Authentication/store";

const username = ref('');
const messages = ref([]);

onMounted(()=>{
  if(sessionStorage.getItem('token')){
    router.push({name: 'home'});
  }
});

function add_message(severity, message) {
  messages.value.push({
    type: severity,
    message: [message]
  });
}

async function login(){
  messages.value = [];
  passkeyLogin(username.value).then((r)=>{
    add_message('success', 'Logged in successfully');
    sessionStorage.setItem('token', r.data.token.key);
    router.push({name: 'home'})
    set_current_auth_state(true);
  }).catch((e)=>{
    if (e.isAxiosError){
      if(e.response.status >= 400 && e.response.status < 500){
        add_message('warning', e.response.data.message);
      } else {
        add_message('error', 'An unexpected error occurred while trying to log in');
      }
    } else {
      add_message('warning', e.message);
    }
  });
}

</script>

<template>
  <AlertBanner :messages="messages"/>

  <v-form
    class="d-flex justify-center align-center"
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
              label="Username or Email"
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
