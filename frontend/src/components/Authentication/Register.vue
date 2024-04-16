<script setup>

import {onMounted, ref} from "vue";
import {register as PasskeyRegister} from "@/Authentication/Passkey";
import routes from "@/api/routes";
import axios from "axios";
import router from "@/router";
import store from "@/Authentication/store";
import MessageManager from "@/tools/MessageManager";

const username = ref('');
const name = ref('');
const messages = ref([]);

onMounted(() => {
  if (sessionStorage.getItem('token')) {
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
  await axios.get(routes.authentication.username_availability, {params: {username: username.value}});
}

function showErrorMessage(e) {
  if (e.isAxiosError) {
    if (e.response.status >= 400 && e.response.status < 500) {
      MessageManager.getInstance().add('warning', e.response.data.message);
    } else {
      MessageManager.getInstance().add('error', 'An unexpected error occurred while trying to register');
    }
  } else {
    MessageManager.getInstance().add('error', e.message);
  }
}

async function register() {
  messages.value = [];

  try {
    await checkValidity();
  } catch (e) {
    showErrorMessage(e);
    return;
  }
  PasskeyRegister(username.value, name.value).then((r) => {
    MessageManager.getInstance().add('success', 'Registered successfully');
    store.commit('setToken', r.data.token.key);
    store.commit('login');
    router.push({name: 'home'})
  }).catch((e) => {
    showErrorMessage(e);
  });
}

</script>

<template>
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
            >
              <v-tooltip
                activator="parent"
              >
                A unique username to identify you
              </v-tooltip>
            </v-text-field>

            <v-text-field
              v-model="name"
              label="Name"
              required
            >
              <v-tooltip
                activator="parent"
              >
                Your full name or a nickname
              </v-tooltip>
            </v-text-field>

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
