<template>
  <div class="px-4 my-4 text-secondary d-flex align-center">
    <NuxtLink class="text-secondary text-caption" to="/resources">Resources</NuxtLink>
    <v-icon class="mx-2">mdi-chevron-right</v-icon>
    <NuxtLink class="text-secondary text-caption" to="/resources/infographics">Infographics</NuxtLink>
    <v-icon class="mx-2">mdi-chevron-right</v-icon>
    <span class="text-caption">{{ infography.slug }}</span>
  </div>

  <v-container min-height="100%">
    <v-row class="py-12">
      <v-col class="d-flex align-center">
        <p class="text-h4 font-weight-bold">{{ infography.title }}</p>
      </v-col>
      <v-col>
        <p class="text-caption text-grey">DATE</p>
        <p class="text-caption mb-2">{{ $dateFormat(new Date(infography.createdAt)) }}</p>
      </v-col>
    </v-row>

    <v-img :src="`http://localhost:1337${infography.file.url}`" width="100%"></v-img>
    <a class="text-subtitle-1 mt-2 d-block text-grey text-caption" :href="infography.url" target="_blank">{{ infography.url }}</a>
    <p class="text-subtitle-1 mt-2">{{ infography.description }}</p>
  </v-container>
</template>

<script setup>
import { onBeforeMount } from 'vue';

const { $dateFormat } = useNuxtApp();
const route = useRoute()

const infography = ref({
  file: {
    url: ''
  },
  title: '',
  description: ''
})

onBeforeMount(async () => {
  const { data } = await $fetch(`/strapi/infographics/${route.params.documentId}?populate=*`)
  infography.value = data;
})
</script>