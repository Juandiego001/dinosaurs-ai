<template>
  <div class="px-4 my-4 text-secondary d-flex align-center">
    <NuxtLink class="text-secondary text-caption" to="/resources">Resources</NuxtLink>
    <v-icon class="mx-2">mdi-chevron-right</v-icon>
    <span class="text-caption">Articles</span>
  </div>

  <v-container min-height="100%">

    <div class="my-4 text-secondary d-flex align-center">
      <span class="text-h5 me-2">Articles</span>
      <v-icon>mdi-file-document-multiple</v-icon>
    </div>

    <v-row class="my-6">
      <v-card v-for="article in articles" :key="article.documentId"
      width="300" height="300" :to="`/resources/articles/${article.documentId}`" class="me-6">
        <v-img max-height="100" cover :src="`http://localhost:1337${article.cover.url}`" />
        <v-card-title>{{ article.title }}</v-card-title>
        <v-card-text>{{ article.description }}</v-card-text>
      </v-card>
    </v-row>

    <div class="py-4 text-center">
      <v-btn class="text-secondary" variant="text" append-icon="mdi-chevron-double-down">Load more</v-btn>
    </div>
  </v-container>
</template>

<script setup>
import { onBeforeMount } from 'vue'

const articles = ref([]);

onBeforeMount(async () => {
  const { data } = await $fetch('/strapi/articles?populate=*');
  articles.value = data;
})
</script>