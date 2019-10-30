<template>
  <div>
    <h1>Favorited Names</h1>
    <ul>
        <li v-for="name in namesToDisplay">{{ name.favorited_name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'favorites',
  data() {
    return {
        namesToDisplay: ''
    }
  },
  methods: {
    getFavoritedNames() {
        axios.get('/favorited-names')
            .then((resp) => {
                this.namesToDisplay = resp.data.favorites;
            })
        }
    },
    mounted() {
        this.getFavoritedNames()
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
