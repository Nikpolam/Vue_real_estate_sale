<template>
  <v-app class="bg-grey-lighten-4">
    <Navbar />
    <router-view></router-view>
  </v-app>
</template>

<script setup>
import Navbar from './Navbar.vue'
</script>

<style>
.main-background {
  background: linear-gradient(135deg, #f3e5dc 0%, #e6d5cc 100%);
  min-height: 100vh;
}
</style>
