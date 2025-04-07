<template>
    <v-container fluid class="bg-secondary py-0 border border-b-lg">
        <v-row class="ma-0 py-2 justify-center no-gutters">
            <v-col class="d-flex align-center justify-center mt-2">
                <NuxtLink class="text-decoration-none text-white text-h5" to="/">🦖 DinoScanAI</NuxtLink>
            </v-col>

            <v-col cols="12" class="d-flex flex-wrap align-center justify-center ">
                <v-btn class="text-none mx-2"  to="/">
                    Home
                </v-btn>
                <v-btn class="text-none mx-2" to="/about" variant="text">
                    About
                </v-btn>
                <v-btn class="text-none mx-2" to="/contact" variant="text">
                    Contact
                </v-btn>
                <v-btn class="text-none mx-2" to="/resources" variant="text">
                    Resources
                </v-btn>
                <v-btn class="text-none mx-2" to="/forum" variant="text">
                    Forum
                </v-btn>
                <v-btn class="text-none mx-2" variant="text" to="/login">
                    Log In
                </v-btn>
                <v-btn class="text-none mx-2" variant="text" to="/signup">
                    Sign Up
                </v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>

</script>