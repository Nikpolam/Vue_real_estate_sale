<template>
  <v-container class="pt-16">
    <v-row>
      <v-col cols="12" class="text-center mb-4">
        <h2 class="text-h3 font-weight-bold primary--text">Наши услуги</h2>
        <p class="text-subtitle-1 mt-2">Выберите интересующий вас раздел</p>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" md="4" v-for="(card, index) in cards" :key="index">
        <v-card class="mx-auto" height="100%" elevation="2">
          <v-img
            :src="card.image"
            height="200"
            cover
          ></v-img>
          <v-card-text class="pa-4">
            <h3 class="text-h5 font-weight-bold mb-2">{{ card.title }}</h3>
            <p class="text-body-1 mb-4">{{ card.description }}</p>
            <v-btn
              color="#D4B08C"
              class="text-black"
              block
              :to="card.route"
            >
              Подробнее
            </v-btn>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
const cards = [
  {
    title: 'Частные дома',
    description: 'Продажа и аренда частных домов в Московской области',
    image: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
    route: '/houses'
  },
  {
    title: 'Квартиры',
    description: 'Продажа и аренда квартир в Москве и области',
    image: 'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
    route: '/apartments'
  },
  {
    title: 'Коммерческая недвижимость',
    description: 'Продажа и аренда коммерческих помещений',
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80',
    route: '/commercial'
  }
]
</script>

<style scoped>
.on-hover {
  transform: translateY(-5px);
  transition: all 0.3s ease;
}

.v-card {
  transition: all 0.3s ease;
  height: 100%;
}

.v-card-title {
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
  border-radius: 8px;
  margin: 16px;
  display: inline-block;
}
</style>
