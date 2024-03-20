<script setup>

import {onMounted, ref} from "vue";
import {register as PasskeyRegister} from "@/Authentication/Passkey";
import AlertBanner from "@/components/AlertBanner.vue";
import routes from "@/api/routes";
import axios from "axios";
import router from "@/router";
import {set_current_auth_state} from "@/Authentication/store";

const username = ref('');
const email = ref('');
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

async function checkValidity() {
  await axios.get(routes.authentication.email_availability, {params: {email: email.value}});
  await axios.get(routes.authentication.username_availability, {params: {username: username.value}});
}

const send_registration = async (credentials, username, email, challenge_id) => {
  const data = {
    credentials: credentials,
    data: {
      username: username,
      email: email,
      challenge_id: challenge_id
    }
  }
  await axios.post(routes.authentication.register, data);
}

function showErrorMessage(e) {
  if (e.isAxiosError) {
    if (e.response.status >= 400 && e.response.status < 500) {
      add_message('warning', e.response.data.message);
    } else {
      add_message('error', 'An unexpected error occurred while trying to register');
    }
  } else {
    add_message('warning', e.message);
  }
}

async function register() {
  messages.value = [];
  await checkValidity();
  PasskeyRegister(username.value, email.value).then((r) => {
    add_message('success', 'Registered successfully');
    sessionStorage.setItem('token', r.data.token.key);
    set_current_auth_state(true)
    router.push({name: 'home'})
  }).catch((e) => {
    showErrorMessage(e);
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
              Register
            </h2>

            <p
              class="text-body-1 mx-2 mb-5"
            >
              Register to Neurona using a passkey.
            </p>

            <v-text-field
              v-model="username"
              label="Username"
              required
            />

            <v-text-field
              v-model="email"
              label="email"
              required
              email
            />

            <v-spacer/>

            <v-container>
              <v-row>
                <v-col cols="12" sm="6">
                  <v-btn
                    @click="() => $router.push({name: 'login'})"
                    prepend-icon="mdi-login"
                    class="mt-2 mb-2 mx-2"
                    block
                  >
                    Login
                  </v-btn>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-btn
                    color="primary"
                    @click="register"
                    prepend-icon="mdi-account-key"
                    class="mt-2 mb-2 mx-2"
                    block
                  >
                    Sign in with passkey
                  </v-btn>
                </v-col>

              </v-row>
            </v-container>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<style scoped>

</style>
