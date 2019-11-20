<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">Login or Register</h2>
          <p class="subtitle error-msg">{{ errorMsg }}</p>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <form v-on:keyup.enter="authenticate()">
          <div class="field">
            <label class="label is-large" for="username">Username:</label>
            <div class="control">
              <input type="username" class="input is-large" id="username" v-model="username">
            </div>
          </div>
          <div class="field">
            <label class="label is-large" for="password">Password:</label>
            <div class="control">
              <input type="password" class="input is-large" id="password" v-model="password">
            </div>
          </div>
          <!-- <div class="control">
            <a class="button is-large is-success" @click="register">Register</a>
          </div> -->
        </form>
      </div>
    </section>

  </div>
</template>

<script>
import { EventBus } from '@/utils'

export default {
	name: 'Login',
	data() {
		return {
			username: '',
      password: '',
      errorMsg: ''
		}
	},
  methods: {
    authenticate () {
      this.$store.dispatch('login', { username: this.username, password: this.password })
        .then(() => this.$router.push('/torr'))
    },
    // register () {
    //   this.$store.dispatch('register', { username: this.username, password: this.password })
    //     .then(() => this.$router.push('/'))
    // }
   },
  mounted () {
    // EventBus.$on('failedRegistering', (msg) => {
    //   this.errorMsg = msg
    // })
    EventBus.$on('failedAuthentication', (msg) => {
      this.errorMsg = msg
    })
  },
  beforeDestroy () {
    // EventBus.$off('failedRegistering')
    EventBus.$off('failedAuthentication')
  }
}
</script>

<style scoped>
</style>