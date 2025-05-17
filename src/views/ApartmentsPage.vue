<template>
  <v-container class="pt-16">
    <v-row>
      <v-col cols="12" class="text-center mb-4">
        <h2 class="text-h3 font-weight-bold primary--text">Квартиры</h2>
        <p class="text-subtitle-1 mt-2">Найдите свою идеальную квартиру</p>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" md="4" v-for="(apartment, index) in apartments" :key="index">
        <v-card class="mx-auto" height="100%" elevation="2">
          <v-img
            :src="apartment.image"
            height="200"
            cover
          ></v-img>
          <v-card-text class="pa-4">
            <h3 class="text-h5 font-weight-bold mb-2">{{ apartment.title }}</h3>
            <p class="text-body-1 mb-2">{{ apartment.description }}</p>
            <div class="d-flex align-center mb-2">
              <v-icon size="20" color="primary" class="mr-1">mdi-map-marker</v-icon>
              <span>{{ apartment.location }}</span>
            </div>
            <div class="d-flex align-center mb-2">
              <v-icon size="20" color="primary" class="mr-1">mdi-currency-rub</v-icon>
              <span class="text-h6">{{ apartment.price }}</span>
            </div>
            <div class="d-flex align-center mb-2">
              <v-icon size="20" color="primary" class="mr-1">mdi-ruler-square</v-icon>
              <span>{{ apartment.area }} м²</span>
            </div>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="white"
                class="text-black"
                @click="showDetails(apartment)"
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
      <v-card v-if="selectedApartment">
        <v-img
          :src="selectedApartment.image"
          height="300"
          cover
        ></v-img>
        <v-card-text class="pa-4">
          <h3 class="text-h4 font-weight-bold mb-4">{{ selectedApartment.title }}</h3>
          <p class="text-body-1 mb-4">{{ selectedApartment.description }}</p>
          
          <div class="d-flex align-center mb-2">
            <v-icon size="20" color="primary" class="mr-2">mdi-map-marker</v-icon>
            <span>{{ selectedApartment.location }}</span>
          </div>
          
          <div class="d-flex align-center mb-2">
            <v-icon size="20" color="primary" class="mr-2">mdi-currency-rub</v-icon>
            <span class="text-h5">{{ selectedApartment.price }}</span>
          </div>
          
          <div class="d-flex align-center mb-2">
            <v-icon size="20" color="primary" class="mr-2">mdi-ruler-square</v-icon>
            <span>{{ selectedApartment.area }} м²</span>
          </div>

          <div class="mt-4">
            <h4 class="text-h6 mb-2">Характеристики:</h4>
            <ul class="pl-4">
              <li v-for="(feature, index) in selectedApartment.features" :key="index" class="mb-1">
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
const selectedApartment = ref(null)

const apartments = [
  {
    title: 'Современная квартира в центре',
    description: 'Просторная квартира с современным ремонтом в центре города',
    location: 'г. Москва, Центральный район',
    price: '25 000 000 ₽',
    area: '85',
    image: 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
    features: [
      '2 спальни',
      '1 ванная комната',
      'Просторная гостиная',
      'Отдельная кухня',
      'Парковочное место',
      'Охрана 24/7'
    ]
  },
  {
    title: 'Квартира с панорамными окнами',
    description: 'Светлая квартира с панорамными окнами и видом на город',
    location: 'г. Москва, Северный район',
    price: '18 500 000 ₽',
    area: '65',
    image: 'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
    features: [
      '1 спальня',
      '1 ванная комната',
      'Панорамные окна',
      'Встроенная кухня',
      'Подземный паркинг',
      'Фитнес-центр'
    ]
  },
  {
    title: 'Семейная квартира в новостройке',
    description: 'Просторная квартира для семьи в современном жилом комплексе',
    location: 'г. Москва, Западный район',
    price: '32 000 000 ₽',
    area: '120',
    image: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
    features: [
      '3 спальни',
      '2 ванные комнаты',
      'Большая кухня-столовая',
      'Детская площадка',
      'Два парковочных места',
      'Развитая инфраструктура'
    ]
  }
]

const showDetails = (apartment) => {
  selectedApartment.value = apartment
  dialog.value = true
}

const contactAgent = () => {
  // Здесь можно добавить логику связи с агентом
  alert('С вами свяжется наш агент в ближайшее время!')
  dialog.value = false
}
</script> 