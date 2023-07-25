<template>
  <v-container class="detail">
    <v-row class="row" v-if="store.getMovie">
      <v-col cols="12">
        <v-text-field
          v-model="store.getMovie.titre"
          label="Titre"
        ></v-text-field>
      </v-col>

      <v-col cols="12">
        <v-textarea
          v-model="store.getMovie.description"
          label="Description"
        ></v-textarea>
      </v-col>
      <v-col cols="12" class="col-btn">
        <v-btn @click="back"> Back to list </v-btn>
        <v-btn color="success" @click="updateMovie">Update</v-btn>
      </v-col>
      
      <v-col cols="12" class="border">
        <h2>Reviews : {{ reviews }}</h2>
      </v-col>
      <v-col cols="12" class="col-btn">
        <v-rating
          v-model="rating"
          bg-color="orange-lighten-1"
          color="blue"
        ></v-rating>
        <v-btn color="success" @click="submitRating">Rating</v-btn>
      </v-col>
      <v-col cols="12">
        <ActeurComponent />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, computed } from "vue";
import { useMovieStore } from "../store/movie";
import { useRoute, useRouter } from "vue-router";
import ActeurComponent from "../components/ActeurComponent.vue"
const { fetchMovie, addReview, updateMovie } = useMovieStore();
const router = useRouter();
const route = useRoute();
const store = useMovieStore();
const rating = ref(0);

fetchMovie(route.params.id);

const reviews = computed(() => {
  const data = store.getMovie.reviews;
  return data.length === 0
    ? 0
    : (data.reduce((a, b) => a + b.grade, 0) / data.length).toFixed(2);
});

const back = () => {
  router.push({ name: "Home" });
};

const submitRating = async () => {
  await addReview(rating.value);
  rating.value = 0;
  fetchMovie(route.params.id);
};
</script>
<style scoped>
.row {
  max-width: 800px;
}
.col-btn {
  display: flex;
  justify-content: space-between;
}
.detail {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.border {
  border: 1px solid black;
  margin: 2rem 0;
}
</style>