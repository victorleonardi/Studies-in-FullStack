<template>
  <div class="app">
    <div class="header">
      <div class="logo-name">
        <img
          class="logo"
          src="https://png.pngtree.com/png-vector/20230531/ourmid/pngtree-train-coloring-page-with-a-locomotive-in-the-background-vector-png-image_6775523.png"
          alt=""
        />
        <h1 class="brand-name">Game Library</h1>
      </div>
    </div>
    <GameTab />
  </div>
</template>

<script setup lang="ts">
import GameTab from './components/GameTab.vue'
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Playwrite+BE+VLG:wght@100..400&display=swap');

.app {
  background-color: antiquewhite;
  height: 100vh;
}

.logo-name {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.logo {
  width: 15%;
}

.brand-name {
  color: black;
  font-family: 'Droid Sans', sans-serif;
  font-weight: bold;
}
</style>
