<template>
  <div class="relative border rounded-lg" id="container">
    <table class="w-full text-sm text-left text-gray-500" id="table">
      <thead class="text-s text-white bg-opacity-70 uppercase bg-black">
        <tr>
          <th class="px-4 py-3">ID</th>
          <th class="px-4 py-3">Name</th>
          <th class="px-4 py-3">Genre</th>
          <th class="px-4 py-3">Played</th>
          <th class="px-4 py-3">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr id="row" v-for="game in gameLib" :key="game.id" class="border-b bg-white">
          <td class="px-4 py-3 font-bold text-gray-900">{{ game.id }}</td>
          <td class="px-4 py-3 font-bold text-gray-900">{{ game.name }}</td>
          <td class="px-4 py-3">{{ game.genre }}</td>
          <td class="px-4 py-3">{{ game.played }}</td>
          <td class="px-4 py-3">
            <Button severity="secondary" text>Update</Button>
            <Button severity="danger" text @click="removeGameFromLibrary(game.id)">Delete</Button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { get_lib, delete_game } from '@/service/server'
import { onMounted, ref } from 'vue'
import Button from 'primevue/button'

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

<style>
#container {
  width: 90vw;
  padding-left: 10vw;
}

#table {
  border-collapse: collapse;
  border-radius: 1rem;
}

#row:last-child {
  border-bottom: none;
}
</style>
