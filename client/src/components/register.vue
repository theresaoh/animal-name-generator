<template>
  <div>
    <h1>Register</h1>
    <p>Username:</p><input v-model="username" type="text" />
    <p>Password:</p><input type="password" v-model="password"/>
    <p>Confirm Password:</p><input type="password" v-model="confirmPassword"/><br><br>
    <button @click="addNewUser()">Register</button>
    <p>Already a registered user?</p>
    <router-link :to="'/login'"><button>Log In</button></router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'login',
  props: ['title'],
  data() {
    return {
      username: '',
      password: '',
      confirmPassword: ''
    }
  },
  methods: {
    addNewUser() {
      axios.post('/add-user', { username: this.username, password: this.password } )
      this.username = '';
      this.password = '';
    }
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
