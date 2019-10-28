<template>
  <div id="app">
    <div v-if="this.$route.path == '/'">
      <router-link :to="'/login'"><button>Log In</button></router-link>
    </div>
    <img alt="Vue logo" src="./assets/logo.png">
    <router-view></router-view>
  </div>
</template>

<script>
import NameGenerator from './components/NameGenerator.vue'
import login from './components/login.vue'
import register from './components/register.vue'

export default {
  name: 'app',
  components: {
    NameGenerator,
    login,
    register
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
