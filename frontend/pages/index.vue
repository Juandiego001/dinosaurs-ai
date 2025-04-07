<template>
    <!-- Video -->
    <v-container class="position-relative pa-0 ma-0 d-flex justify-center align-center" fluid>
        <video class="w-100" autoplay muted loop src="/Dinos_2.mp4"></video>

        <v-sheet class="bg-transparent position-absolute pa-8 rounded-xl text-center elevation-12"
            style="backdrop-filter: blur(14px);">
            <h1 class="text-white">Learn more about the incredible world of the dinosaurs🦕</h1>
            <p class="text-white my-6">Use artificial intelligence🤖 to know everything about your favorite dinosaur:
                species, era, habitat and more🚀</p>
            <v-btn class="bg-secondary" size="x-large">Start now</v-btn>
        </v-sheet>
    </v-container>

    <!-- Discover the giants of the past -->
    <v-container class="py-12" fluid>
        <v-row>
            <v-col class="d-flex justify-center align-center text-center" md="6" cols="12">
                <v-sheet class="text-secondary px-6">
                    <h1 class="text-h4">Discover the Giants of the Past💪</h1>
                    <h4 class="text-h6 px-6">
                        Step into a world where colossal creatures ruled the Earth🌍. Our AI-powered dinosaur explorer
                        brings
                        the ancient past to life — from towering predators to gentle herbivores. Dive into a
                        prehistoric⌛
                        adventure and learn what made these creatures truly extraordinary🤩
                    </h4>
                </v-sheet>
            </v-col>
            <v-col md="6" cols="12">
                <v-row no-gutters>
                    <v-col class="mb-4" cols="12">
                        <v-img class="mx-auto" max-width="600" cover src="/triceratops.webp" />
                    </v-col>
                    <v-col cols="12">
                        <v-sheet class="pa-4 bg-secondary text-white text-center end rounded-xl">
                            <h2>Triceratops🦖</h2>
                            <p>
                                One of the most iconic herbivorous dinosaurs, Triceratops roamed North America🗺️ around
                                68
                                to 66
                                million years ago⏳
                            </p>
                        </v-sheet>
                    </v-col>
                </v-row>
            </v-col>
        </v-row>
    </v-container>

    <!-- Most beloved dinosaurs -->
    <v-container class="bg-secondary text-center py-8 rounded-lg mb-8">
        <v-sheet class="bg-white d-inline-block mx-auto text-center mb-12 w-auto rounded-xl pa-4">
            <h2 class="text-secondary">Most beloved dinosaurs🦕💘</h2>
        </v-sheet>

        <v-row>
            <v-col md="4" cols="12">
                <v-img contain width="300" height="300" class="mx-auto mb-4" src="/velociraptor.webp"></v-img>
                <h2>Velociraptor🦎</h2>
                <p class="text-subtitle-2">
                    Small but deadly, Velociraptor was a fast, agile predator that hunted in packs. It lived around 75
                    million years ago and was about the size of a turkey, but don't let that fool you — it had a curved
                    claw on each foot and sharp teeth perfect for tearing into prey. Evidence suggests it had feathers,
                    making it an important link between dinosaurs and modern birds
                </p>
            </v-col>
            <v-col md="4" cols="12">
                <v-img contain width="300" height="300" class="mx-auto mb-4" src="/tyrannosaurus_rex.webp"></v-img>
                <h2>Tyrannosaurus Rex🦖</h2>
                <p class="text-subtitle-2">
                    Arguably the most famous dinosaur of all time, Tyrannosaurus Rex was a massive carnivore that lived
                    during the late Cretaceous period. Standing up to 40 feet long, it had powerful jaws capable of
                    crushing bone and sharp teeth up to 12 inches long. Despite its tiny arms, it was a dominant
                    predator, feared throughout its habitat. Its name means "Tyrant Lizard King" — and it certainly
                    lived up to it
                </p>
            </v-col>
            <v-col md="4" cols="12">
                <v-img contain width="300" height="300" class="mx-auto mb-4" src="/brachiosaurus.webp"></v-img>
                <h2>Brachiosaurus🦕</h2>
                <p class="text-subtitle-2">
                    Brachiosaurus was a gentle giant of the Jurassic period, known for its long neck and towering
                    stance. Unlike many other long-necked dinosaurs, its front legs were longer than its hind legs,
                    giving it a giraffe-like posture. It could reach treetops to feed on leaves and likely moved in
                    herds. Its size alone — up to 80 feet long — was a powerful defense against predators
                </p>
            </v-col>
        </v-row>
    </v-container>

    <!-- What we do -->
    <v-container class="text-center py-12">
        <h2 class="text-secondary mb-4 text-h4">What we do?🏭</h2>

        <v-row>
            <v-col md="6" cols="12">
                <v-sheet class="text-secondary text-subtitle-1 text-left">
                    DinoScan AI is an interactive platform where science meets
                    cutting-edge AI. Upload an image of a dinosaur
                    fossil, illustration, or model, and let our intelligent system predict the species with astonishing
                    accuracy. Whether you're a student, enthusiast, researcher, or just curious — this is your portal into the
                    prehistoric world.
                </v-sheet>
            </v-col>

            <v-col md="6" cols="12">
                <v-sheet class="text-secondary text-subtitle-1 text-right">
                    DinoScan AI is also a community-driven hub for dinosaur enthusiasts, learners, and curious minds. Our
                    interactive forum lets users ask questions, discuss fun facts, and even crowdsource feedback on uncertain
                    predictions. Whether you're a budding paleontologist or simply a fan of ancient creatures, there's a space
                    for you here.
                </v-sheet>
            </v-col>
        </v-row>

        <p class="text-h5 my-12 text-secondary">
            Also, our platform and community seeks to inform its users in different ways, so you will have the following resources at your disposal
        </p>

        <v-sheet class="my-12">
            <v-btn color="secondary" variant="outlined" class="me-4" append-icon="mdi-file-document-multiple" to="/resources">Resources</v-btn>
            <v-btn color="secondary" class="me-4" append-icon="mdi-rocket-launch" to="/login">Start Now</v-btn>
            <v-btn color="secondary" variant="outlined" append-icon="mdi-forum" to="/forum">Forum</v-btn>
        </v-sheet>

        <p class="text-h4 text-secondary font-italic">... and what are you waiting for🦖?</p>
    </v-container>
</template>

<script setup>
const name = ref('');
</script>

<style>
video {
    max-height: 100vh;
    object-fit: cover;
}
</style>