<template>
    Testing
</template>

<script setup>
const { $ability } = useNuxtApp();

definePageMeta({
    layout: 'app',
    middleware: 'private'
})

useHead({
    title: 'DinoScanAI | App'
})

onMounted(() => {
    // if (!$ability.can('read', 'users')) navigateTo('/login');
})

</script>