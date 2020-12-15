<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dense
      dark
    >
      <v-toolbar-title>CSC4160 Project</v-toolbar-title>
      <template v-slot:extension>
        <v-tabs align-with-title>
          <v-tab @click="tab=0">Imagetotext</v-tab>
          <v-tab @click="tab=1">TextSummarization</v-tab>
        </v-tabs>
      </template>
    </v-app-bar>

    <v-main>
      <Imagetotext v-if="tab==0"/>
      <TextSummarization v-if="tab==1"/>
    </v-main>
  </v-app>
</template>

<script>
import Imagetotext from './components/Imagetotext';
import TextSummarization from './components/TextSummarization';

export default {
  name: 'App',

  components: {
    Imagetotext,
    TextSummarization
  },

  data: () => ({
    "tab": 0
  }),
};
</script>
