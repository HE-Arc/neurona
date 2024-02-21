<script setup>

import {ref} from "vue";
import {createPublicKeyCredential, getCredentials} from "@/Authentication/Passkey";
import router from "@/router";
import {set_current_auth_state, state} from "@/Authentication/store";
import AlertBanner from "@/components/AlertBanner.vue";

const username = ref('');
const messages = ref([]);

function register() {
  const credentials = createPublicKeyCredential('test', username.value)
    .then((response) => {
      state.authenticated = true;
      set_current_auth_state('true');
      router.push({name: 'home'});
    })
    .catch((e) => {
      messages.value = [{
        type: 'error',
        message: [e.message]
      }];
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
