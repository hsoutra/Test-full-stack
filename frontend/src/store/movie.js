// Utilities
import axios from 'axios';
import { defineStore } from 'pinia'

export const useMovieStore = defineStore('movie', {
  state: () => ({
    movies: {},
    movie: null,
    loading: false,
    error: null,
    count: null,
  }),
  
  actions: {
    fetchAll(page=0) {
      this.loading = true;
      axios.get("http://localhost:8000/films/?offset="+page*5)
        .then(({data}) => {
          this.movies = data.results;
          this.count = data.count;
        })
        .catch((err) => console.error(err))
        .finally(() => {this.loading = false});
    },
    fetchMovie(id) {
      this.loading = true;
      axios.get(`http://localhost:8000/films/${id}/`)
        .then(({data}) => {
          this.movie = data;
        })
        .catch((err) => console.error(err))
        .finally(() => {this.loading = false});
    },
    addReview(grade) {
      this.loading = true;
      axios.post(`http://localhost:8000/reviews/`, {
        "grade" : grade,
        "film" : this.movie.id,
      })
        .then(({data}) => {
          console.log(data);
        })
        .catch((err) => console.error(err))
        .finally(() => {this.loading = false});
    },
    updateMovie() {
      this.loading = true;
      axios.patch(`http://localhost:8000/films/${this.movie.id}/`, {
        "titre" : this.movie.titre,
        "description" : this.movie.description,
      })
        .then(({data}) => {
          console.log(data);
        })
        .catch((err) => console.error(err))
        .finally(() => {this.loading = false});
    },
    updateActor(data) {
      this.loading = true;
      axios.patch(`http://localhost:8000/actors/${data.id}/`, data)
        .then(({data}) => {
          console.log(data);
        })
        .catch((err) => console.error(err))
        .finally(() => {this.loading = false});
    },
  },
  
  getters: {
    getMovies(state) {
      return state.movies;
    },
    getMovie(state) {
      return state.movie;
    },
    pages(state) {
      return Math.round(state.count /5);
    },
  },
})
