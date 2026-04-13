<script setup lang="ts">
// --- Countdown Timer ---
const days = ref(0)
const hours = ref(0)
const minutes = ref(0)
const seconds = ref(0)

const updateCountdown = () => {
  const now = new Date()
  const target = new Date()
  target.setHours(21, 30, 0, 0)
  if (target <= now) target.setDate(target.getDate() + 1)
  const diff = target.getTime() - now.getTime()
  days.value = Math.floor(diff / 86400000)
  hours.value = Math.floor((diff % 86400000) / 3600000)
  minutes.value = Math.floor((diff % 3600000) / 60000)
  seconds.value = Math.floor((diff % 60000) / 1000)
}

onMounted(() => {
  updateCountdown()
  const timer = setInterval(updateCountdown, 1000)
  onUnmounted(() => clearInterval(timer))
})

const pad = (n: number) => String(n).padStart(2, "0")

// --- Mock Data（未來換成 useFetch('/api/games')）---
//  const { data } = await useFetch('/api/games')
import { mockGames } from "~/data/mockGames"
const { twiceWeekly: gamesTwiceWeekly, daily: gamesDaily } = mockGames

useHead({ title: "台彩分析 - 即時開獎資訊" }) //頁面標題 適合SEO
</script>

<template>
  <div class="space-y-3 flex flex-col w-full max-w-[1200px] mx-auto px-2 sm:px-4">
    <!-- Countdown Banner -->
    <div
      class="w-full flex flex-col sm:flex-row items-center justify-center sm:justify-around px-6 py-4 sm:py-0 gap-3 mb-[26px]"
      style="
        min-height: 151px;
        background: linear-gradient(180deg, #9ce2f9 0%, #daf6f0 100%);
        box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
        border-radius: 5px;
      "
    >
      <img src="/images/logos/jinchoi539.png" alt="今彩539" width="246" height="104" class="object-contain" />
      <div
        class="text-center"
        style="font-family: &quot;Inter&quot;, sans-serif; font-weight: 700; color: #626262"
        :style="{ fontSize: 'clamp(16px, 2.5vw, 36px)' }"
      >
        開獎直播倒數：{{ days }} 天 {{ pad(hours) }} 時 {{ pad(minutes) }} 分 {{ pad(seconds) }} 秒
      </div>
    </div>

    <!-- 每五分鐘開獎一次 -->
    <SectionBanner>每五分鐘開獎一次</SectionBanner>
    <BingoBingoCard
      draw_term="115018164"
      draw_date="115/03/31(二)"
      draw_time="15:00"
      next_draw_date="115/03/31(二)"
      next_draw_time="15:10"
      :numbers="[13, 27, 28, 41, 26, 16, 22, 31, 2, 36, 27, 10, 9, 6, 24, 12, 37, 25, 22]"
      :special_number="1"
      :super_prize="1"
      guess_big_small="-"
      guess_odd_even="單"
    />

    <!-- 每週開獎兩次 -->
    <div class="mt-[26px]">
      <SectionBanner>每週開獎兩次</SectionBanner>
    </div>
    <!-- 威力彩 全寬 -->
    <LotteryGameCard :game="gamesTwiceWeekly[0]" :full-width="true" />
    <!-- 大樂透 + 49樂合彩 -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
      <LotteryGameCard :game="gamesTwiceWeekly[1]" />
      <LotteryGameCard :game="gamesTwiceWeekly[2]" />
    </div>

    <!-- 每日開獎一次 -->
    <div class="mt-[26px]">
      <SectionBanner>每日開獎一次</SectionBanner>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
      <LotteryGameCard v-for="game in gamesDaily" :key="game.name + game.draw_term" :game="game" />
    </div>
  </div>
</template>
