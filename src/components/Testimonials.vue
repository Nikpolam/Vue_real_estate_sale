<template>
  <v-container class="py-16">
    <v-row>
      <v-col cols="12" class="text-center mb-8">
        <h2 class="text-h3 font-weight-bold text-black">Отзывы наших клиентов</h2>
        <p class="text-subtitle-1 mt-2 text-black">Что говорят о нас люди, которые уже воспользовались нашими услугами</p>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" md="4" v-for="(testimonial, index) in testimonials" :key="index">
        <v-card class="mx-auto" height="100%" elevation="2">
          <v-card-text class="pa-3">
            <div class="d-flex align-center mb-2">
              <v-avatar size="48" color="#D4B08C" class="mr-3">
                <v-img :src="testimonial.avatar"></v-img>
              </v-avatar>
              <div>
                <h4 class="text-subtitle-1 font-weight-bold" style="color: #D4B08C">{{ testimonial.name }}</h4>
                <p class="text-caption">{{ testimonial.date }}</p>
              </div>
            </div>
            <p class="text-body-1">{{ testimonial.text }}</p>
            <div class="d-flex mt-2">
              <v-rating
                v-model="testimonial.rating"
                color="#D4B08C"
                dense
                half-increments
                readonly
                size="20"
              ></v-rating>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
const testimonials = [
  {
    name: 'Анна Петрова',
    date: '15 марта 2024',
    text: 'Очень довольна сервисом! Нашли идеальную квартиру в кратчайшие сроки. Специалисты проявили профессионализм и внимание к деталям.',
    rating: 5,
    avatar: 'https://randomuser.me/api/portraits/women/1.jpg'
  },
  {
    name: 'Михаил Иванов',
    date: '10 марта 2024',
    text: 'Отличный сервис! Все документы оформили быстро и без лишних хлопот. Рекомендую!',
    rating: 4.5,
    avatar: 'https://randomuser.me/api/portraits/men/1.jpg'
  },
  {
    name: 'Елена Сидорова',
    date: '5 марта 2024',
    text: 'Профессиональный подход к каждому клиенту. Помогли найти именно то, что я искала.',
    rating: 5,
    avatar: 'https://randomuser.me/api/portraits/women/2.jpg'
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