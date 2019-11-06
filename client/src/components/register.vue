<template>
  <div>
    <div v-if="this.$parent.loggedIn == false">
      <h1>Register</h1>
      <p>Username:</p><input v-model="username" type="text" />
      <p>Password:</p><input type="password" v-model="password"/>
      <p>Confirm Password:</p><input type="password" v-model="confirmPassword"/><br><br>
      <div class="error-message">{{ duplicateUserErrorMessage }}</div>
      <div class="error-message">{{ passwordMatchErrorMessage }}</div>
      <div class="error-message">{{ passwordRequirementsErrorMessage }}</div>
      <button @click="testDuplicateUser()">Register</button>
      <p>Already a registered user?</p>
      <router-link :to="'/login'"><button>Log In</button></router-link>
      </div>
    <div v-else>
    <h1>You're already logged in.</h1>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'register',
  data() {
    return {
      username: '',
      password: '',
      confirmPassword: '',
      duplicateUserErrorMessage: '',
      passwordRequirementsErrorMessage: '',
      passwordMatchErrorMessage: ''
    }
  },
  methods: {
    passwordMeetsRequirements(){
      this.duplicateUserErrorMessage = '';
      this.passwordRequirementsErrorMessage = '';
      this.passwordMatchErrorMessage = '';
      const capitalLetters = /[A-Z]/
      const specialChracters = /\W/
      if (!capitalLetters.test(this.password) || !specialChracters.test(this.password) || !this.password.length >= 7){
        this.passwordRequirementsErrorMessage = "Passwords must be at least 5 characters long and include at least one capital letter and one special character";
        return;
      }
      if (this.password != this.confirmPassword){
        this.passwordMatchErrorMessage = "Those passwords don't match. Please re-enter.";
        return;
      }
      this.addNewUser();
    },
    testDuplicateUser(){
      axios.post('/duplicate-user-test', { username: this.username })
      .then(resp => {
        if (resp.data.does_the_user_exist.length == 0){
          this.passwordMeetsRequirements();
        } else {
          this.duplicateUserErrorMessage = "Sorry, that username already exists."
          this.username = '';
          this.password = '';
          this.confirmPassword = '';
        }
      })
    },
    addNewUser() {
      axios.post('/add-user', { username: this.username, password: this.password })
      .then(resp => {
        this.login(resp.data.username, resp.data.password);
      })
      this.username = '';
      this.password = '';
      this.confirmPassword = '';
    },
    login(user, pass) {
      axios.post('/login', {username: user, password: pass})
      .then((resp) => {
        if (resp.data.success == false){
          this.$router.go();
        } else {
          this.$parent.loggedIn = true;
          this.$router.push('/');
        }
      });
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
.error-message{
  color: red;
  font-weight: bold;
}
</style>
