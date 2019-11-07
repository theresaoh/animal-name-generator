<template>
  <div class="login-contents">
    <div v-if="!this.$parent.loggedIn">
      <h1>Login</h1>
      <p>Username:</p><input v-model="username" type="text" />
      <p>Password:</p><input type="password" v-model="password"/>
      <br><br>
      <button @click="login()">Submit</button>
      <p>Not yet registered?</p>
      <router-link :to="'/register'"><button>Register</button></router-link>
    </div>
    <div v-if="this.$parent.loggedIn"> 
      <h1>You're already logged in.</h1>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'login',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login(){
      axios.post('/login', {username: this.username, password: this.password})
      .then((resp) => {
        if (resp.data.success == false){
          this.$router.go();
        } else {
          this.$parent.loggedIn = true;
          this.$router.push('/')
        }
      });
      this.username = '';
      this.password = '';
    }
  }
}
</script>

<style scoped>
.login-contents {
  padding-top: 20px;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  color: black;
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
