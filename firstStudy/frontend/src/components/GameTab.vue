<template>
  <table class="game-lib-table">
    <thead>
      <tr class="header">
        <th>Name</th>
        <th>Genre</th>
        <th>Played</th>
        <th>Actions</th>
      </tr>
    </thead>

    <tbody>
      <tr class="row-values" v-for="game in gameLib" :key="game.name">
        <td>{{ game.name }}</td>
        <td>{{ game.genre }}</td>
        <td>{{ game.played }}</td>
        <td>
          <button>Update</button>
          <button @click="removeGameFromLibrary(game.id)">Deletar</button>
        </td>
      </tr>
    </tbody>
  </table>

  <!-- <div class="container">
    <div class="header">
      <h1>Name</h1>
      <h1>Genre</h1>
      <h1>Played</h1>
      <h1>Actions</h1>
    </div>
    <div class="row-values" v-for="game in gameLib" :key="game.id">
      <h1>{{ game.name }}</h1>
      <h1>{{ game.genre }}</h1>
      <h1>{{ game.played }}</h1>
      <div class="action">
        <button>Update</button>
        <button @click="removeGameFromLibrary(game.id)">Deletar</button>
      </div>
    </div> -->
  <!-- </div> -->
</template>

<script setup lang="ts">
import { get_lib, delete_game } from '@/service/server'
import { onMounted, ref } from 'vue'

const gameLib = ref({})

const handleClick = () => {
  console.log('click')
}

async function removeGameFromLibrary(id) {
  const removedGame = await delete_game(id)
  gameLib.value = await get_lib()
  return true
}

onMounted(async () => {
  try {
    gameLib.value = await get_lib()
    console.log(gameLib.value)
  } catch (err) {
    console.log(err)
  }
})
</script>

<style scoped>
.game-lib-table {
  width: 90%;
  padding-left: 10%;
}

.action {
  display: flex;
  justify-content: center;
}

.header,
.row-values {
  display: flex;
  justify-content: space-between; /* Distribui espaço entre as colunas */
  justify-items: start;
}

.header,
.row-values,
.action {
  width: 100%;
  flex: 1; /* Cada item ocupará uma parte igual do espaço disponível */
  text-align: center; /* Alinha o texto ao centro de cada coluna */
  margin: 0; /* Remove margens adicionais */
}

.header {
  font-weight: bold; /* Torna o texto do cabeçalho mais proeminente */
  border-bottom: solid 3px;
  font-size: 1.5rem;
}

.row-values {
  border-bottom: solid 2px;
  font-size: 0.6rem;
}

.row-values:last-child {
  border-bottom: none;
}
</style>
