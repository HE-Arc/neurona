<script setup>
import { ref, computed } from "vue";
import router from "@/router";
import ApiRequests from "@/api/ApiRequests";
import MessageManager from "@/tools/MessageManager";
import { useSpaceStore } from "@/stores/SpaceStore";
import { usePostStore } from "@/stores/PostStore";

const spaceStore = useSpaceStore();
const postStore = usePostStore();
const rules = ref([]);
const content = ref("");
const selectedSpace = ref(null);
const valid = ref(false);

rules.value = [(v) => v.length <= 1000 || "Max 1000 characters"];

const spaces = computed(() => spaceStore.getSpaces);

const uploadedFiles = ref([]);

function onFileChange(event) {
  console.log("Event:", event); // This should give context
  const files = event.target.files;
  console.log("Files:", files); // This should show the files
  if (Array.isArray(files) || files.length > 0) {
    uploadedFiles.value = Array.from(files);
  }
}
async function submit() {
  const req = new ApiRequests();

  let imageLinks = [];
  if (Array.isArray(uploadedFiles.value) && uploadedFiles.value.length > 0) {
    console.log("Starting to iterate over uploaded files.");
    const uploadPromises = uploadedFiles.value.map((file) => {
      return req
        .uploadImageToLocal(file)
        .then((imageLink) => {
          console.log("Image uploaded successfully:", imageLink);
          return imageLink;
        })
        .catch((error) => {
          console.error("Failed to upload image:", error);
          return null; // Continue with other uploads even if one fails
        });
    });

    // Wait for all uploads to complete
    imageLinks = (await Promise.all(uploadPromises)).filter(
      (link) => link !== null
    );
  } else {
    console.log("No files to upload.");
  }

  const postData = {
    content: content.value,
    space: selectedSpace.value,
    image_urls: imageLinks,
    saved: false,
  };

  try {
    await req.createPost(postData);
    console.log("Post created with images:", postData.image_urls);
    MessageManager.getInstance().snackbar("Post created successfully", 5000);
    postStore.fetchPosts();
    router.push({ name: "home" });
  } catch (error) {
    console.error("Error creating post:", error);
  }
}
</script>
<template>
  <v-container>
    <v-form v-model="valid">
      <v-autocomplete
        :items="spaces"
        item-title="name"
        item-value="id"
        prepend-icon="mdi-account"
        label="Space"
        v-model="selectedSpace"
      ></v-autocomplete>

      <v-textarea
        counter
        label="What's on your mind?"
        :rules="rules"
        v-model="content"
        prepend-icon="mdi-text-box-edit"
        auto-grow
        clearable
      ></v-textarea>

      <v-file-input
        v-model="uploadedFiles.value"
        label="Upload an image"
        accept="image/*"
        prepend-icon="mdi-image"
        :chips="true"
        multiple
        @change="onFileChange"
      ></v-file-input>

      <div class="d-flex flex-row-reverse my-5">
        <v-btn
          :disabled="!valid"
          prepend-icon="mdi-check"
          color="primary"
          class="mx-2"
          @click="submit"
        >
          Submit
        </v-btn>

        <v-btn
          prepend-icon="mdi-close"
          text="Cancel"
          class="mx-2"
          @click="() => $router.go(-1)"
        />
      </div>
    </v-form>
  </v-container>
</template>

<style scoped></style>
