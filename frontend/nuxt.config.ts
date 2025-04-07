// https://nuxt.com/docs/api/configuration/nuxt-config
import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

export default defineNuxtConfig({
  app: {
    head: {
      title: 'DinoScan AI',
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/t_rex_icon.png' }
      ]
    }
  },
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  runtimeConfig: {
    public: {
      api: process.env.NUXT_PUBLIC_API
    }
  },
  build: {
    transpile: ['vuetify']
  },
  routeRules: {
    '/api/**': { proxy: 'http://127.0.0.1:5000/api/**' },
    '/strapi/**': { proxy: 'http://127.0.0.1:1337/api/**' },
    '/discourse/**': { proxy: 'http://192.168.0.104:4200/**' }
  },
  modules: [
    (_options, nuxt) => {
      nuxt.hooks.hook('vite:extendConfig', (config) => {
        // @ts-expect-error
        config.plugins.push(vuetify({ autoImport: true }))
      })
    },
  ],
  vite: {
    vue: {
      template: {
        transformAssetUrls,
      }
    }
  }
})
