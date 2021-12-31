<template>
  <div id="app">
    <HomePage msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import HomePage from './components/HomePage.vue'

export default {
  name: 'App',
  components: {
    HomePage,
  },
}
</script>

<style>
#app {
    max-width: 95%;
    margin: 0 auto;
}
</style>
