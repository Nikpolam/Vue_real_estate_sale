<template>
  <v-container class="pt-16">
    <v-row>
      <v-col cols="12" class="text-center mb-4">
        <h2 class="text-h3 font-weight-bold primary--text">Коммерческая недвижимость</h2>
        <p class="text-subtitle-1 mt-2">Найдите идеальное помещение для вашего бизнеса</p>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" md="4" v-for="(property, index) in commercialProperties" :key="index">
        <v-card class="mx-auto" height="100%" elevation="2">
          <v-img
            :src="property.image"
            height="200"
            cover
          ></v-img>
          <v-card-text class="pa-4">
            <h3 class="text-h5 font-weight-bold mb-2">{{ property.title }}</h3>
            <p class="text-body-1 mb-2">{{ property.description }}</p>
            <div class="d-flex align-center mb-2">
              <v-icon size="20" color="primary" class="mr-1">mdi-map-marker</v-icon>
              <span>{{ property.location }}</span>
            </div>
            <div class="d-flex align-center mb-2">
              <v-icon size="20" color="primary" class="mr-1">mdi-currency-rub</v-icon>
              <span class="text-h6">{{ property.price }}</span>
            </div>
            <div class="d-flex align-center mb-2">
              <v-icon size="20" color="primary" class="mr-1">mdi-ruler-square</v-icon>
              <span>{{ property.area }} м²</span>
            </div>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="white"
                class="text-black"
                @click="showDetails(property)"
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
      <v-card v-if="selectedProperty">
        <v-img
          :src="selectedProperty.image"
          height="300"
          cover
        ></v-img>
        <v-card-text class="pa-4">
          <h3 class="text-h4 font-weight-bold mb-4">{{ selectedProperty.title }}</h3>
          <p class="text-body-1 mb-4">{{ selectedProperty.description }}</p>
          
          <div class="d-flex align-center mb-2">
            <v-icon size="20" color="primary" class="mr-2">mdi-map-marker</v-icon>
            <span>{{ selectedProperty.location }}</span>
          </div>
          
          <div class="d-flex align-center mb-2">
            <v-icon size="20" color="primary" class="mr-2">mdi-currency-rub</v-icon>
            <span class="text-h5">{{ selectedProperty.price }}</span>
          </div>
          
          <div class="d-flex align-center mb-2">
            <v-icon size="20" color="primary" class="mr-2">mdi-ruler-square</v-icon>
            <span>{{ selectedProperty.area }} м²</span>
          </div>

          <div class="mt-4">
            <h4 class="text-h6 mb-2">Характеристики:</h4>
            <ul class="pl-4">
              <li v-for="(feature, index) in selectedProperty.features" :key="index" class="mb-1">
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
const selectedProperty = ref(null)

const commercialProperties = [
  {
    title: 'Офисное помещение в бизнес-центре',
    description: 'Современное офисное помещение с панорамными окнами в престижном бизнес-центре',
    location: 'г. Москва, Центральный район',
    price: '45 000 000 ₽',
    area: '150',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
    features: [
      'Открытая планировка',
      'Система кондиционирования',
      'Высокоскоростной интернет',
      'Круглосуточная охрана',
      'Подземный паркинг',
      'Конференц-зал'
    ]
  },
  {
    title: 'Торговое помещение на первом этаже',
    description: 'Просторное помещение с витринами для розничной торговли',
    location: 'г. Москва, Северный район',
    price: '32 000 000 ₽',
    area: '120',
    image: 'https://images.unsplash.com/photo-1556911220-bff31c812dba?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
    features: [
      'Высокие потолки',
      'Панорамные витрины',
      'Складское помещение',
      'Грузовой лифт',
      'Охрана 24/7',
      'Высокая проходимость'
    ]
  },
  {
    title: 'Складской комплекс',
    description: 'Современный складской комплекс с развитой инфраструктурой',
    location: 'Московская область, Химки',
    price: '85 000 000 ₽',
    area: '500',
    image: 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
    features: [
      'Высокие потолки',
      'Погрузочные рампы',
      'Система пожаротушения',
      'Охрана территории',
      'Подъездные пути',
      'Таможенный пост'
    ]
  }
]

const showDetails = (property) => {
  selectedProperty.value = property
  dialog.value = true
}

const contactAgent = () => {
  // Здесь можно добавить логику связи с агентом
  alert('С вами свяжется наш агент в ближайшее время!')
  dialog.value = false
}
</script> 