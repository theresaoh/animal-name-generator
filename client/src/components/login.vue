<template>
  <div>
    <div v-if="!this.$parent.userInSession">
      <h1>Login</h1>
      <p>Username:</p><input v-model="username" type="text" />
      <p>Password:</p><input type="password" v-model="password"/>
      <p v-if="this.errorMessage != ''">{{ errorMessage }}</p>
      <br><br>
      <button @click="login()">Log In</button>
      <p>Not yet registered?</p>
      <router-link :to="'/register'"><button>Register</button></router-link>
    </div>
    <div v-else>
      <h1>You're already logged in, {{ this.$parent.userInSession }}</h1>
      <button @click="logout()">Log Out</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'login',
  props: {
    testUserInSession: '',
  },
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    }
  },
  methods: {
    login(){
      axios.post('/login', {username: this.username, password: this.password})
      .then((resp) => {
        if (resp.data.success == false){
          this.errorMessage = "Login Failed!"
        } else {
          console.log("logged in!")
        }
      });
      this.username = '';
      this.password = '';
      this.errorMessage = '';
      this.$router.push('/')
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
