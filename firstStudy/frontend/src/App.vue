<template>
  <div class="app bg-gray-200">
    <div class="header flex">
      <div class="logo-name">
        <img
          class="logo"
          src="https://png.pngtree.com/png-vector/20230531/ourmid/pngtree-train-coloring-page-with-a-locomotive-in-the-background-vector-png-image_6775523.png"
          alt=""
        />
        <h1 class="brand-name text-">Game Library</h1>
      </div>
      <Button class="add-game" @click="handleClick" raised severity="success"
        >Adicionar Novo Jogo</Button
      >
    </div>
    <GameTab />
    <div v-show="showRegisterGame" class="bg-black text-gray-300 text-center py-10 m-10">{{showRegisterGame}}</div>
  </div>
</template>

<script setup lang="ts">
import GameTabPrime from './components/GameTabPrime.vue'
import Button from 'primevue/button'
import GameTab from '@/components/GameTab.vue'
import { ref } from 'vue'

const showRegisterGame = ref(false)

const handleClick = () => {
  console.log('click')
  showRegisterGame.value = !showRegisterGame.value
  console.log(showRegisterGame.value)
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Playwrite+BE+VLG:wght@100..400&display=swap');

.app {
  height: 100vh;
}

.header {
  gap: 40vw;
}

.logo-name {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 50vw;
}

.logo {
  width: 35%;
}

.add-game {
  width: 300px;
  height: 4vh;
  top: 3vh;
  right: 2%;
  font-size: x-small;
}

.brand-name {
  color: black;
  font-family: 'Droid Sans', sans-serif;
  font-weight: bold;
}
</style>
