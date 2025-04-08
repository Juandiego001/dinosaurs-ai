<template>
    <v-navigation-drawer v-model="drawer" class="bg-secondary" location="left">
        <v-list-item>
            <v-list-item-title>
                <NuxtLink to="/app" class="text-white text-decoration-none">🦖 DinoScanAI</NuxtLink>
            </v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>

        <template v-for="route in routes">
            <v-list-item v-if="!['forums', 'strapi'].includes(route.subject)" link :to="route.path" :title="route.title" :append-icon="route.icon"></v-list-item>
            <v-list-item v-if="['forums', 'strapi'].includes(route.subject)" link :href="route.path" :title="route.title" :append-icon="route.icon"></v-list-item>
        </template>

        <template v-slot:append>
            <div class="pa-2">
                <v-btn class="bg-secondary" block variant="text" @click="navigateTo('/')">
                    <v-icon icon="mdi-logout" class="me-2"></v-icon>
                    Logout
                </v-btn>
            </div>
        </template>
    </v-navigation-drawer>

    <v-app-bar color="secondary">
        <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>DinoScanAI</v-toolbar-title>
        <v-spacer></v-spacer>
        <template v-if="$vuetify.display.mdAndUp">
            <v-btn icon="mdi-plus" variant="text" @click="createDialog = !createDialog"></v-btn>
            <v-btn icon="mdi-magnify" variant="text" @click="searchDialog = !searchDialog"></v-btn>
        </template>

        <v-btn icon="mdi-dots-vertical" variant="text"></v-btn>
    </v-app-bar>
</template>

<script setup>
import { toRefs } from 'vue'
import { searchMixin } from '~/mixins/searchMixin'
import { createMixin } from '~/mixins/createMixin'

const { $ability } = useNuxtApp();
const { searchDialog } = toRefs(searchMixin)
const { createDialog } = toRefs(createMixin)

const routes = ref([])
const drawer = ref(true);
const menu = ref([
    {
        title: 'Users',
        subject: 'users',
        path: '/app/users',
        icon: 'mdi-account'

    },
    {
        title: 'Groups',
        subject: 'groups',
        path: '/app/groups',
        icon: 'mdi-account-group'

    },
    {
        title: 'Searches',
        subject: 'searches',
        path: '/app/searches',
        icon: 'mdi-magnify'
    },
    {
        title: 'Dinosaurs',
        subject: 'dinosaurs',
        path: '/app/dinosaurs',
        icon: 'mdi-google-downasaur'
    },
    {
        title: 'Forums',
        subject: 'forums',
        path: 'http://192.168.0.104:4200',
        icon: 'mdi-open-in-new'
    },
    {
        title: 'Strapi',
        subject: 'strapi',
        path: 'http://localhost:1337',
        icon: 'mdi-open-in-new'
    }
])


onMounted(() => {
    try {
        routes.value = menu.value.filter(item => $ability.can('read', item.subject));
    } catch (err) {
        console.error(err);
    }
})
</script>