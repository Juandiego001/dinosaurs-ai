<template>
  <v-data-table :headers="headers"></v-data-table>

  <!-- Create Dialog -->
  <v-dialog v-model="createDialog">
    <v-card>
      <v-card-title class="bg-blue-darken-4">
        <v-row no-gutters align="center">
          Make a prediction
          <v-spacer></v-spacer>
          <v-btn class="bg-blue-darken-4" variant="icon" icon="mdi-close"
            @click="isActive = false; createDialog = false"></v-btn>
        </v-row>
      </v-card-title>
      <v-card-text>
        <v-row class="pa-5">
          <v-col class="pa-0 mb-3" cols="12">
            <video ref="video" class="w-100" poster="/public/camera-enhance-outline.svg"></video>
            <canvas ref="canvas" class="d-none"></canvas>
          </v-col>

          <v-col class="text-center" cols="12">
            <v-row class="justify-center ga-4">
              <v-btn v-if="!camActive" class="bg-blue-darken-4" @click="openCam">OPEN CAMERA</v-btn>
              <v-btn v-if="camActive" class="bg-blue-darken-4" @click="closeCam">CLOSE CAMERA</v-btn>
              <v-btn v-if="camActive && !photo" variant="outlined" color="blue-darken-4" @click="takePicture">TAKE
                PICTURE</v-btn>
              <v-btn v-if="photo" variant="outlined" color="blue-darken-4" @click="takeAnotherPicture">TAKE ANOTHER
                PICTURE</v-btn>
              <v-btn v-if="photo" color="light-blue-darken-4" @click="validatePhoto">VALIDATE ENTRY</v-btn>
            </v-row>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { toRefs } from 'vue'
import { searchMixin } from '~/mixins/searchMixin'
import { createMixin } from '~/mixins/createMixin'

definePageMeta({
  layout: 'app',
  middleware: ['private']
})

useHead({
    title: 'DinoScanAI | Searches'
})

const { ...searchRefs } = toRefs(searchMixin)
const { ...createRefs } = toRefs(createMixin)

const headers = computed(() => [
  { title: 'Id', key: 'id' },
  { title: 'Image', key: 'img_path' },
  { title: 'Prediction', key: 'prediction' },
  { title: 'Options', key: 'options', align: 'center' }
])

</script>