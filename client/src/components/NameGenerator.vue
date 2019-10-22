<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <button @click="getFemaleNames">Get Female Names</button>
    <ul>
      <li v-for="name in this.femaleNamesToDisplay">{{ name.name }}</li>
    </ul>
    <button @click="getMaleNames">Get Male Names</button>
    <ul>
      <li v-for="name in this.maleNamesToDisplay">{{ name.name }}</li>
    </ul>
    <button @click="getGNNames">Get Gender-Neutral Names</button>
    <ul>
      <li v-for="name in this.genderNeutralNamesToDisplay">{{ name.name }}</li>
    </ul>
    <input v-model="inputValue" />
    <button @click="handleAddNameClick">Add new name</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'NameGenerator',
  props: ['title'],
  data() {
    return {
      names: ['a', 'b', 'c'],
      maleNamesToDisplay: [],
      femaleNamesToDisplay: [],
      genderNeutralNamesToDisplay: [],
      inputValue: ''
    }
  },
  methods: {
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
    handleAddNameClick() {
      axios.post('/name', {item: this.inputValue})
        .then(() => {
          axios.get('/names').then( res => this.names = res.data.results);
        })
      this.inputValue = '';
    }
  },
  mounted() {
    axios.get('/names')
      .then(res =>  this.names = res.data.name)
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
