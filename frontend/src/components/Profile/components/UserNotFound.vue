<script setup>

const props = defineProps({
  username: String,
});

</script>

<template>
  <v-container class="mt-16" fluid>
    <v-row justify="center" align="center">
      <v-col cols="12" sm="8" md="6" class="text-center">
        <v-icon
          size="100px"
          color="primary"
        >
          mdi-account-question
        </v-icon>

        <h1
          class="display-2 font-weight-bold mb-3"
        >
          404 - User Not Found
        </h1>
        <p
          class="subtitle-1 ma-5"
        >
          Sorry, the user <strong>"{{ username }}"</strong> does not exist. Please check the username and try again.
        </p>
        <v-btn
          color="primary mt-16"
          prepend-icon="mdi-home"
          to="/"
        >
          Go Home
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>

</style>
