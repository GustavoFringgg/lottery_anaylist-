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

const pad = (n: number) => String(n).padStart(2, '0')

// --- Mock Data ---
const games5min = [
  {
    name: '今彩539',
    nameColor: '#e53935',
    draw_term: '115000079',
    draw_date: '115/03/30',
    draw_time: '15:00',
    next_draw: '115/04/01',
    numbers: [3, 29, 33, 27, 30],
    special_number: null,
  },
  {
    name: '威力彩',
    nameColor: '#7b1fa2',
    draw_term: '115000026',
    draw_date: '115/03/27',
    draw_time: '21:30',
    next_draw: '115/03/31',
    numbers: [3, 29, 33, 27, 30, 17],
    special_number: 9,
  },
]

const gamesDaily = [
  {
    name: '大樂透',
    nameColor: '#e65100',
    draw_term: '115000030',
    draw_date: '115/03/27',
    draw_time: '21:30',
    next_draw: '115/03/31',
    numbers: [3, 29, 33, 27, 30, 17],
    special_number: 9,
  },
  {
    name: '49樂合彩',
    nameColor: '#e65100',
    draw_term: '115000030',
    draw_date: '115/03/27',
    draw_time: '21:30',
    next_draw: '115/03/31',
    numbers: [3, 29, 33, 27],
    special_number: 9,
  },
  {
    name: '今彩539',
    nameColor: '#e53935',
    draw_term: '115000079',
    draw_date: '115/03/30',
    draw_time: '15:00',
    next_draw: '115/04/01',
    numbers: [3, 29, 33, 27, 30],
    special_number: null,
  },
  {
    name: '39樂合彩',
    nameColor: '#f57c00',
    draw_term: '115000079',
    draw_date: '115/03/30',
    draw_time: '15:00',
    next_draw: '115/04/01',
    numbers: [29, 27, 3, 33],
    special_number: null,
  },
  {
    name: '3星彩',
    nameColor: '#c8a000',
    draw_term: '115000079',
    draw_date: '115/03/30',
    draw_time: '13:30',
    next_draw: '115/04/01',
    numbers: [3, 2, 9],
    special_number: null,
  },
  {
    name: '4星彩',
    nameColor: '#e65100',
    draw_term: '115000079',
    draw_date: '115/03/30',
    draw_time: '13:30',
    next_draw: '115/04/01',
    numbers: [3, 2, 9, 7],
    special_number: null,
  },
]

useHead({ title: '台彩分析 - 即時開獎資訊' })
</script>

<template>
  <div class="space-y-3">
    <!-- Countdown Banner -->
    <div class="bg-white rounded-lg shadow-sm border border-gray-100 px-4 py-3 flex items-center justify-between flex-wrap gap-2">
      <span class="text-base font-bold text-red-600">今彩 539</span>
      <div class="text-sm text-gray-700">
        開獎直播倒數：
        <span class="font-bold text-orange-600">
          {{ days }}天 {{ pad(hours) }}時 {{ pad(minutes) }}分 {{ pad(seconds) }}秒
        </span>
      </div>
    </div>

    <!-- 每五分鐘開獎一次 -->
    <div class="section-banner">每五分鐘開獎一次</div>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
      <LotteryGameCard
        v-for="game in games5min"
        :key="game.name"
        :game="game"
      />
    </div>

    <!-- 每日開獎一次 -->
    <div class="section-banner">每日開獎一次</div>
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
      <LotteryGameCard
        v-for="game in gamesDaily"
        :key="game.name + game.draw_term"
        :game="game"
      />
    </div>
  </div>
</template>
