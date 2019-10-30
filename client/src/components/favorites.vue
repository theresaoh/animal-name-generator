<template>
  <div>
    <h1>Favorited Names</h1>
    <div class="favorited-names">
    <div class="fav-female-names">
        <h2>Female Names</h2>
        <ul  v-for="name in namesToDisplay" v-if="name.name_gender == 'F'">
            <li>{{ name.favorited_name }}</li>
        </ul>
    </div>
    <div class="fav-male-names">
        <h2>Male Names</h2>
        <ul  v-for="name in namesToDisplay" v-if="name.name_gender == 'M'">
            <li>{{ name.favorited_name }}</li>
        </ul>
    </div>
    <div class="fav-gn-name">
        <h2>Gender-Neutral Names</h2>
        <ul  v-for="name in namesToDisplay" v-if="name.name_gender =='GN'">
            <li>{{ name.favorited_name }}</li>
        </ul>
    </div>
    </div>
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
.favorited-names{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}
a {
  color: #42b983;
}
</style>
