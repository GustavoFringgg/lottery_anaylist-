export default defineNuxtConfig({
  compatibilityDate: '2026-04-09',
  devtools: { enabled: true },

  modules: ['@nuxtjs/tailwindcss'],

  css: ['~/assets/css/main.css'],

  typescript: {
    strict: true,
  },

  runtimeConfig: {
    public: {
      apiBase: process.env.API_BASE_URL || 'http://localhost:8000',
      wsBase: process.env.WS_BASE_URL || 'ws://localhost:8000',
    },
  },

  app: {
    head: {
      title: '台彩分析 - 即時開獎資訊',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: '全台最快即時台彩開獎資訊、歷史數據分析、號碼統計' },
      ],
      link: [
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap' },
      ],
    },
  },

  ssr: true,
})
