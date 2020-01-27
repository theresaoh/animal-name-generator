<template>
  <div class="register-component">
    <template v-if="this.$parent.loggedIn == false">
    <!-- if a user isn't currently logged in, allow them to register -->
      <h1>Register</h1>
      <p>Username:</p><input v-model="username" type="text" />
      <p>Password:</p><input type="password" v-model="password" />
      <p>Confirm Password:</p><input type="password" v-model="confirmPassword" /><br><br>
      <div class="error-message">{{ duplicateUserErrorMessage }}</div>
      <div class="error-message">{{ passwordMatchErrorMessage }}</div>
      <div class="error-message">{{ passwordRequirementsErrorMessage }}</div>
      <button @click="testDuplicateUser()">Register</button>
      <p>Already a registered user?</p>
      <router-link :to="'/login'"><button>Log In</button></router-link>
    </template>
    <template v-else>
    <!-- if a user is already logged in, tell them -->
      <h1>You're already logged in.</h1>
    </template>
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
      const capitalLetters = /[A-Z]/ //checks a password for any capital alphabetical letters
      const specialChracters = /\W/ //checks a password for any special characters (non-alpha, non-number)
      if (!capitalLetters.test(this.password) || !specialChracters.test(this.password) || !this.password.length >= 5){
        /* if a password doesn't contain a capital letter, doesn't contain a special 
        character, OR is less than 5 chars total, display error */
        this.passwordRequirementsErrorMessage = "Passwords must be at least 5 characters long and include at least one capital letter and one special character";
        return;
      }
      if (this.password != this.confirmPassword){
        // if the password and confirmed password don't match, display error
        this.passwordMatchErrorMessage = "Those passwords don't match. Please re-enter.";
        return;
      }
      // if the passwords match and meet requirements, add the user to DB
      this.addNewUser();
    },
    testDuplicateUser(){
      // before adding a new user to DB, make sure that username isn't already taken
      axios.post('/duplicate-user-test', { username: this.username })
        .then(resp => {
          if (resp.data.does_the_user_exist.length == 0){
          // if the length of response is 0, the user doesn't exist - test the password validity
            this.passwordMeetsRequirements();
          } else {
          // otherwise, display an error
            this.duplicateUserErrorMessage = "Sorry, that username already exists."
            this.username = '';
            this.password = '';
            this.confirmPassword = '';
          }
        })
    },
    addNewUser() {
      // add a new user to the DB, log them in, and redirect to the home page
      axios.post('/add-user', { username: this.username, password: this.password })
      this.$parent.loggedIn = true;
      this.$parent.userInSession = this.username;
      this.username = '';
      this.password = '';
      this.confirmPassword = '';
      this.$router.push('/');
    }
  }
}
</script>

<style scoped>
.register-component {
  padding-top: 20px;
}
.error-message{
  color: red;
  font-weight: bold;
}
</style>
