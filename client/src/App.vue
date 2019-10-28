<template>
  <div id="app">
    <div v-if="this.$route.path == '/'">
      <router-link :to="'/login'"><button>Log In</button></router-link>
    </div>
    <login :testUserInSession="testUserInSession" v-on:userLoggedIn="testUserInSession" hidden></login>
    <img alt="Vue logo" src="./assets/logo.png">
    <router-view></router-view>
  </div>
</template>

<script>
import NameGenerator from './components/NameGenerator.vue'
import login from './components/login.vue'
import register from './components/register.vue'
import axios from 'axios'

export default {
  name: 'app',
  data() {
    return {
      userInSession: '',
    }
  },
  methods: {
    testUserInSession(username) {
      axios.post('/users', {userInSession: username})
      .then((resp) => {
        if (resp.data.success == false){
          return false;
        }
        this.userInSession = resp.data.userInSession;
        console.log(this.userInSession)
        return true;
      })
    }
  },
  components: {
    NameGenerator,
    login,
    register
  },
  mounted() {
    this.testUserInSession();
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
