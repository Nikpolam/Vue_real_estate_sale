<template>
  <v-container class="py-2 primary">
    <v-row>
      <v-col cols="12" class="text-center mb-2">
        <h2 class="text-h3 font-weight-bold text-black">Почему выбирают нас</h2>
        <p class="text-subtitle-1 mt-1 text-black">Мы предлагаем качественный сервис и индивидуальный подход</p>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" md="4" v-for="(feature, index) in features" :key="index">
        <v-card class="mx-auto" height="100%" elevation="2">
          <v-card-text class="text-center pa-3">
            <v-icon size="48" color="#D4B08C" class="mb-2">{{ feature.icon }}</v-icon>
            <h3 class="text-h5 font-weight-bold mb-2 primary--text">{{ feature.title }}</h3>
            <p class="text-body-1">{{ feature.description }}</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
const features = [
  {
    icon: 'mdi-home-search',
    title: 'Профессиональный подбор',
    description: 'Наши эксперты помогут найти идеальное жилье, учитывая все ваши пожелания'
  },
  {
    icon: 'mdi-clock-check',
    title: 'Быстрый процесс',
    description: 'Минимальные сроки на оформление всех необходимых документов'
  },
  {
    icon: 'mdi-shield-check',
    title: 'Безопасность сделок',
    description: 'Гарантируем безопасность и прозрачность всех операций'
  }
]
</script>

<style scoped>
.v-card {
  transition: transform 0.3s;
}
.v-card:hover {
  transform: translateY(-5px);
}
</style> 