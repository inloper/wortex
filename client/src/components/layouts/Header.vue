<template>
  <header class="header">
    <div>
     <nav class="navbar">
      <div class="container-fluid">
        <div class="navbar-header">
        </div>
        <h6 style="color: #6c757d;">wortex</h6>
        <ul id="menu">
          <li class="menu-item"><router-link to="/home">home</router-link></li>
          <li class="menu-item"><router-link to="/podcasts">podcasts</router-link></li>
          <li class="menu-item"><router-link to="/rss">rss</router-link></li>
          <li class="menu-item" v-if="isAuthenticated"><router-link to="/torr">torr</router-link></li>
          <li class="menu-item" v-if="!isAuthenticated"><router-link to="/login">login</router-link></li>
          <li class="menu-item" v-if="isAuthenticated"><a href='/home' @click="logout">logout</a></li>
        </ul>
      </div>
    </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
  methods: {
    logout () {
      localStorage.removeItem('token')
      console.log('token deleted')
    }
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated
    }
  }
}
</script>


<style scoped>
  .header {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px;
  }
  .header a {
    color: #fff;
    padding-right: 5px;
  }
</style>
