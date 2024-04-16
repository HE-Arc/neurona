<script setup>

const props = defineProps({
  messages: Array,
});

</script>

<template>
  <div v-if="props.messages">
    <v-alert v-for="(item, key) in props.messages" :key="key" :type="item.type" closable>
    <strong>{{ item.title }}</strong>
    <ul>
      <li v-for="(msg, index) in item.message" :key="index">{{ msg }}</li>
    </ul>
    </v-alert>
  </div>
</template>

<style scoped>

</style>
