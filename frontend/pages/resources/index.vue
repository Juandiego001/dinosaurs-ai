<template>
  <v-container min-height="100vh">
    <NuxtLink to="/resources/articles" class="my-4 text-secondary text-decoration-none d-flex align-center">
      <span class="text-h5 me-2">Articles</span>
      <v-icon>mdi-file-document-multiple</v-icon>
    </NuxtLink>

    <v-row>
      <v-card v-for="article in articles" :key="article.documentId"
      width="300" height="300" :to="`/resources/articles/${article.documentId}`" class="me-6">
        <v-img max-height="100" cover :src="`${strapiUrl}${article.cover.url}`" />
        <v-card-title>{{ article.title }}</v-card-title>
        <v-card-text>{{ article.description }}</v-card-text>
      </v-card>
    </v-row>

    <div class="py-4">
      <v-btn class="text-secondary" to="/resources/articles" variant="text" append-icon="mdi-chevron-double-right">View
        more</v-btn>
    </div>

    <NuxtLink to="/resources/videos" class="my-4 text-secondary text-decoration-none d-flex align-center">
      <span class="text-h5 me-2">Videos</span>
      <v-icon>mdi-video</v-icon>
    </NuxtLink>

    <v-row>
      <v-card v-for="video in videos" :key="video.documentId" width="300" height="300"
        :to="`/resources/videos/${video.documentId}`" class="me-6">
        <v-img max-height="100" cover :src="`${strapiUrl}${video.poster.url}`" />
        <v-card-title>{{ video.title }}</v-card-title>
        <v-card-text>{{ video.description }}</v-card-text>
      </v-card>
    </v-row>

    <div class="py-4">
      <v-btn class="text-secondary" to="/resources/videos" variant="text" append-icon="mdi-chevron-double-right">View
        more</v-btn>
    </div>

    <NuxtLink to="/resources/articles" class="my-4 text-secondary text-decoration-none d-flex align-center">
      <span class="text-h5 me-2">Infographics</span>
      <v-icon>mdi-file-image</v-icon>
    </NuxtLink>

    <v-row>
      <v-card v-for="infography in infographics" :key="infography.documentId" width="300" height="300"
      :to="`/resources/infographics/${infography.documentId}`" class="me-6">
        <v-img max-height="100" cover :src="`${strapiUrl}${infography.file.url}`" />
        <v-card-title>{{ infography.title }}</v-card-title>
        <v-card-text>{{ infography.description }}</v-card-text>
      </v-card>
    </v-row>

    <div class="py-4">
      <v-btn class="text-secondary" to="/resources/infographics" variant="text" append-icon="mdi-chevron-double-right">View
        more</v-btn>
    </div>
  </v-container>
</template>

<script setup>
import { onBeforeMount } from 'vue'

const config = useRuntimeConfig();

const strapiUrl = config.public.strapiUrl;
const articles = ref([]);
const videos = ref([]);
const infographics = ref([]);

onBeforeMount(async () => {
  let data;
  ({ data } = await $fetch('/strapi/articles?populate=*'));
  articles.value = data;
  ({ data } = await $fetch('/strapi/videos?populate=*'));
  videos.value = data;
  ({ data } = await $fetch('/strapi/infographics?populate=*'));
  infographics.value = data;
})

</script>
