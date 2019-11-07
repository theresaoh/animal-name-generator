<template>
  <div class="favorites-component">
    <div v-if="this.$parent.loggedIn">
    <!-- If a user is logged in, show their favorites -->
        <h1>Favorited Names</h1>
        <h3><b>Double-click</b> on a name to un-favorite it.</h3>
        <div class="favorites-container">
            <div class="fav-names">
                <h2>Female Names</h2>
                <ul  v-for="name in femaleNamesToDisplay" :key="name.id">
                    <li @click="determineClickOrDoubleClick($event, name)">{{ name.favorited_name }}</li>
                </ul>
            </div>
            <div class="fav-names">
                <h2>Male Names</h2>
                <ul  v-for="name in maleNamesToDisplay" :key="name.id">
                    <li @click="determineClickOrDoubleClick($event, name)">{{ name.favorited_name }}</li>
                </ul>
            </div>
            <div class="fav-names">
                <h2>Gender-Neutral Names</h2>
                <ul  v-for="name in gnNamesToDisplay" :key="name.id">
                    <li @click="determineClickOrDoubleClick($event, name)">{{ name.favorited_name }}</li>
                </ul>
            </div>
        </div>
    </div>
    <div v-if="!this.$parent.loggedIn">
    <!-- if a user is not logged in, entice them to register by demonstrating favorites functionality -->
        <h1>Sorry, you must be logged in to view your favorited names.</h1>
        <h2>Registering and logging in gives you the ability to favorite the names you like the most and view them at any time, like this:</h2>
        <br>
        <hr>
        <div class="favorites-container">
            <div class="fav-names">
                <h2>Female Names</h2>
                <ul  v-for="name in demoFemaleNames">
                    <li>{{ name }}</li>
                </ul>
            </div>
            <div class="fav-names">
                <h2>Male Names</h2>
                <ul  v-for="name in demoMaleNames">
                    <li>{{ name }}</li>
                </ul>
            </div>
            <div class="fav-names">
                <h2>Gender-Neutral Names</h2>
                <ul  v-for="name in demoGNNames">
                    <li>{{ name }}</li>
                </ul>
            </div>
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
        delay: 300,
        clicks: 0,
        timer: null,
        demoFemaleNames: ["Bella", "Luna", "Fluffy"],
        demoMaleNames: ["Rex", "Sparky", "Bruno"],
        demoGNNames: ["Socks", "Chowder", "Snuggles"],
        femaleNamesToDisplay: [],
        maleNamesToDisplay: [],
        gnNamesToDisplay: []
    }
  },
  methods: {
    determineClickOrDoubleClick(event, name){
    // if a user clicks only once during the timeout period (300 ms), do nothing
      this.clicks++ 
      if (this.clicks === 1) {
        var self = this;
        this.timer = setTimeout(() => {
          self.clicks = 0
          }, this.delay);
        } else {
        /* if during the timeout period the user clicked twice, remove the favorited 
        name instance from both the page and the favorites db */
          clearTimeout(this.timer);
          axios.post('/remove-favorite', {id: name.id})
          this.clicks = 0;
          this.$router.go();
        }        	     
    },
    getFavoritedNames() {
        axios.get('/favorited-names')
            .then((resp) => {
                // sort a user's favorited names by their gender so that they can be displayed by gender more easily
                for (var i = 0; i < resp.data.favorites.length; i++){
                    if (resp.data.favorites[i].name_gender == 'F'){
                        this.femaleNamesToDisplay.push(resp.data.favorites[i]);
                    } else if (resp.data.favorites[i].name_gender == 'M'){
                        this.maleNamesToDisplay.push(resp.data.favorites[i]);
                    } else if (resp.data.favorites[i].name_gender == 'GN'){
                        this.gnNamesToDisplay.push(resp.data.favorites[i]);
                    }
                }
            })
        }
    },
    mounted() {
        this.getFavoritedNames()
  }
}
</script>

<style scoped>
.favorites-component {
    padding-top: 20px;
}
h3 {
    font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  color: black;
  display: inline-block;
}
li:hover {
    font-weight: bold;
}
.favorites-container {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}
.fav-names {
    width: 18em;
}
</style>
