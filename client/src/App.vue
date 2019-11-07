<template>
  <div id="app">
    <div class="nav-bar">
      <div v-if="this.$route.path != '/'">
        <router-link class="nav-bar-elem" :to="'/'"><button>Home</button></router-link>
      </div>
      <div v-if="this.displayLoginRegisterButtons">
        <router-link class="nav-bar-elem" :to="'/login'"><button>Log In</button></router-link>
        <router-link class="nav-bar-elem" :to="'/register'"><button>Register</button></router-link>
      </div>
        <router-link class="nav-bar-elem" :to="'/favorites'"><button>Favorites</button></router-link>
      <div v-if="this.loggedIn">
          <button class="nav-bar-elem" @click="logout()">Log Out</button>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
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
      if (this.$route.path == '/'){
        this.$router.go();
        return;
      }
    },
    async testUserInSession() {
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
      return result;
    }
  },
    computed: {
    displayLoginRegisterButtons(){
      if (this.$route.path != '/login' && !this.loggedIn){
        return true;
      } else {
        return false;
      }
    }
  },
  mounted() {
    this.testUserInSession()
  }
}
</script>

<style>
#app {
  margin: 10%;
  padding: 20px;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.nav-bar {
  display: flex;
  border-top: 1px #2c3e50 solid;
  border-bottom: 1px #2c3e50 solid;
  flex-direction: row;
  justify-content: center;
  padding: 10px;
}
.nav-bar-elem {
  margin: 0 10px;
}
button {
  color: #2c3e50 !important;
  background-color: #c9dbba !important;
  text-transform: uppercase;
  padding: 5px;
  border: 2px solid #2c3e50 !important;
  border-radius: 6px;
  display: inline-block;
  transition: all 0.3s ease 0s;
}
button:hover {
  background-color: #b2c6a1 !important;
  color: #2c3e50 !important;
  border-radius: 50px;
  border-color: #2c3e50 !important;
  transition: all 0.3s ease 0s;
}


</style>
