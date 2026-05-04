<script setup lang="ts">
const slides = [
  {
    desktop: "/images/ads/ad1-desktop.png",
    mobile: "/images/ads/ad1-mobile.png",
    type: "external",
    url: "https://165.npa.gov.tw/#/promotion",
    name: "test"
  },
  {
    desktop: "/images/ads/ad2-desktop.png",
    mobile: "/images/ads/ad2-mobile.png",
    type: "internal",
    url: "/",
    num: 1
  }
]

// 紀錄目前是第幾張 0 = 第1張 / 1 = 第2張
const current = ref(0)

let timer: ReturnType<typeof setInterval>

// 設定 setInterval setting
function startTimer() {
  timer = setInterval(() => {
    current.value = (current.value + 1) % slides.length
  }, 5000)
}

function handleClick(slide: (typeof slides)[number]) {
  if (slide.type === "external") {
    window.open(slide.url, "_blank", "noopener,noreferrer")
  } else {
    navigateTo(slide.url)
  }
}

onMounted(startTimer)
onUnmounted(() => clearInterval(timer))
</script>

<template>
  <div class="flex justify-center px-2 sm:px-4 py-3">
    <div
      class="relative w-[350px] h-[210px] sm:w-full sm:max-w-[1170px] sm:h-[355px] overflow-hidden cursor-pointer rounded shadow-md"
      style="border-radius: 5px"
    >
      <TransitionGroup name="fade">
        <div
          v-for="(slide, i) in slides"
          v-show="current === i"
          :key="i"
          class="absolute inset-0 w-full h-full"
          @click="handleClick(slide)"
        >
          <picture class="w-full h-full">
            <source media="(min-width: 640px)" :srcset="slide.desktop" />
            <img :src="slide.mobile" :alt="`廣告 ${i + 1}`" class="w-full h-full object-cover" />
          </picture>
        </div>
      </TransitionGroup>

      <div class="absolute bottom-2 left-1/2 -translate-x-1/2 flex gap-2">
        <button
          v-for="(_, i) in slides"
          :key="i"
          class="w-2 h-2 rounded-full transition"
          :style="current === i ? 'background:#fff' : 'background:rgba(255,255,255,0.4)'"
          @click.stop="current = i"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
