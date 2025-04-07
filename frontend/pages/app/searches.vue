<template>
  <v-data-table :headers="headers"></v-data-table>

  <!-- Chat Dialog -->
  <v-dialog v-model="createDialog" fullscreen>
    <v-card>
      <v-card-title class="d-flex align-center bg-secondary">
        <p class="text-caption">DinoScanAI Chat 🦖</p>
        <v-spacer></v-spacer>
        <v-btn class="bg-secondary" density="compact" icon="mdi-close" elevation="0" @click="createDialog=false"></v-btn>
      </v-card-title>

      <v-card-text class="d-flex justify-center align-center position-relative pa-0">
        <v-img class="position-absolute h-100 w-100" cover src="/public/dinos-wallpaper.jpg"></v-img>
        <v-sheet class="position-absolute bg-primary h-100 w-75" style="z-index: 2;">
          <div class="position-absolute bottom-0 left-0 right-0 pa-4">
            <v-text-field v-model="message" label="Escribe tu mensaje o adjunta una foto" hide-details="auto" prepend-icon="mdi-paperclip">
              <template v-slot:append>
                <v-btn class="bg-primary">Send</v-btn>
              </template>
            </v-text-field>
          </div>
        </v-sheet>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { toRefs } from 'vue'
import { searchMixin } from '~/mixins/searchMixin'
import { createMixin } from '~/mixins/createMixin'
import { useTemplateRef, nextTick } from 'vue'

definePageMeta({
  layout: 'app',
  middleware: ['private']
})

useHead({
  title: 'DinoScanAI | Searches'
})

// refs
const { ...searchRefs } = toRefs(searchMixin);
const { createDialog } = toRefs(createMixin);
const form = ref({});
const message = ref('');
const camActive = ref(false);
const media = ref('');
const photo = ref('');
const isActive = ref(false);

// template_refs
const video = useTemplateRef('video');
const canvas = useTemplateRef('canvas');

// computed
const headers = computed(() => [
  { title: 'Id', key: 'id' },
  { title: 'Image', key: 'img_path' },
  { title: 'Prediction', key: 'prediction' },
  { title: 'Options', key: 'options', align: 'center' }
])

// methods
const openCam = async () => {
  try {
    const constraints = {
      video: { width: 1280, height: 720 },
    };

    media.value = await navigator.mediaDevices.getUserMedia(constraints);
    video.value.srcObject = media.value;
    video.value.onloadedmetadata = () => video.value.play();
    camActive = true;
  } catch (err) {
    console.log(err);
  }
}

const closeCam = async () => {
  try {
    if (video.value) video.value.src = '';
    const videoTrack = media.value.getVideoTracks()[0];
    videoTrack.stop();
    media.value.removeTrack(videoTrack);
    camActive.value = false;
    photo.value = ''
  } catch (err) {
    console.log(err);
  }
}

const takePicture = async () => {
  try {
    video.value.pause();
    const context = canvas.value.getContext('2d');

    const width = video.value.getBoundingClientRect().width;
    const height = video.value.getBoundingClientRect().height;

    canvas.value.width = width;
    canvas.value.height = height;

    context.drawImage(video.value, 0, 0, canvas.value.width, canvas.value.height);
    photo.value = canvas.value.toDataURL('image/png');
  } catch (err) {
    console.log(err);
  }
}

const takeAnotherPicture = async () => {
  try {
    video.value.play();
    photo.value = ''
  } catch (err) {
    console.log(err);
  }
}

const validatePhoto = async () => {
  try {
    const { message, isOwner, plate } = await $fetch('/api/entries/validate/photo', {
      method: 'POST',
      body: {
        photo: photo.value
      }
    });

    isActive.value = true;
    form.value = {
      isOwner,
      plate
    };

    $nextTick(() => {
      createDialog.value = false;
      entryDialog.value = true;
    })
  } catch (err) {
    console.log(err);
  }

}

</script>