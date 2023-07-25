<template>
      <v-form>
        <h3>Add acteur</h3>
        <br>
        <div>
          <v-text-field
          v-model="selectdActor.first_name"
          label="Prenom"
        ></v-text-field>
      </div>
        <div><v-text-field
          v-model="selectdActor.last_name"
          label="Nom"
        ></v-text-field></div>
        <div>        
          <v-btn color="success" @click="handelAddActor(selectdActor)">Ajouter</v-btn>
        </div>
      </v-form>
    
</template>
<script setup>
import { useMovieStore } from "../store/movie";
import { reactive } from "vue";
const { addActor } = useMovieStore();
const selectdActor = reactive({first_name: "", last_name: ""})
const emit = defineEmits(['userAdded'])

const handelAddActor = async (actor) => {
  await addActor(actor);
  selectdActor.first_name = null;
  selectdActor.last_name = null;
  emit('userAdded')
}
</script>

<style scoped>
.mt-3 {
  margin-top: 2rem;
}
</style>