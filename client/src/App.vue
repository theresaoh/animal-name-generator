<template>
  <div id="app">
    <div class="nav-bar">
    <!-- Navigation bar -->
      <router-link class="nav-bar-elem" :to="'/'"><button>Home</button></router-link>
      <template v-if="!this.loggedIn">
        <router-link class="nav-bar-elem" :to="'/login'"><button>Log In</button></router-link>
        <router-link class="nav-bar-elem" :to="'/register'"><button>Register</button></router-link>
      </template>
        <router-link class="nav-bar-elem" :to="'/favorites'"><button>Favorites</button></router-link>
        <router-link class="nav-bar-elem" :to="'/advanced'"><button>Movie Names</button></router-link>
      <template v-if="this.loggedIn">
          <button class="nav-bar-elem" @click="logout()">Log Out</button>
      </template>
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
    login(user, pass) {
      // logs user in and redirects to home
      axios.post('/login', {username: user, password: pass})
        .then((resp) => {
          if (resp.data.success == false){
            this.$router.go();
          } else {
            this.loggedIn = true;
            this.$router.push('/');
          }
        });
    },
    logout(){
      // logs user out and redirects to home or refreshes if already on homepage
      axios.post('/logout', {user: this.userInSession})
      this.loggedIn = false;
      if (this.$route.path == '/'){
        this.$router.go();
        return;
      }
      this.$router.push('/');
    },
    async testUserInSession() {
      /* hits backend and checks to see if a user is in session - adjusts this.loggedIn accordingly
      this ensures that the correct navbar buttons are displayed at all times */
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
      // these lines ensure that the promise resolves before adjusting the value of this.loggedIn (accounts for asynch)
      let result = await promise;
      return result;
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
  color: #2c3e50;
  background-color: #c9dbba;
  text-transform: uppercase;
  padding: 5px;
  border: 2px solid #2c3e50;
  border-radius: 6px;
  display: inline-block;
  transition: all 0.3s ease 0s;
}
button:hover {
  background-color: #b2c6a1;
  color: #2c3e50;
  border-radius: 50px;
  border-color: #2c3e50;
  transition: all 0.3s ease 0s;
}
</style>
