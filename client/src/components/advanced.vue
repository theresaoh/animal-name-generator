<template>
    <div class="advanced-component">
        <h1>Names From Popular Films</h1>
        <h4>Find names from a list of the top 20 currently trending films.<br>Select a name here:</h4>
        <select v-model="selectedMovie" @change="displayMovieInfo()">
            <option v-for="movie in moviesResultsObjects" :value="movie">{{movie.title}}</option>
        </select>
        <br><br>
        <h1>{{ selectedMovie.title }}</h1><br>
        <div class="selected-movie-container" v-if="selectedMovie">
            <div class="selected-movie-poster">
                <img :src="posterUrl(selectedMovie)">
            </div>
            <div class="selected-movie-info">
            <h2>Character Names</h2>
            <ul>
                <li v-for="char in selectedMovieCharacterNames">{{ char.character }}</li>
            </ul>
            </div>
        </div>  
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'advanced',
  data() {
    return {
      trendingMovies: '',
      movieId: '',
      movieCharacters: [],
      moviesResultsObjects: [],
      selectedMovie: '',
      selectedMovieCharacterNames: '',
    }
  },
  methods: {
    displayMovieInfo: function() {
      this.selectedMovieCharacterNames = this.selectedMovie.credits.cast;
    },
    discoverMovies: function () {
        axios.get(`${api.root}/trending/movie/day?api_key=${api.token}`)
        .then((response) => {
            this.trendingMovies = response.data.results;
        for (var i = 0; i < this.trendingMovies.length; i++){
            this.movieId = this.trendingMovies[i].id;
            axios.get(`${api.root}/movie/${this.movieId}?api_key=${api.token}&append_to_response=credits`)
                .then((response) => {
                    this.moviesResultsObjects.push(response.data);
                });
            }
        })
    },
    posterUrl: function(movie) {
        var baseImageUrl = "http://image.tmdb.org/t/p/w300/";
        return baseImageUrl + movie.poster_path;
        }
    },
    mounted() {
        this.discoverMovies();
    }
}
</script>

<style scoped>
h4 {
  font-weight: normal;
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
.selected-movie-container {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}
.selected-movie-info {
    margin: 0 40px;
}
</style>
