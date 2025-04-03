<template>
<v-container fluid class="fill-height justify-center bg-grey-darken-4">
    <v-card max-width="700" class="pa-3 bg-grey-darken-4" elevation="10">
        
        <v-card-title class="text-center">
            <p class="text-h6 ">Descubre el Mundo Prehistórico</p>
        </v-card-title>

        <v-card-text>
            <p class="my-4 text-justify">
                ¿Curioso sobre dinosaurios y quieres conocer datos fascinantes?<br /><br />

                ¡Es simple! Sube una imagen de cualquier dinosaurio o toma una foto en tiempo real 
                con nuestra función de cámara.<br /><br />

                En segundos, nuestro sistema de inteligencia artificial identificará la especie 
                y te proporcionará información detallada<br /><br />

                Ideal para estudiantes, aficionados y cualquier entusiasta de la paleontología.
            </p>

            <!-- Falta la parte del upload image -->

            <v-form>
                <v-row class="justify-center align-center">
                    <v-col cols="12">
                        <v-img max-height="300"></v-img>
                    </v-col>

                    <v-col cols="12">
                        <v-textarea label="Message" hide-details="auto"></v-textarea>
                    </v-col>

                    <v-col class="text-end" cols="12">
                        <v-btn type="submit" variant="outlined">Send</v-btn>
                    </v-col>
                </v-row>
            </v-form>

        </v-card-text>
    </v-card>
</v-container>
</template>

<script setup>

</script>
