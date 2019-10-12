<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <NameGenerator title="Name Generator"/>
  </div>
</template>

<script>
import NameGenerator from './components/NameGenerator.vue'

export default {
  name: 'app',
  components: {
    NameGenerator
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
