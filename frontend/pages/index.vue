<script setup lang="ts">
import type { CardData } from "~/types/index"

// --- Countdown Timer ---
const days = ref(0)
const hours = ref(0)
const minutes = ref(0)
const seconds = ref(0)

//
// const updateCountdown = () => {
//   const now = new Date()
//   const target = new Date()
//   target.setHours(21, 30, 0, 0)
//   if (target <= now) target.setDate(target.getDate() + 1)
//   const diff = target.getTime() - now.getTime()
//   days.value = Math.floor(diff / 86400000)
//   hours.value = Math.floor((diff % 86400000) / 3600000)
//   minutes.value = Math.floor((diff % 3600000) / 60000)
//   seconds.value = Math.floor((diff % 60000) / 1000)
// }
// onMounted(() => {
//   updateCountdown()
//   const timer = setInterval(updateCountdown, 1000)

//   onUnmounted(() => clearInterval(timer))
// })

// const pad = (n: number) => String(n).padStart(2, "0")

const todayWeekday = new Date().getDay() //0~6
const isDrawTody = (game: CardData) => game.draw_days?.includes(todayWeekday) ?? false
const { featured: gamesFeatured, grid: gamesGrid } = useLotteryLatest()
const { bingoCard } = useBingoLatest()

useHead({ title: "台彩分析 - 即時開獎資訊" }) //頁面標題 適合SEO
</script>

<template>
  <div class="flex flex-col w-full max-w-[1200px] mx-auto">
    <AdCarousel />
  </div>
  <div class="space-y-3 flex flex-col w-full max-w-[1200px] mx-auto px-2 sm:px-4">
    <!-- <div
      class="w-full flex flex-col sm:flex-row items-center sm:justify-center px-6 py-4 sm:py-0 gap-x-10 mb-[26px]"
      style="
        min-height: 151px;
        background: linear-gradient(180deg, #9ce2f9 0%, #daf6f0 100%);
        box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
        border-radius: 5px;
      "
    >
      <img src="../public/images/logos/jinchoi539.png" alt="今彩539" width="246" height="104" class="object-contain" />
      <div
        class="text-center"
        style="font-family: &quot;Inter&quot;, sans-serif; font-weight: 700; color: #626262"
        :style="{ fontSize: 'clamp(16px, 2.5vw, 36px)' }"
      >
        開獎直播倒數：{{ days }} 天 {{ pad(hours) }} 時 {{ pad(minutes) }} 分 {{ pad(seconds) }} 秒
      </div>
    </div> -->
    <LotteryGameCard v-for="game in gamesFeatured" :key="game.name + game.draw_term" :game="game" :full-width="true">
      <DrawDateButton class="mt-[5px] sm:mt-[10px]" v-if="isDrawTody(game)">今日開獎</DrawDateButton>
    </LotteryGameCard>
    <BingoBingoCard
      v-if="bingoCard"
      :draw_term="bingoCard.draw_term"
      :draw_date="bingoCard.draw_date"
      :draw_time="bingoCard.draw_time"
      :next_draw_date="bingoCard.next_draw_date"
      :next_draw_time="bingoCard.next_draw_time"
      :numbers="bingoCard.numbers"
      :special_number="bingoCard.special_number"
      :super_prize="bingoCard.special_number"
      :guess_big_small="bingoCard.guess_big_small"
      :guess_odd_even="bingoCard.guess_odd_even"
    >
      <DrawDateButton class="mt-[5px] sm:mt-[10px]">每五分鐘開獎</DrawDateButton>
    </BingoBingoCard>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
      <LotteryGameCard v-for="game in gamesGrid" :key="game.name + game.draw_term" :game="game">
        <DrawDateButton class="mt-[5px] sm:mt-[10px]" v-if="isDrawTody(game)">今日開獎</DrawDateButton>
      </LotteryGameCard>
    </div>
  </div>
</template>
