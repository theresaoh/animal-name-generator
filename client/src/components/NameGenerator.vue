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
    <br><br>
    <button @click="addName">Add Name</button>
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
      result: '',
      delay: 300,
      clicks: 0,
      timer: null
    }
  },
  methods: {
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
</style>
