<template>
  <div class="min-h-screen bg-cream">
    <!-- Header -->
    <header class="py-2.5 text-center" style="background-color: #59ADBC;">
      <span class="text-white font-bold" style="font-size: 40px;">LOGO</span>
    </header>

    <!-- Main content -->
    <main class="mx-auto max-w-[1200px] px-2 py-3 sm:px-4">
      <slot />
    </main>

    <!-- Footer -->
    <footer class="py-4 text-center text-xs text-gray-500">
      Copyright ©Liyaodata All Rights Reserved.
    </footer>
  </div>
</template>
