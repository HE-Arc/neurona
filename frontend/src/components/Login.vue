<script setup>

import {ref} from "vue";
import {createPublicKeyCredential} from "@/Authentication/Passkey";

const username = ref('');

function login() {
  const credentials = createPublicKeyCredential('test', username.value);
  console.log(credentials);
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
        <v-col cols="12" md="10" lg="6">
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
