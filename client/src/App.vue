<template>
  <div id="app">
    <div v-if="this.$route.path != '/'">
      <router-link :to="'/'"><button>Home</button></router-link>
    </div>
   <div v-if="!this.loggedIn">
      <router-link :to="'/login'"><button>Log In</button></router-link>
      <router-link :to="'/register'"><button>Register</button></router-link>
    </div>
    <div v-if="this.loggedIn">
      <button @click="logout()">Log Out</button>
   </div>
    <img alt="Vue logo" src="./assets/logo.png">
    <router-view></router-view>
  </div>
</template>

<script>
import NameGenerator from './components/NameGenerator.vue'
import login from './components/login.vue'
import register from './components/register.vue'
import favorites from './components/favorites.vue'
import axios from 'axios'

export default {
  name: 'app',
  components: {
    NameGenerator,
    login,
    register,
    favorites
  },
  data() {
    return {
      userInSession: '',
      loggedIn: false
    }
  },
  methods: {
    login(user, pass){
      axios.post('/login', {username: user, password: pass})
      .then((resp) => {
        if (resp.data.success == false){
          console.log("failed!");
          this.$router.go();
        } else {
          console.log("logged in!")
          this.$router.push('/');
          this.$router.go();
        }
      });
    },
    logout(){
      axios.post('/logout', {user: this.userInSession})
      .then((resp) => {
      })
      if (this.$route.path == '/'){
        this.$router.go();
      } else {
        this.$router.push('/')
      }
    },
    async testUserInSession(username) {
      let promise = axios.post('/users')
      .then((resp) => {
        if (resp.data.success == false){
          this.loggedIn = false;
          return false;
        }
        this.userInSession = resp.data.userInSession;
        this.loggedIn = true;
        return true;
      })
      let result = await promise;
      console.log("result : " + result);
      return result;
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
