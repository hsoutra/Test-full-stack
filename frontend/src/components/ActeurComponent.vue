<template>
  <v-table density="compact">
    <thead>
      <tr>
        <th class="text-left">Prenom</th>
        <th class="text-left">Nom</th>
        <th class="text-left">action</th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="item in store.getMovie.actors"
        :key="item.id"
      >
        <td>{{ item.first_name }}</td>
        <td>{{ item.last_name }}</td>
        <td> 
            <v-icon @click="handelSelectedActor(item)"
              end
              icon="mdi-pencil"
            ></v-icon>
        </td>
      </tr>
      <tr v-if="selectdActor.first_name && selectdActor.last_name" class="mt-3">
        <td><v-text-field
          v-model="selectdActor.first_name"
          label="Titre"
        ></v-text-field></td>
        <td><v-text-field
          v-model="selectdActor.last_name"
          label="Titre"
        ></v-text-field></td>
        <td>        
          <v-btn color="success" @click="handelUpdateActor(selectdActor)">Update</v-btn>
        </td>
      </tr>
    </tbody>
  </v-table>
</template>
<script setup>
import { useMovieStore } from "../store/movie";
import { useRoute, useRouter } from "vue-router";
import { reactive } from "vue";

const { fetchMovie, updateActor } = useMovieStore();
const router = useRouter();
const route = useRoute();
const store = useMovieStore();

const selectdActor = reactive({})


const handelSelectedActor = (actor) => {
  Object.assign(selectdActor, actor);
}

fetchMovie(route.params.id);

const handelUpdateActor = async (actor) => {
  await updateActor(actor);
  selectdActor.first_name = null;
  selectdActor.last_name = null;
  fetchMovie(route.params.id);

}
</script>

<style scoped>
.mt-3 {
  margin-top: 2rem;
}
</style>