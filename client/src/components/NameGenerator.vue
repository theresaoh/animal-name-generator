<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <ul>
      <li v-for="name in names">{{ name.name }}</li>
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
      inputValue: ''
    }
  },
  methods: {
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
      .then(res => this.names = res.data.results)
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
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
