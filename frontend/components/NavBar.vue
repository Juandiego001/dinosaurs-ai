<template>
    <v-container fluid class="bg-secondary py-0 border border-b-lg">
        <v-row class="ma-0 py-2 justify-center no-gutters">
            <v-col class="d-flex align-center justify-center mt-2">
                <NuxtLink class="text-decoration-none text-white text-h5" to="/">🦖 DinoScanAI</NuxtLink>
            </v-col>

            <v-col cols="12" class="d-flex flex-wrap align-center justify-center ">
                <v-btn class="text-none mx-2"  to="/">
                    Inicio
                </v-btn>
                <v-btn class="text-none mx-2" to="/crew" variant="text">
                    Archivar
                </v-btn>
                <v-btn class="text-none mx-2" to="/about" variant="text">
                    Recursos
                </v-btn>
                <v-btn class="text-none mx-2" to="/crew" variant="text">
                    Crew
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