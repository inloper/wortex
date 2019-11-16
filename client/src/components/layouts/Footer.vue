<template>
  <header class="gooter">
    <div>
        <div class="footer"><p>Made by Index {{ year }}</p></div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Footer',
  data() {
    return {
        year:  new Date().toJSON().slice(0,4)
    }
  },
}
</script>


<style scoped>

</style>
