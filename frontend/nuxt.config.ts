export default defineNuxtConfig({
  compatibilityDate: '2026-04-09',
  devtools: { enabled: true },

  modules: ['@nuxtjs/tailwindcss'],

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
        {
          name: 'description',
          content: '全台最快即時台彩開獎資訊、歷史數據分析、號碼統計',
        },
      ],
    },
  },

  ssr: true,

  nitro: {
    preset: 'vercel-edge',
  },
})
