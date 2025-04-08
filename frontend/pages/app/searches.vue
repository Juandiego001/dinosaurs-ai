<template>
  <v-data-table :headers="headers"></v-data-table>
  <canvas ref="canvas" class="d-none"></canvas>

  <!-- Chat Dialog -->
  <v-dialog v-model="createDialog" max-width="600" min-height="">
    <v-card>
      <v-card-title class="d-flex align-center bg-secondary">
        <p>Search Dinosaur</p>
        <v-spacer></v-spacer>
        <v-btn class="bg-secondary" icon="mdi-close" variant="text" @click="createDialog = false"></v-btn>
      </v-card-title>

      <v-card-text class="d-flex justify-center align-center position-relative">

        <v-row>
          <v-col v-if="prediction" class="text-white bg-secondary my-5">
            <p  class=" text-center text-h6 py-2">
              {{ prediction }}
            </p>
          </v-col>

          <v-col cols="12">
            <v-select v-model="dinosaur" color="secondary" :items="dinosaurs" item-title="nombreComun" item-value="nombreComun"
              label="Selec the dinosaur that you want know about or attach an image" hide-details="auto" :readonly="!!photo">
              <template v-slot:prepend>
                <v-btn class="bg-secondary" icon="mdi-paperclip" variant="text" @click="optionsDialog = true"></v-btn>
              </template>
            </v-select>
          </v-col>

          <v-col v-if="photo" class="text-caption text-secondary text-center" cols="12">
            You've upload a photo. Remember we take your photo and pass it to our model to check if
            there is a dinosaur and to tell you features about it. So you can not combine images and text.
          </v-col>

          <v-col v-if="photo" class="text-center w-100 position-relative d-flex justify-center align-center"
            @mouseenter="allowRemoveFinal = true" @mouseleave="allowRemoveFinal = false" cols="12">
            <v-img width="250" height="250" class="mx-auto" :src="photo"></v-img>
            <v-btn v-if="allowRemoveFinal" size="small" color="red-darken-4" class="position-absolute"
              icon="mdi-trash-can" @click="photo = ''"></v-btn>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="secondary" variant="outlined" @click="">Cancel</v-btn>
        <v-btn class="bg-secondary" @click="sendSearch">Send</v-btn>
        <v-btn v-if="prediction && imgPath" class="bg-secondary" @click="saveSearch">Save search</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <!-- Options Dialog -->
  <v-dialog v-model="optionsDialog" max-width="500">
    <v-card>
      <v-card-title class="bg-secondary">
        <v-row no-gutters class="align-center">
          <p>Attach an image</p>
          <v-spacer></v-spacer>
          <v-btn class="bg-secondary" icon="mdi-close" variant="text" @click="optionsDialog = false"></v-btn>
        </v-row>
      </v-card-title>
      <v-card-text class="pa-0">
        <v-row no-gutters class="align-center py-6">
          <div class="d-inline-block text-center w-50 border-e-sm">
            <v-file-input v-model="image" icon="mdi-paperclip" hide-input :multiple="false"></v-file-input>
            <p class="text-grey px-6">Attach an image from your computer</p>
          </div>
          <div class="d-inline-block align-center text-center w-50">
            <v-btn color="grey" size="large" icon="mdi-camera" variant="text" @click="photoDialog = true"></v-btn>
            <p class="text-grey px-6">Take a photo</p>
          </div>
          <div v-if="photo" class="d-block w-100 text-center position-relative d-flex justify-center align-center mt-6"
            @mouseenter="allowRemove = true" @mouseleave="allowRemove = false">
            <v-img width="150" contain height="150" class="mx-auto" :src="photo"></v-img>
            <v-btn v-if="allowRemove" size="small" color="red-darken-4" class="position-absolute" icon="mdi-trash-can"
              @click="photo = ''"></v-btn>
          </div>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="secondary" variant="outlined" @click="photo = ''; optionsDialog = false">Cancel</v-btn>
        <v-btn class="bg-secondary" @click="optionsDialog = false">Confirm</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <!-- Camera dialog -->
  <v-dialog v-model="photoDialog" max-width="500">
    <v-card>
      <v-card-title class="bg-secondary">
        <v-row no-gutters class="align-center">
          <p>Take a photo</p>
          <v-spacer></v-spacer>
          <v-btn class="bg-secondary" icon="mdi-close" variant="text" @click="photoDialog = false"></v-btn>
        </v-row>
      </v-card-title>
      <v-card-text>
        <v-col class="pa-0 mb-3" cols="12">
          <video ref="video" class="w-100" :poster="!!photo ? photo : cameraSvg"></video>
        </v-col>

        <v-col class="text-center" cols="12">
          <v-row class="justify-center ga-4">
            <v-btn v-if="!camActive" class="bg-secondary" @click="openCam">OPEN CAMERA</v-btn>
            <v-btn v-if="camActive" class="bg-secondary" @click="closeCam">CLOSE CAMERA</v-btn>
            <v-btn v-if="camActive && !photo" variant="outlined" color="secondary" @click="takePicture">TAKE
              PICTURE</v-btn>
            <v-btn v-if="photo" variant="outlined" color="secondary" @click="takeAnotherPicture">TAKE ANOTHER
              PICTURE</v-btn>
            <v-btn v-if="photo" color="secondary" @click="confirmPhoto">CONFIRM</v-btn>
          </v-row>
        </v-col>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { toRefs } from 'vue'
import { searchMixin } from '~/mixins/searchMixin'
import { createMixin } from '~/mixins/createMixin'
import { useTemplateRef, nextTick, watch } from 'vue'
import cameraSvg from '~/public/camera-enhance-outline.svg'

definePageMeta({
  layout: 'app',
  middleware: ['private']
})

useHead({
  title: 'DinoScanAI | Searches'
})

// refs
const { searchDialog } = toRefs(searchMixin);
const { createDialog } = toRefs(createMixin);
const optionsDialog = ref(false);
const photoDialog = ref(false);
const dinosaurs = ref([]);
const search = ref('');
const page = ref(1);
const perPage = ref(1500);
const form = ref({});
const dinosaur = ref('');
const camActive = ref(false);
const media = ref('');
const photo = ref('');
const image = ref(null);
const prediction = ref('');
const imgPath = ref('');
const isActive = ref(false);
const allowRemove = ref(false);
const allowRemoveFinal = ref(false);

// template_refs
const video = useTemplateRef('video');
const canvas = useTemplateRef('canvas');

// watch
watch(photo, (value) => {
  if (value) dinosaur.value = '';
})

watch(createDialog, async (value) => {
  if (value) {
    await getDinosaurs();
  }
})

watch(image, async (value) => {
  if (value) {
    const reader = new FileReader();
      reader.onload = function (e) {
        const img = new Image();
        img.onload = function () {
          const context = canvas.value.getContext('2d');
          context.clearRect(0, 0, canvas.value.width, canvas.value.height);
          context.drawImage(img, 0, 0, canvas.value.width, canvas.value.height);
          photo.value = canvas.value.toDataURL('image/png');
        };
      img.src = e.target.result;
    };
    reader.readAsDataURL(value);
  }
});

watch(createDialog, value => {
  if (!value) {
    photo.value = ''
    image.value = ''
  }
})

// computed
const headers = computed(() => [
  { title: 'Id', key: 'id' },
  { title: 'Image', key: 'img_path' },
  { title: 'Prediction', key: 'prediction' },
  { title: 'Options', key: 'options', align: 'center' }
])

// methods
const getDinosaurs = async () => {
  try {
    const data = await $fetch('/api/dinosaurs', {
      query: {
        search: search.value,
        page: page.value,
        perPage: perPage.value
      },
      method: 'GET'
    });
    dinosaurs.value = data.items;
  } catch (err) {
    console.error(err);
  }
}

const openCam = async () => {
  try {
    const constraints = {
      video: { width: 1280, height: 720 },
    };

    media.value = await navigator.mediaDevices.getUserMedia(constraints);
    video.value.srcObject = media.value;
    video.value.onloadedmetadata = () => video.value.play();
    camActive.value = true;
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

const confirmPhoto = async () => {
  try {
    if (video.value) video.value.src = '';
    const videoTrack = media.value.getVideoTracks()[0];
    videoTrack.stop();
    media.value.removeTrack(videoTrack);
    camActive.value = false;
    photoDialog.value = false;
  } catch (err) {
    console.log(err);
  }
}

const sendSearch = async () => {
  try {
    prediction.value = ''
    const data = await $fetch('/api/searches/photo', {
      body: {
        photo: photo.value
      },
      method: 'POST'
    });

    prediction.value = data.prediction
    imgPath.value = data.imgPath
  } catch (err) {
    console.error(err);
  }
}

const saveSearch = async () => {
  try {
    const { message } = await $fetch('/api/searches/save/photo', {
      body: {
        dinosaur: dinosaur.value,
        prediction: prediction.value,
        imgPath: imgPath.value
      },
      method: 'POST'
    });
  } catch (err) {
    console.err(err);
  }
}

</script>
