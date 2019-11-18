<template>
<main role="main" class="container">
  <div class="d-flex align-items-center p-3 my-3 text-white-50 bg-purple rounded shadow-sm">
    <!-- <img class="mr-3" src="/docs/4.3/assets/brand/bootstrap-outline.svg" alt="" width="48" height="48"> -->
    <div class="lh-100">
      <h6 class="mb-0 text-white lh-100">Podcasts
        <select v-model="selected" @change="getPodcastsData(selected)">
          <option v-for="option in options" :key="option.index" v-bind:value="option">{{ option }}</option>
        </select>
      </h6>
    </div>
  </div>
  <div class="my-3 p-3 rounded shadow-sm">
    <h6 class="border-bottom border-gray pb-2 mb-0">Recode Decode
      <input type="number" size="50" v-model="podcastLimit" v-on:keyup.enter="getPodcastsData()">
    </h6>
    <div v-if="!rss_entries.length"><h1>LOADING {{ selected }}</h1></div>
    <div v-else class="media text-muted pt-3" v-for="item in rss_entries" :key="item.index">
      <svg class="bd-placeholder-img mr-2 rounded" width="32" height="32" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: 32x32"><title>Placeholder</title><rect width="100%" height="100%" fill="#007bff"/><text x="50%" y="50%" fill="#007bff" dy=".3em">32x32</text></svg>
      <p class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
        <strong class="d-block text-gray-dark">{{ item.title }} | <small>{{ item.published }}</small></strong>
        <vue-audio :file="item.link" />
      </p>
    </div>
    <small class="d-block text-right mt-3">
      <div href="#">All podcasts</div>
    </small>
  </div>
</main>
</template>

<script>
import Axios from 'axios'
import VueAudio from 'vue-audio'

export default {
  components: {
    'vue-audio': VueAudio
  },
  data() {
    return {
      rss_entries: [],
      podcastLimit: '5',
      selected: 'recode',
      options: ['recode', 'earth911']
    }
  },
  methods: {
    getPodcastsData(selected) {
      const path = 'http://localhost:5000/api/podcasts/' + this.selected
      Axios.get(path)
        .then((res) => { this.rss_entries = res.data.rss_entries.slice(0, this.podcastLimit) })
        .catch((error) => {console.error(error) })
    }
  },
  created() {
    this.getPodcastsData()
  },
}
</script>

<style scoped>
  input[type=number] {
    background-color: #6c757d;
    width: 55px;
    height: 25px;
    float: right;
    border: none;
    border-radius: 1px;
  }

</style>