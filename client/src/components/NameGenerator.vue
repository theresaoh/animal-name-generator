<template>
  <div class="name-generator-component">
    <h1>Animal Name Generator</h1>
    <h4><b>Click</b> on a name to set it aside. Any names set aside will be erased on page refresh.<br><b>Double-click</b> to favorite a name to view later. You must be logged in to favorite names.</h4>
    <div class="name-generation-container">
      <div class="name-list-container">
        <button @click="getFemaleNames">Get Female Names</button>
        <ul>
          <li class="name-list" @click="determineClickOrDoubleClick($event, name)" v-for="name in this.femaleNamesToDisplay" :key="name.id">{{ name.name }}<br></li>
        </ul>
      </div>
      <div class="name-list-container">
        <button @click="getMaleNames">Get Male Names</button>
        <ul>
          <li class="name-list" @click="determineClickOrDoubleClick($event, name)" v-for="name in this.maleNamesToDisplay" :key="name.id">{{ name.name }}<br></li>
        </ul>
      </div>
      <div class="name-list-container">
        <button @click="getGNNames">Get Gender-Neutral Names</button>
        <ul>
          <li class="name-list" @click="determineClickOrDoubleClick($event, name)" v-for="name in this.genderNeutralNamesToDisplay" :key="name.id">{{ name.name }}<br></li>
        </ul>
      </div>
    </div>
    <div v-if="this.setAsideNames.length > 0">
      <hr>
      <h1 class="liked-title">Liked Names</h1>
      <ul>
        <li class="liked-names-list" v-for="name in this.setAsideNames" :key="name.id">{{ name }}</li>
      </ul>
    </div>
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
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'NameGenerator',
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
          self.clicks = 0
          this.nameAlreadySetAside(name);
          }, this.delay);
        } else {
          if (!this.$parent.loggedIn){
            return;
          }
          clearTimeout(this.timer);
          this.favoriteName(name);
          this.result = 'Favorited';
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
.contents{
  padding-top: 10px;
}
body {
  color: #2c3e50;
}
h3 {
  margin: 40px 0 0;
}
h4 {
  font-weight: normal;
}
.liked-title {
  color: #a15655;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  color: #2c3e50;;
  margin: 5px 10px;
  font-weight: bold;
}
.name-list:hover {
  font-weight: normal;
}
.name-generation-container {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}
.name-list-container {
  border: 1px solid #2c3e50;
  padding-top: 10px;
  width: 15em;
}
.error-message {
  color: red;
  font-weight: bold;
}
.success-message {
  color: green;
  font-weight: bold;
}
.liked-names-list {
  display: inline-block;
  font-weight: normal;
}
</style>
