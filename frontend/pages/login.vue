<template>
    <v-container fluid class="fill-height justify-center pa-0 position-relative">
        <v-img width="100%" height="100%" cover class="position-absolute" src="/dino1.png"></v-img>
        <v-card max-width="400" class="bg-transparent px-6 pb-6" elevation="3" style="backdrop-filter: blur(14px);">
            <v-card-title class="text-center text-h4 text-white py-4">Log In</v-card-title>
            <v-form @submit.prevent="logIn">
                <v-row>
                    <v-col cols="12">
                        <v-text-field class="text-white" v-model="email" label="Email" hide-details="auto" type="email" variant="outlined">
                        </v-text-field>
                    </v-col>

                    <v-col cols="12 pb-0">
                        <v-text-field class="text-white" v-model="password" label="Password" hide-details="auto" variant="outlined"
                            type="password"></v-text-field>
                    </v-col>

                    <v-col cols="12" class="text-end">
                        <NuxtLink to="/recover-password" class="text-caption text-white text-decoration-none">Forgot
                            password?</NuxtLink>
                    </v-col>

                    <v-col cols="12">
                        <v-btn class="text-white" block variant="outlined" type="submit">
                            Log In
                        </v-btn>
                    </v-col>

                    <v-col class="text-caption text-white text-center pt-0" cols="12">
                        Don't have an account?
                        <NuxtLink to="/signup" class="text-white">Sign up</NuxtLink>
                    </v-col>
                </v-row>
            </v-form>
        </v-card>
    </v-container>
</template>

<script setup>
import { useProfile } from '~/composables/useProfile'

definePageMeta({
    layout: 'account'
})

const { $ability } = useNuxtApp();
const profile = useProfile()
const email = ref('')
const password = ref('')

const logIn = async () => {
    try {
        await $fetch('/api/users/login', {
            method: 'POST',
            body: {
                email: email.value,
                password: password.value
            }
        })
        const { abilities } = await $fetch('/api/users/profile', { method: 'GET' });
        $ability.update(abilities);
        navigateTo('/app');
    } catch (err) {
        console.log(err);
    }
}
</script>