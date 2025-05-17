<template>
  <v-container class="pt-16">
    <v-row>
      <v-col cols="12" class="text-center mb-4">
        <h2 class="text-h3 font-weight-bold primary--text">Частные дома</h2>
        <p class="text-subtitle-1 mt-2">Найдите свой идеальный дом</p>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" md="4" v-for="(house, index) in houses" :key="index">
        <v-card class="mx-auto" height="100%" elevation="2">
          <v-img
            :src="house.image"
            height="200"
            cover
          ></v-img>
          <v-card-text class="pa-4">
            <h3 class="text-h5 font-weight-bold mb-2">{{ house.title }}</h3>
            <p class="text-body-1 mb-2">{{ house.description }}</p>
            <div class="d-flex align-center mb-2">
              <v-icon size="20" color="primary" class="mr-1">mdi-map-marker</v-icon>
              <span>{{ house.location }}</span>
            </div>
            <div class="d-flex align-center mb-2">
              <v-icon size="20" color="primary" class="mr-1">mdi-currency-rub</v-icon>
              <span class="text-h6">{{ house.price }}</span>
            </div>
            <div class="d-flex align-center mb-2">
              <v-icon size="20" color="primary" class="mr-1">mdi-ruler-square</v-icon>
              <span>{{ house.area }} м²</span>
            </div>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="white"
                class="text-black"
                @click="showDetails(house)"
              >
                Подробнее
              </v-btn>
            </v-card-actions>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Диалог с подробной информацией -->
    <v-dialog v-model="dialog" max-width="600">
      <v-card v-if="selectedHouse">
        <v-img
          :src="selectedHouse.image"
          height="300"
          cover
        ></v-img>
        <v-card-text class="pa-4">
          <h3 class="text-h4 font-weight-bold mb-4">{{ selectedHouse.title }}</h3>
          <p class="text-body-1 mb-4">{{ selectedHouse.description }}</p>
          
          <div class="d-flex align-center mb-2">
            <v-icon size="20" color="primary" class="mr-2">mdi-map-marker</v-icon>
            <span>{{ selectedHouse.location }}</span>
          </div>
          
          <div class="d-flex align-center mb-2">
            <v-icon size="20" color="primary" class="mr-2">mdi-currency-rub</v-icon>
            <span class="text-h5">{{ selectedHouse.price }}</span>
          </div>
          
          <div class="d-flex align-center mb-2">
            <v-icon size="20" color="primary" class="mr-2">mdi-ruler-square</v-icon>
            <span>{{ selectedHouse.area }} м²</span>
          </div>

          <div class="mt-4">
            <h4 class="text-h6 mb-2">Характеристики:</h4>
            <ul class="pl-4">
              <li v-for="(feature, index) in selectedHouse.features" :key="index" class="mb-1">
                {{ feature }}
              </li>
            </ul>
          </div>

          <v-btn
            color="#D4B08C"
            class="text-black mt-4"
            block
            @click="contactAgent"
          >
            Связаться с агентом
          </v-btn>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'

const dialog = ref(false)
const selectedHouse = ref(null)

const houses = [
  {
    title: 'Современный дом с участком',
    description: 'Просторный дом с современным дизайном и большим участком',
    location: 'Московская область, Одинцово',
    price: '45 000 000 ₽',
    area: '250',
    image: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
    features: [
      '3 спальни',
      '2 ванные комнаты',
      'Большая гостиная',
      'Отдельная кухня',
      'Гараж на 2 машины',
      'Участок 15 соток'
    ]
  },
  {
    title: 'Уютный дом в лесу',
    description: 'Деревянный дом с панорамными окнами и видом на лес',
    location: 'Московская область, Химки',
    price: '35 000 000 ₽',
    area: '180',
    image: 'https://images.unsplash.com/photo-1600596542815-ffad4c153aee9?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
    features: [
      '2 спальни',
      '1 ванная комната',
      'Открытая терраса',
      'Камин',
      'Участок 12 соток',
      'Вид на лес'
    ]
  },
  {
    title: 'Семейный дом с садом',
    description: 'Просторный дом для большой семьи с ухоженным садом',
    location: 'Московская область, Красногорск',
    price: '55 000 000 ₽',
    area: '300',
    image: 'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
    features: [
      '4 спальни',
      '3 ванные комнаты',
      'Большая кухня-столовая',
      'Кабинет',
      'Гараж',
      'Участок 20 соток'
    ]
  }
]

const showDetails = (house) => {
  selectedHouse.value = house
  dialog.value = true
}

const contactAgent = () => {
  // Здесь можно добавить логику связи с агентом
  alert('С вами свяжется наш агент в ближайшее время!')
  dialog.value = false
}
</script> 