<script setup lang="ts">
interface Props {
  draw_term: string
  draw_date: string
  draw_time: string
  next_draw_date: string
  next_draw_time: string
  numbers: number[]
  special_number: number | null
  super_prize: number | null
  guess_big_small: string
  guess_odd_even: string
}

withDefaults(defineProps<Props>(), {
  special_number: null,
  super_prize: null,
  guess_big_small: "-",
  guess_odd_even: "-"
})
</script>

<template>
  <div class="rounded-lg overflow-hidden shadow-lg" style="background-color: #f1e5ff; border-radius: 5px">
    <!-- Logo -->
    <div class="flex justify-center pt-4 pb-2">
      <img src="/images/logos/bingobingo.png" alt="BingoBingo" class="h-[120px] object-contain" />
    </div>

    <!-- Draw info bar -->
    <DrawInfoBar
      :drawDate="draw_date"
      :drawTime="draw_time"
      :drawTerm="draw_term"
      :nextDraw="`${next_draw_date}(${next_draw_time})`"
    />

    <!-- Ball grid (5 per row) -->
    <div class="grid grid-cols-5 gap-x-4 gap-y-3 px-6 pb-4">
      <div v-for="(num, i) in numbers" :key="i" class="flex flex-col items-center">
        <LotteryBall :number="num" type="normal" size="md" />
      </div>
      <!-- Special number with label -->
      <div class="flex flex-col items-center">
        <LotteryBall :number="special_number" type="special" size="md" />
        <span class="text-xs text-red-500 font-bold mt-0.5">特別號</span>
      </div>
    </div>

    <!-- Bottom: 超級獎號 / 猜大小 / 猜單雙 -->
    <div class="flex items-center gap-4 px-6 pb-4 text-sm text-gray-700">
      <span class="font-medium">超級獎號</span>
      <LotteryBall :number="super_prize" type="special" size="sm" />

      <span class="font-medium">猜大小</span>
      <div
        class="w-7 h-7 rounded-full flex items-center justify-center text-xs font-bold text-gray-700 shrink-0"
        style="background-color: #f9d71c"
      >
        {{ guess_big_small }}
      </div>

      <span class="font-medium">猜單雙</span>
      <div
        class="w-7 h-7 rounded-full flex items-center justify-center text-xs font-bold text-white shrink-0"
        style="background-color: #26a69a"
      >
        {{ guess_odd_even }}
      </div>
    </div>
  </div>
</template>
