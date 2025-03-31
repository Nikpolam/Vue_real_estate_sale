<template>
  <v-main class="main-background pa-0">
    <v-container class="pt-16">
      <WelcomeCard ref="welcomeCard" />
      <Features ref="features" />
      <Testimonials ref="testimonials" />
      <registration-form ref="registrationForm"></registration-form>
    </v-container>
  </v-main>
</template>

<script setup>
import WelcomeCard from '../Card.vue'
import RegistrationForm from '../Vee-validate.vue'
import Features from '../components/Features.vue'
import Testimonials from '../components/Testimonials.vue'
</script>

<style>
.main-background {
  background: linear-gradient(135deg, #f3e5dc 0%, #e6d5cc 100%);
  min-height: 100vh;
}
</style> 