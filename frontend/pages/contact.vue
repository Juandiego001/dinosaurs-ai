<template>
<v-container fluid class="fill-height justify-center">
    <v-card max-width="700" class="pa-3 bg-primary" elevation="10">
        <v-card-title class="text-center">
            <p class="text-h4">Discover the Prehistoric World</p>
        </v-card-title>

        <v-card-text>
            <p class="my-4 text-justify">
                Curious about dinosaurs and want to discover fascinating facts?<br /><br />

                It’s simple! Upload an image of any dinosaur or take a real-time photo using our camera feature.<br /><br />

                In seconds, our artificial intelligence system will identify the species and provide you with detailed information.<br /><br />

                Perfect for students, hobbyists, and any paleontology enthusiast.
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
