<template>
  <div class="name-generator-component">
    <h1>Animal Name Generator</h1>
    <h4><b>Click</b> on a name to set it aside. Any names set aside will be erased on page refresh.<br><b>Double-click</b> to favorite a name to view later. You must be logged in to favorite names.</h4>
    <div class="name-generation-container">
    <!-- display 10 random female, male, and gender-neutral names at a time
        and pull new names on each user button click -->
      <div class="name-list-container">
        <button @click="getFemaleNames">Get Female Names</button>
        <ul>
          <li class="name-list" :class="{highlight:name.id == selected}" @click="determineClickOrDoubleClick($event, name)" v-for="name in this.femaleNamesToDisplay" :key="name.id" >{{ name.name }}<br></li>
        </ul>
      </div>
      <div class="name-list-container">
        <button @click="getMaleNames">Get Male Names</button>
        <ul>
          <li class="name-list" :class="{highlight:name.id == selected}" @click="determineClickOrDoubleClick($event, name)" v-for="name in this.maleNamesToDisplay" :key="name.id">{{ name.name }}<br></li>
        </ul>
      </div>
      <div class="name-list-container">
        <button @click="getGNNames">Get Gender-Neutral Names</button>
        <ul>
          <li class="name-list" :class="{highlight:name.id == selected}" @click="determineClickOrDoubleClick($event, name)" v-for="name in this.genderNeutralNamesToDisplay" :key="name.id">{{ name.name }}<br></li>
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
    <!-- Add a Name Section -->
    <h1>Add a Name</h1>
    <input placeholder="Enter Name Here" v-model="inputValue" /><br>
    <p>This name is typically:</p>
    <select v-model="addNameGender">
      <option value="F">Female</option>
      <option value="M">Male</option>
      <option value="GN">Gender-Neutral</option>
    </select>
    <!-- display error or success message if there's an error or success with entering new name to db -->
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
      delay: 300,
      clicks: 0,
      timer: null,
      selected: undefined,
    }
  },
  methods: {
    doubleClicked(name) {
      this.isDoubleClicked = false
      console.log(name.name)
    },
    testDuplicateNameInDB(){
      // before adding a new name to the DB, make sure that it doesn't already exist
      this.inputValue = this.inputValue.toUpperCase();
      this.successMessage = '';
      this.duplicateNameErrorMessage = '';
      axios.post('/duplicate-name-test', { name: this.inputValue, gender: this.addNameGender })
      .then(resp => {
        if (resp.data.does_the_name_exist.length == 0){
          // if the response from the database has a length of 0, the name doesn't exist and should be added
          this.addName();
        } else {
          this.duplicateNameErrorMessage = "That name already exists in the database."
          this.inputValue = '';
        }
      })
    },
    nameAlreadySetAside(name){
      // before setting aside a name in the "Liked Names" section of the page, make sure they're not already set aside
      if (!this.setAsideNames.includes(name.name)){
        // if the name hasn't already been set aside, set it aside
        this.setAside(name);
        return;
      }
      return false;
    },
    determineClickOrDoubleClick(event, name){
      // if a user clicks on a name just once during the timeout period (300 ms), set it aside in the "Liked Names" section
      this.clicks++ 
      if (this.clicks === 1) {
        var self = this;
        this.timer = setTimeout(() => {
          self.clicks = 0
          this.nameAlreadySetAside(name);
          }, this.delay);
        } else {
          // if a user double-clicks during the timeout period AND is currently logged in, user favorites the name
          if (!this.$parent.loggedIn){
            return;
          }
          this.selected = name.id
          clearTimeout(this.timer);
          this.favoriteName(name);
          this.clicks = 0;
        }        	     
    },
    setAside(name) {
      // set aside a name in the "Liked Names" section
      this.setAsideNames.push(name.name);
    },
    favoriteName(name){
      // favorite a name
      axios.post('/favorite-name', {name_id: name.id, favorited_name: name.name, name_gender: name.gender})
      this.isDoubleClicked = true
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
      axios.post('/name', {
        name: this.inputValue, 
        gender: this.addNameGender
        })
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

<style scoped>
.name-generator-component{
  padding-top: 10px;
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
  cursor: pointer;
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
li.highlight{
  animation: effect_dylan 0.5s ease-out;
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
@keyframes effect_dylan {
  50% {
    transform: scale(1.5, 1.5);
    opacity: 1;
  }
}
</style>
