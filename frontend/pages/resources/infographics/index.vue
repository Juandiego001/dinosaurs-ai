<template>
  <div class="px-4 my-4 text-secondary d-flex align-center">
    <NuxtLink class="text-secondary text-caption" to="/resources">Resources</NuxtLink>
    <v-icon class="mx-2">mdi-chevron-right</v-icon>
    <span class="text-caption">Infographics</span>
  </div>

  <v-container min-height="100%">

    <div class="my-4 text-secondary d-flex align-center">
      <span class="text-h5 me-2">Infographics</span>
      <v-icon>mdi-file-image</v-icon>
    </div>

    <v-row class="my-6">
        <v-card v-for="infography in infographics" :key="infography.documentId"
          width="300" height="300" :to="`/resources/infographics/${infography.documentId}`" class="me-6">
          <v-img max-height="100" cover :src="`${strapiUrl}${infography.file.url}`" />
          <v-card-title>{{ infography.title }}</v-card-title>
          <v-card-text>{{ infography.description }}</v-card-text>
        </v-card>
    </v-row>

    <div class="py-4 text-center">
      <v-btn class="text-secondary" variant="text" append-icon="mdi-chevron-double-down">Load more</v-btn>
    </div>
  </v-container>
</template>

<script setup>
import { onBeforeMount } from 'vue'

const config = useRuntimeConfig();

const strapiUrl = config.public.strapiUrl;
const infographics = ref([]);

onBeforeMount(async () => {
  const { data } = await $fetch('/strapi/infographics?populate=*');
  infographics.value = data;
})
</script>