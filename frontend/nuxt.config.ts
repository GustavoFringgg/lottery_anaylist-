export default defineNuxtConfig({
  compatibilityDate: "2026-04-09", //告訴 Nuxt「以這個日期的版本行為為準」，避免 Nuxt 升版後自動採用破壞性的新預設值
  devtools: { enabled: true }, //開啟右下角的 Nuxt DevTools（就是你截圖看到的那個工具列）

  modules: ["@nuxtjs/tailwindcss"], //裡載入了 Tailwind CSS 的 Nuxt 整合版

  css: ["~/assets/css/main.css"], // 全域載入 CSS，你的 main.css（包含 Tailwind 的 @tailwind base/components/utilities 和自訂 class）在每個頁面都會生效。

  typescript: {
    strict: true //，等同於 tsconfig.json 裡的 strict: true。
  },

  runtimeConfig: {
    apiKey: process.env.NUXT_API_KEY || "",  // server only
    public: {
      apiBase: process.env.API_BASE_URL || "https://lottery-anaylist.onrender.com"
    }
  },
  /*   環境變數管理，這是 Nuxt 特有的。
  - public 底下的值 → 前後端都看得到（會暴露給瀏覽器）
  - 如果放在 public 外面 → 只有 server 看得到（適合放 API secret）

  在元件裡用 useRuntimeConfig().public.apiBase 來取值。 */

  // app index.html head 內容
  app: {
    head: {
      title: "台彩分析 - 即時開獎資訊",
      meta: [
        { charset: "utf-8" },
        { name: "viewport", content: "width=device-width, initial-scale=1" },
        { name: "description", content: "全台最快即時台彩開獎資訊、歷史數據分析、號碼統計" }
      ],
      link: [{ rel: "icon", type: "image/png", href: "/images/logos/favicon.png" }]
    }
  },

  ssr: true //開啟ssr模式
})
