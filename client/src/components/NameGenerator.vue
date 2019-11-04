<template>
  <div>
    <h1>{{ title }}</h1>
    <button @click="getFemaleNames">Get Female Names</button>
    <ul>
      <li @click="determineClickOrDoubleClick($event, name)" v-for="name in this.femaleNamesToDisplay">{{ name.name }}</li>
    </ul>
    <button @click="getMaleNames">Get Male Names</button>
    <ul>
      <li @click="determineClickOrDoubleClick($event, name)" v-for="name in this.maleNamesToDisplay">{{ name.name }}</li>
    </ul>
    <button @click="getGNNames">Get Gender-Neutral Names</button>
    <ul>
      <li @click="determineClickOrDoubleClick($event, name)" v-for="name in this.genderNeutralNamesToDisplay">{{ name.name }}</li>
    </ul>
    <hr>
    <h1>Liked Names</h1>
    <ul>
      <li v-for="name in this.setAsideNames">{{ name }}</li>
    </ul>
    <hr>
    <h1>Add a Name</h1>
    <input placeholder="Enter Name Here" v-model="inputValue" /><br>
    <p>This name is typically:</p>
    <select v-model="addNameGender">
      <option value="F">Female</option>
      <option value="M">Male</option>
      <option value="GN">Gender-Neutral</option>
    </select>
    <div class="error-message">{{ duplicateNameErrorMessage }}</div>
    <div class="success-message">{{ successMessage }}</div>
    <br><br>
    <button @click="this.testDuplicateNameInDB">Add Name</button>
    <br><br><br>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'NameGenerator',
  props: ['title'],
  data() {
    return {
      setAsideNames: [],
      names: ['a', 'b', 'c'],
      maleNamesToDisplay: [],
      femaleNamesToDisplay: [],
      genderNeutralNamesToDisplay: [],
      inputValue: '',
      addNameGender: '',
      duplicateNameErrorMessage: '',
      successMessage: '',
      result: '',
      delay: 300,
      clicks: 0,
      timer: null
    }
  },
  methods: {
    testDuplicateNameInDB(){
      this.successMessage = '';
      this.duplicateNameErrorMessage = '';
      axios.post('/duplicate-name-test', { name: this.inputValue, gender: this.addNameGender })
      .then(resp => {
        console.log(resp.data.does_the_name_exist.length)
        if (resp.data.does_the_name_exist.length == 0){
          this.addName();
        } else {
          this.duplicateNameErrorMessage = "That name already exists in the database."
          this.inputValue = '';
        }
      })
    },
    nameAlreadySetAside(name){
      if (!this.setAsideNames.includes(name.name)){
        this.setAside(name);
      } else {
        return false;
      }
    },
    determineClickOrDoubleClick(event, name){
      this.clicks++ 
      if (this.clicks === 1) {
        var self = this;
        this.timer = setTimeout(() => {
          this.result = "click"
          console.log(name.id);
          self.clicks = 0
          this.nameAlreadySetAside(name);
          }, this.delay);
        } else {
          if (!this.$parent.loggedIn){
            console.log("Sorry, you have to be logged in to favorite names");
            return;
          }
          clearTimeout(this.timer);
          this.favoriteName(name);
          this.result = 'Favorited';
          console.log(this.result);
          this.clicks = 0;
        }        	     
    },
    setAside(name) {
      this.setAsideNames.push(name.name);
    },
    favoriteName(name){
      axios.post('/favorite-name', {name_id: name.id, favorited_name: name.name, name_gender: name.gender})
    },
    getFemaleNames() {
      axios.get('/female-names')
        .then(res =>  {
          this.femaleNamesToDisplay = res.data.name;
        })
    },
    getMaleNames() {
      axios.get('/male-names')
        .then(res =>  {
          this.maleNamesToDisplay = res.data.name;
        })
    },
    getGNNames() {
      axios.get('/gender-neutral-names')
        .then(res =>  {
          this.genderNeutralNamesToDisplay = res.data.name;
        })
    },
    addName() {
      this.inputValue = this.inputValue.toUpperCase();
      axios.post('/name', {name: this.inputValue, gender: this.addNameGender})
      this.successMessage = "You've added that name to the database!";
      this.inputValue = '';
      this.addNameGender = '';
    }
  },
  mounted() {
    this.getGNNames(),
    this.getMaleNames(),
    this.getFemaleNames()
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
.error-message {
  color: red;
  font-weight: bold;
}
.success-message {
  color: green;
  font-weight: bold;
}
</style>
