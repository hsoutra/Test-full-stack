<template>
  <v-container>
    <v-table density="compact">
    <thead>
      <tr>
        <th class="text-left">
          titre
        </th>
        <th class="text-left">
          date creation
        </th>
        <th class="text-left">
          action
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="item in store.getMovies"
        :key="item.id"
      >
        <td>{{ item.titre }}</td>
        <td>{{ item.created_at }}</td>
        <td> 
          <router-link :to="{name:'Detail', params: {id: item.id}}">
            <v-icon 
              end
              icon="mdi-eye"
            ></v-icon>
          </router-link>
        </td>
      </tr>
    </tbody>
    <tfoot>
      <v-pagination
        v-model="page"
        :length="store.pages"
        rounded="circle"
      ></v-pagination>
    </tfoot>
  </v-table>
  </v-container>
</template>

<script setup>
import { watch, ref } from 'vue'
import { useMovieStore } from "../store/movie";
const store = useMovieStore();
const { fetchAll } = useMovieStore();
const page = ref(1);

fetchAll();

watch(page, function(val) {
  fetchAll(val-1)
})
</script>
