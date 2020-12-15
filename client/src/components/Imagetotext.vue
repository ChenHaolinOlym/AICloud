<template>
  <v-container>
    <v-row>
      <v-col>
        <v-row>
          <v-file-input
          counter
          show-size
          truncate-length="15"
          @change="uploadFile()"
          ref="fileupload"
          v-model="image"
          >
          </v-file-input>
        </v-row>
        <v-row>
          <!-- <v-img
            lazy-src="https://picsum.photos/id/11/10/6"
            max-height="300"
            max-width="300"
            src="https://picsum.photos/id/11/500/300"
          ></v-img> -->
          <v-img
            lazy-src="https://picsum.photos/id/11/10/6"
            max-height="300"
            max-width="300"
            :src="img_src"
          ></v-img>
        </v-row>
      </v-col>
      <v-col>
        <v-textarea
            outlined
            disabled
            name="Output1"
            label="Output Data"
            :value="Output1"
        ></v-textarea>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import UploadService from '../services/uploadservice'

export default {
  name: 'Imagetotext',
  data: () => ({
    img_src: "http://localhost:5000/static/images/example.png",
    progress: 0,
    message: "",
    image: 0,
    Output1: "",
  }),
  methods: {
    uploadFile: function() {
      this.upload()
    },
    upload: function() {
      UploadService.upload(this.image, (event) => {
        this.progress = Math.round((100 * event.loaded) / event.total);
      })
        .then((response) => {
          this.message = response.data.sentence;
          this.Output1 = this.message
          this.img_src = response.data.image
          return this.message;
        })
        .then((files) => {
          this.fileInfos = files.data;
        })
        .catch(() => {
          this.progress = 0;
          this.message = "Could not upload the file!";
          this.currentFile = undefined;
      });
    }
  }
}
</script>