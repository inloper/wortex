<template>
	<div>
		<div class="row">
			<form v-on:submit.prevent="searchString" method="POST">
				<input class="form-control form-control-sm" type="text" v-model="searched_string" placeholder=' browse' />
				<button class="btn btn-primary btn-sm">search</button>
			</form>
			<button @click="updateButton" class="btn btn-info btn-sm"> Update </button>
		</div>
	</div>
</template>

<script>
export default {
  name: "Search",
  data() {
    return {
		searched_string: '',
		errors: []
    }
  },
	methods: {
    updateButton() {
      this.$store.dispatch('scraper')
        .then(() => this.$router.push('/torr'))
    },
    searchString() {
			this.$store.dispatch('searchedString', {body: this.searched_string})
        .then(() => this.$router.push('/torr'))
    },
	}
}
</script>


<style scoped>
	form {
		display: flex;
	}
</style>