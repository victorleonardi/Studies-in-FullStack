<template>
  <DataTable class="header" :value="gameLib" tableStyle="min-width: 50rem">
    <Column field="name" header="Name"></Column>
    <Column field="genre" header="Genre"></Column>
    <Column field="played" header="Played"></Column>
    <Column field="actions" header="Actions"></Column>
    <!-- <Column
      v-for="col of columns"
      :key="col.field"
      :field="col.field"
      :header="col.header"
    ></Column> -->
  </DataTable>
</template>

<script setup lang="ts">
import { get_lib, delete_game } from '@/service/server'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import ColumnGroup from 'primevue/columngroup' // optional
import Row from 'primevue/row'
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

<style>
.header {
  --p-datatable-header-cell-border-color: #fff;
  --p-datatable-body-cell-border-color: #fff;
  --p-datatable-header-cell-background: #10b981;
  --p-datatable-row-background: #10b981;
}
</style>
