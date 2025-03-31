<template>
  <v-container class="py-4 primary">
    <v-row>
      <v-col cols="12" class="text-center mb-4">
        <h2 class="text-h3 font-weight-bold text-white">Контакты</h2>
        <p class="text-subtitle-1 mt-2 text-white">Свяжитесь с нами любым удобным способом</p>
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-card class="mx-auto" elevation="2">
          <v-card-text class="pa-4">
            <div class="d-flex align-center mb-4">
              <v-icon size="24" color="primary" class="mr-2">mdi-phone</v-icon>
              <span class="text-body-1">+7 (XXX) XXX-XX-XX</span>
            </div>
            
            <div class="d-flex align-center mb-4">
              <v-icon size="24" color="primary" class="mr-2">mdi-email</v-icon>
              <span class="text-body-1">info@example.com</span>
            </div>
            
            <div class="d-flex align-center mb-4">
              <v-icon size="24" color="primary" class="mr-2">mdi-map-marker</v-icon>
              <span class="text-body-1">г. Москва, ул. Примерная, д. 123</span>
            </div>

            <div class="text-center mt-6">
              <h3 class="text-h6 mb-4">Мы в социальных сетях</h3>
              <div class="d-flex justify-center">
                <v-btn
                  v-for="(social, index) in socials"
                  :key="index"
                  :href="social.link"
                  target="_blank"
                  icon
                  class="mx-2"
                  color="primary"
                  size="large"
                >
                  <v-icon>{{ social.icon }}</v-icon>
                </v-btn>
              </div>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
const socials = [
  {
    icon: 'mdi-vk',
    link: 'https://vk.com/your_company'
  },
  {
    icon: 'mdi-telegram',
    link: 'https://t.me/your_company'
  },
  {
    icon: 'mdi-whatsapp',
    link: 'https://wa.me/your_number'
  },
  {
    icon: 'mdi-instagram',
    link: 'https://instagram.com/your_company'
  }
]
</script> 