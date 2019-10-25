<template>
  <div>
    <h1>Login</h1>
    <p>Username:</p><input v-model="username" type="text" />
    <p>Password:</p><input type="password" v-model="password"/>
    <p>Not yet registered?</p>
    <button @click="display(username)">Register</button>
  </div>
</template>

<script>

export default {
  name: 'login',
  props: ['title'],
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    display(info) {
      console.log(info);
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
