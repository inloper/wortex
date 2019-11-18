<template>
	<div>
		<div class="row">
			<form v-on:submit.prevent="search_string" method="POST">
				<input class="form-control form-control-sm" type="text" v-model="searched_string" placeholder=' browse' />
				<button class="btn btn-primary btn-sm">search</button>
			</form>
			<button @click="searchButton" class="btn btn-info btn-sm"> Update </button>
		</div>
	</div>
</template>

<script>
import {HTTP} from '@/http-common'

export default {
  name: "Search",
  data() {
    return {
		searched_string: '',
		errors: []
    }
  },
	methods: {
		searchButton() {
			// this.searching = false
			HTTP.get('scraper')
		},
    search_string () {
			console.log(this.searched_string)
			HTTP.post('scraper/search=', {body: this.searched_string})
    },
	}
}
</script>


<style scoped>
	form {
		display: flex;
	}
</style>