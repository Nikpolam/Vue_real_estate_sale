/**
 * router/index.js
 */

import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import ContactsPage from '../views/ContactsPage.vue'
import HousesPage from '../views/HousesPage.vue'
import ApartmentsPage from '../views/ApartmentsPage.vue'
import CommercialPage from '../views/CommercialPage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/contacts',
    name: 'contacts',
    component: ContactsPage
  },
  {
    path: '/houses',
    name: 'houses',
    component: HousesPage
  },
  {
    path: '/apartments',
    name: 'apartments',
    component: ApartmentsPage
  },
  {
    path: '/commercial',
    name: 'commercial',
    component: CommercialPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Workaround for https://github.com/vitejs/vite/issues/11804
router.onError((err, to) => {
  if (err?.message?.includes?.('Failed to fetch dynamically imported module')) {
    if (!localStorage.getItem('vuetify:dynamic-reload')) {
      console.log('Reloading page to fix dynamic import error')
      localStorage.setItem('vuetify:dynamic-reload', 'true')
      location.assign(to.fullPath)
    } else {
      console.error('Dynamic import error, reloading page did not fix it', err)
    }
  } else {
    console.error(err)
  }
})

router.isReady().then(() => {
  localStorage.removeItem('vuetify:dynamic-reload')
})

export default router
