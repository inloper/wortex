<template>
  <div class="container-fluid">
    <div class="row">
      <input type="text" class="form-control form-control-sm" v-model="search" placeholder=" filter">
      <Search />
      <b-alert show dismissible class='success'><b>Logged in!</b></b-alert>
      <table class="table table-hover table-dark hover_img">
        <div v-if="torr_data.length">
        <thead>
          <tr>
            <th class="col-sm">Date</th>
            <th class="col-sm">Size</th>
            <th class="col-long">Title</th>
            <th></th>
          </tr>
        </thead>
        <tbody v-if="torr_data.length">
          <tr v-for="(item, id) in filterTitles.slice().reverse()" :key="id"> 
            <th scope="row" class="gray-txt">{{ item.date }}</th>
            <th scope="row" class="gray-txt">{{ item.size }}</th>
            <td>
              <div>
                <a :href="item.mlink" v-bind:title="item.title">{{ item.title | snippet }}
                  <span><img class="thumb_img" :src="item.image" alt="image"></span>
                </a>
              </div>
            </td>
          </tr>
        </tbody>
        </div>
        <div v-else>
          <p class="btn-danger" style="text-align: center;">Connection error. Please check if API server is running.</p>
        </div>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Search from '../components/Search'
import { isValidJwt, EventBus } from '@/utils'

export default {
  components: {
    Search
  },
  data() {
    return {
      torr_data: [],
      search: ''
    }
  },

  methods: {
    loadDataFromStore() {
      this.$store.dispatch('loadTorrData')
        .then(res => {
          this.torr_data = this.$store.state.loadedTorrData
          // console.log(res.headers)
        })
      }
  },

  created() {
    this.loadDataFromStore()
  },

	computed: {
		filterTitles: function() {
			return this.torr_data.filter((item) => {
        return item.title.toLowerCase().match(this.search)
      })
    },
    // isAuthenticated() {
    //   return this.$store.getters.isAuthenticated
    // }
  },

  filters: {
    snippet(value) {
      return value.slice(0, 150)
    }
  },
}
</script>