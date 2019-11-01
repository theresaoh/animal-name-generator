<template>
  <div>
    <h1>Favorited Names</h1>
    <div class="favorited-names">
    <div class="fav-female-names">
        <h2>Female Names</h2>
        <ul  v-for="name in namesToDisplay" v-if="name.name_gender == 'F'">
            <li @click="determineClickOrDoubleClick($event, name)">{{ name.favorited_name }}</li>
        </ul>
    </div>
    <div class="fav-male-names">
        <h2>Male Names</h2>
        <ul  v-for="name in namesToDisplay" v-if="name.name_gender == 'M'">
            <li @click="determineClickOrDoubleClick($event, name)">{{ name.favorited_name }}</li>
        </ul>
    </div>
    <div class="fav-gn-name">
        <h2>Gender-Neutral Names</h2>
        <ul  v-for="name in namesToDisplay" v-if="name.name_gender =='GN'">
            <li @click="determineClickOrDoubleClick($event, name)">{{ name.favorited_name }}</li>
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
        namesToDisplay: '',
        delay: 300,
        clicks: 0,
        timer: null
    }
  },
  methods: {
    determineClickOrDoubleClick(event, name){
      this.clicks++ 
      if (this.clicks === 1) {
        var self = this;
        this.timer = setTimeout(() => {
          self.clicks = 0
          }, this.delay);
        } else {
          clearTimeout(this.timer);
          axios.post('/remove-favorite', {id: name.id})
          this.clicks = 0;
          this.$router.go();
        }        	     
    },
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
