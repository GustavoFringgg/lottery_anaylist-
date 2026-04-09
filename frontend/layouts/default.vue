<template>
  <div class="min-h-screen bg-gray-950">
    <!-- Nav -->
    <nav class="sticky top-0 z-50 border-b border-white/10 bg-gray-950/80 backdrop-blur-md">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="flex h-14 items-center justify-between">
          <div class="flex items-center gap-2">
            <span class="text-xl font-bold text-brand-500">台彩分析</span>
            <span class="rounded-full bg-brand-500/20 px-2 py-0.5 text-xs text-brand-500">LIVE</span>
          </div>
          <div class="flex items-center gap-6 text-sm text-gray-400">
            <NuxtLink to="/" class="hover:text-white transition-colors">即時開獎</NuxtLink>
            <NuxtLink to="/history" class="hover:text-white transition-colors">歷史查詢</NuxtLink>
            <NuxtLink to="/analysis" class="hover:text-white transition-colors">統計分析</NuxtLink>
          </div>
        </div>
      </div>
    </nav>

    <!-- Main -->
    <main class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
      <slot />
    </main>

    <!-- Footer -->
    <footer class="border-t border-white/10 py-6 text-center text-sm text-gray-600">
      © 2026 台彩分析 · 資料僅供參考
    </footer>
  </div>
</template>
