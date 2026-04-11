<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<!-- 使用者訪問 /
    → app.vue 渲染
      → NuxtLayout 載入 layouts/default.vue（Header + Footer）
        → NuxtPage 載入 pages/index.vue（首頁內容） -->
