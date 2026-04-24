<template>
  <div class="min-h-screen bg-cream">
    <!-- Header -->
    <header
      class="py-2.5 relative flex items-center justify-center sm:h-[104px] h-[59px]"
      style="background-color: #59adbc"
    >
      <!-- <img
        src="../public/images/logos/539lotto_header.png"
        alt="今彩539"
        width="246"
        height="104"
        class="object-contain"
      /> -->

      <!-- 手機版漢堡選單 -->
      <button
        class="sm:hidden absolute right-4 top-1/2 -translate-y-1/2 w-9 h-9 rounded-full flex flex-col items-center justify-center gap-1.5"
        style="background-color: #ffe868"
        aria-label="選單"
      >
        <span class="block w-5 h-0.5 rounded" style="background-color: #00c296"></span>
        <span class="block w-5 h-0.5 rounded" style="background-color: #00c296"></span>
        <span class="block w-5 h-0.5 rounded" style="background-color: #00c296"></span>
      </button>
    </header>

    <!-- Main content -->
    <main class="mx-auto max-w-[1540px] px-2 py-3 sm:px-4">
      <slot />
    </main>

    <footer class="py-4 text-center text-xs text-white" style="background-color: #59adbc"></footer>
  </div>
</template>
