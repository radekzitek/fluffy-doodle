import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  app: {
    head: {
      title: 'Home',
      titleTemplate: 'Doodle: %s',
    },
  },
  $development: {
    app: {
      head: {
        titleTemplate: 'Doodle[DEV]: %s',
      },
    },
    devtools: { enabled: true },
  },
  $test: {
    app: {
      head: {
        titleTemplate: 'Doodle[TEST]: %s',
      },
    },
    devtools: { enabled: false },
  },
  $production: {
    app: {
      head: {
        titleTemplate: 'Doodle[PROD]: %s',
      },
    },
    devtools: { enabled: false },
  },
})
