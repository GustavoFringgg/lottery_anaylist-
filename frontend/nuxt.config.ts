export default defineNuxtConfig({
  compatibilityDate: "2026-04-09", //告訴 Nuxt「以這個日期的版本行為為準」，避免 Nuxt 升版後自動採用破壞性的新預設值
  devtools: { enabled: true }, //開啟右下角的 Nuxt DevTools（就是你截圖看到的那個工具列）

  modules: ["@nuxtjs/tailwindcss"], //裡載入了 Tailwind CSS 的 Nuxt 整合版

  css: ["~/assets/css/main.css"], // 全域載入 CSS，你的 main.css（包含 Tailwind 的 @tailwind base/components/utilities 和自訂 class）在每個頁面都會生效。

  typescript: {
    strict: true //，等同於 tsconfig.json 裡的 strict: true。
  },

  runtimeConfig: {
    apiKey: process.env.NUXT_API_KEY || "",  // server only (prod SSR)
    public: {
      apiBase: process.env.API_BASE_URL || "https://lottery-anaylist.onrender.com",
      ...(process.env.NODE_ENV === 'development' && { apiKey: process.env.NUXT_PUBLIC_API_KEY || "" })
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
        { name: "description", content: "提供今彩539、大樂透、威力彩、39樂合彩、49樂合彩、3星彩、4星彩、BingoBingo 即時開獎號碼，歷史數據分析與號碼統計，幫助彩迷快速掌握開獎資訊。" },
        { name: "keywords", content: "大樂透,威力彩,今彩539,台彩,全民i彩券,BingoBingo,39樂合彩,49樂合彩,3星彩,4星彩,開獎號碼,號碼統計,歷史開獎,數據分析" },
        { name: "robots", content: "follow, index, max-snippet:-1, max-image-preview:large" },
        { name: "google-site-verification", content: "6ITddVFWHs0TBPCXs_lf8yG-U0C7AEqyz1jrbZ_3_Ko" },
        { property: "og:locale", content: "zh_TW" },
        { property: "og:type", content: "website" },
        { property: "og:site_name", content: "台彩分析" },
        { property: "og:title", content: "台彩分析 - 即時開獎資訊" },
        { property: "og:description", content: "提供今彩539、大樂透、威力彩、39樂合彩、49樂合彩、3星彩、4星彩、BingoBingo 即時開獎號碼，歷史數據分析與號碼統計。" },
        { property: "og:url", content: "https://www.539lto.co/" },
        { property: "og:image", content: "https://www.539lto.co/images/logos/favicon.png" },
        { name: "twitter:card", content: "summary_large_image" },
        { name: "twitter:title", content: "台彩分析 - 即時開獎資訊" },
        { name: "twitter:description", content: "提供今彩539、大樂透、威力彩、39樂合彩、49樂合彩、3星彩、4星彩、BingoBingo 即時開獎號碼，歷史數據分析與號碼統計。" },
        { name: "twitter:image", content: "https://www.539lto.co/images/logos/favicon.png" },
      ],
      link: [
        { rel: "icon", type: "image/png", href: "/images/logos/favicon.png" },
        { rel: "canonical", href: "https://www.539lto.co/" },
      ],
      script: [
        {
          src: "https://www.googletagmanager.com/gtag/js?id=G-Z5TWHGFH4L",
          async: true,
        },
        {
          innerHTML: `
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-Z5TWHGFH4L');
          `,
        },
      ],
    }
  },

  ssr: process.env.NODE_ENV !== 'development'
})
