<template>
	<div>
		<button @click="searchButton" class="btn btn-info"> Update </button>
	</div>
</template>

<script>
import {HTTP} from '@/http-common'

export default {
  name: "Search",
  data() {
    return {

    }
  },
	methods: {
		searchButton() {
			// this.searching = false
			HTTP.get('scraper')
		}

	}

}
</script>

<style scoped>
	form {
		display: flex;
	}
</style>