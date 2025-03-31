<template>
  <v-app-bar color="#3C2A21" dark>
    <v-app-bar-title>Недвижимость</v-app-bar-title>

    <v-spacer></v-spacer>

    <v-btn
      v-for="(item, index) in menuItems"
      :key="index"
      :to="item.route"
      text
    >
      {{ item.title }}
    </v-btn>
  </v-app-bar>
</template>

<script setup>
const menuItems = [
  { title: 'Главная', route: '/' },
  { title: 'Контакты', route: '/contacts' }
]
</script>

<style scoped>
/* Здесь можно добавить дополнительные стили при необходимости */
</style>
