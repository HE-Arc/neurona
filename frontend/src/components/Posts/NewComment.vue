<script setup>

import {ref} from "vue";
import ApiRequests from "@/api/ApiRequests";
import MessageManager from "@/tools/MessageManager";

const props = defineProps({
  open: Boolean,
  postId: String,
})

const value_ = ref(props.value);
const emit = defineEmits(['update:open', 'refresh']);

function submit(){
  const req = new ApiRequests();
  req.createComment(props.postId, value_.value).then(() => {
    MessageManager.getInstance().snackbar('Created successfully');
    emit('update:open', false);
    emit('refresh', value_.value)
  }).catch((e) => {
    // no need to show error message, it's already been done by the request class itself
    emit('update:open', false);
  });
}

</script>

<template>
  <v-dialog
    v-model="props.open"
    width="400"
  >
    <v-form>

      <v-card>
        <v-card-title>
          Add a new comment
        </v-card-title>
        <v-card-text>

          <v-textarea
            v-model="value_"
            label="comment"
          >
          </v-textarea>

        </v-card-text>
        <v-card-actions>
          <v-btn
            prepend-icon="mdi-close"
            @click="() => emit('update:open', false)"
            color="error"
          >
            Cancel
          </v-btn>
          <v-btn
            prepend-icon="mdi-check"
            color="primary"
            @click="submit"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
  </v-dialog>
</template>
<style scoped>
</style>
