<style>
.blur_img {
    filter: blur(30px);
}
</style>

<template>
    <v-container fluid class="fill-height justify-center bg-indigo-darken-4 position-relative pa-0">
        <v-img content-class="blur_img" width="100%" height="100%" cover class="position-absolute"
            src="/dino2.jpg"></v-img>
        <v-card max-width="500" class="bg-transparent px-6 pb-6" elevation="3" style="backdrop-filter: blur(14px);">
            <v-card-title class="text-h4 text-center py-4">Sign Up</v-card-title>
            <v-form ref="form" @submit.prevent="signUp">
                <v-row>
                    <v-col cols="12">
                        <v-text-field v-model="fullName" required label="Full name" hide-details="auto" />
                    </v-col>

                    <v-col cols="12">
                        <v-text-field v-model="email" required label="Email" hide-details="auto" />
                    </v-col>

                    <v-col cols="6">
                        <v-text-field v-model="password" required label="Password" hide-details="auto"
                            type="password" />
                    </v-col>

                    <v-col cols="6">
                        <v-text-field v-model="confirmPassword" required label="Confirm password" hide-details="auto"
                            type="password" />
                    </v-col>

                    <v-col cols="12" class="ma-0 d-flex justify-space-between" justify="end">
                        <v-btn to="/login" width="49%" variant="outlined" type="submit">
                            Log In
                        </v-btn>
                        <v-btn width="49%" type="submit">
                            Sign Up
                        </v-btn>
                    </v-col>
                </v-row>
            </v-form>
        </v-card>
    </v-container>
</template>

<script setup>
definePageMeta({
    layout: 'account'
})

const fullName = ref('')
const email = ref('')
const password = ref('',)
const confirmPassword = ref('')
const document = ref('')


const signUp = async () => {
    try {
        const response = await $fetch('/api/users/signup', {
            method: 'POST',
            body: {
                fullName: fullName.value,
                email: email.value,
                password: password.value,
                document: document.value
            }
        })
        navigateTo('/login');
    } catch (err) {
        console.log(err)
    }
}
</script>
