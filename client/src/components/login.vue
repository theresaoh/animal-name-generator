<template>
  <div>
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
      this.$parent.login(this.username, this.password);
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
