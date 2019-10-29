<template>
  <div id="app">
    <div v-if="this.$route.path != '/'">
      <router-link :to="'/'"><button>Home</button></router-link>
    </div>
   <div v-if="!this.loggedIn">
      <router-link :to="'/login'"><button>Log In</button></router-link>
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
import axios from 'axios'

export default {
  name: 'app',
  data() {
    return {
      userInSession: '',
      loggedIn: false
    }
  },
  methods: {
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
    consoleTest(){
      this.testUserInSession().then(function(data){
        console.log("console test : " + data)
        return data;
      })
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
      // var accessResult = promise.then(function(result) {
      //   console.log(result);
      // });
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
    this.consoleTest();
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
