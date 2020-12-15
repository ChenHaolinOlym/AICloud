<template>
  <v-container>
    <v-row>
      <v-col>
        <v-textarea
          outlined
          name="Input1"
          label="Input Text"
          value=""
          v-model="Input1"
        ></v-textarea>
      </v-col>
      <v-col>
        <v-textarea
          outlined
          disabled
          name="Output2"
          label="Output Text"
          :value="Output2"
        ></v-textarea>
      </v-col>
    </v-row>
    <v-row>
      <v-btn @click="summarization()" color="primary">
        Summarization
      </v-btn>
    </v-row>
  </v-container>
</template>

<script>
import TextService from '../services/textservice'

export default {
  name: 'TextSummarization',
  data: () => ({
    Input1: "",
    Output2: "",
  }),
  methods: {
    summarization: function() {
      this.upload()
      console.log(this.Input1)
      console.log(this.hi)
    },
    upload: function() {
      TextService.upload(this.Input1, (event) => {
        this.progress = Math.round((100 * event.loaded) / event.total);
      })
        .then((response) => {
          this.message = response.data;
          this.Output2 = this.message
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