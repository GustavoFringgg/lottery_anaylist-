<script setup lang="ts">
const menuOpen = ref(false)
const menuItems = [
  { label: "今彩539", logo: "/images/ham_logo/539.png" },
  { label: "大樂透", logo: "/images/ham_logo/big-lotto.png" },
  { label: "威力彩", logo: "/images/ham_logo/power-lotto.png" },
  { label: "BINGO BINGO", logo: "/images/ham_logo/bingo.png" },
  { label: "49樂合彩", logo: "/images/ham_logo/49lotto.png" },
  { label: "39樂合彩", logo: "/images/ham_logo/39lotto.png" },
  { label: "3星彩", logo: "/images/ham_logo/3star.png" },
  { label: "4星彩", logo: "/images/ham_logo/4star.png" },
]

const navRef = ref<HTMLElement | null>(null)

function handleOutsideClick(e: MouseEvent) {
  if (menuOpen.value && !navRef.value?.contains(e.target as Node)) {
    menuOpen.value = false
  }
}

onMounted(() => document.addEventListener("click", handleOutsideClick))
onUnmounted(() => document.removeEventListener("click", handleOutsideClick))
</script>

<template>
  <div class="min-h-screen bg-cream relative">
    <!-- Header -->
    <header
      class="py-2.5 relative flex items-center justify-center sm:h-[104px] h-[59px]"
      style="background-color: #59adbc"
    >
      <img
        src="../public/images/logos/539lotto_header.png"
        alt="今彩539"
        class="h-[44px] sm:h-[90px] w-auto object-contain"
      />
      <!-- 漢堡選單按鈕 -->
      <button
        ref="btnRef"
        class="absolute right-4 top-1/2 -translate-y-1/2 rounded-full flex flex-col items-center justify-center gap-1.5 w-[35px] h-[35px] sm:w-[71px] sm:h-[71px]"
        style="background-color: #ffe868"
        aria-label="選單"
        @click.stop="menuOpen = !menuOpen"
      >
        <template v-if="menuOpen">
          <span class="text-xl sm:text-3xl font-bold leading-none" style="color: #00c296">✕</span>
        </template>
        <template v-else>
          <span class="block w-5 h-0.5 sm:w-9 sm:h-1 rounded" style="background-color: #00c296"></span>
          <span class="block w-5 h-0.5 sm:w-9 sm:h-1 rounded" style="background-color: #00c296"></span>
          <span class="block w-5 h-0.5 sm:w-9 sm:h-1 rounded" style="background-color: #00c296"></span>
        </template>
      </button>
    </header>

    <!-- 展開選單 -->
    <Transition name="menu">
      <nav
        v-if="menuOpen"
        ref="navRef"
        class="absolute left-0 right-0 z-50 top-[59px] sm:top-[104px]"
        style="background-color: #0b879e"
      >
        <ul>
          <li
            v-for="item in menuItems"
            :key="item.label"
            class="border-b last:border-b-0"
            style="border-color: rgba(255, 255, 255, 0.2)"
          >
            <button
              class="w-full flex items-center justify-center py-[17px] text-2xl font-bold menu-item px-6"
              style="color: #ffe868"
              @click="menuOpen = false"
            >
              <div class="w-12 sm:w-14 flex justify-center shrink-0">
                <img :src="item.logo" :alt="item.label" class="w-8 h-8 sm:w-10 sm:h-10 object-contain" />
              </div>
              <div class="w-40 sm:w-48 text-center">{{ item.label }}</div>
            </button>
          </li>
        </ul>
      </nav>
    </Transition>

    <!-- Ad Carousel -->
    <AdCarousel />

    <!-- Main content -->
    <main class="mx-auto max-w-[1540px] px-2 py-3 sm:px-4">
      <slot />
    </main>

    <!-- Ad Banner -->
    <!-- <div class="flex justify-center mb-4">
      <img src="/images/logos/adExample.png" alt="廣告" class="w-full max-w-[1170px] h-auto" />
    </div> -->

    <footer class="py-4 text-center text-xs text-white" style="background-color: #59adbc"></footer>
  </div>
</template>

<style scoped>
.menu-enter-active,
.menu-leave-active {
  transition: all 0.25s ease;
  overflow: hidden;
}
.menu-enter-from,
.menu-leave-to {
  opacity: 0;
  max-height: 0;
}
.menu-enter-to,
.menu-leave-from {
  opacity: 1;
  max-height: 600px;
}

.menu-item:hover {
  background-color: rgba(255, 255, 255, 0.1);
}
</style>
