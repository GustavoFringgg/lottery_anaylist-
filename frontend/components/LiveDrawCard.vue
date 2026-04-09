<script setup lang="ts">
interface DrawResult {
  draw_term: string
  draw_date: string
  numbers: number[]
  special_number: number | null
  is_live: boolean
  source?: string
}

interface Props {
  result: DrawResult | null
  loading?: boolean
  gameName?: string
}

withDefaults(defineProps<Props>(), {
  loading: false,
  gameName: '大樂透',
})
</script>

<template>
  <div class="glass-card p-6">
    <!-- Header -->
    <div class="flex items-center justify-between mb-6">
      <div>
        <h2 class="text-xl font-bold text-white">{{ gameName }}</h2>
        <p class="text-sm text-gray-500 mt-0.5">
          {{ result ? `第 ${result.draw_term} 期` : '載入中...' }}
        </p>
      </div>
      <div
        v-if="result?.is_live"
        class="flex items-center gap-1.5 rounded-full bg-red-500/20 px-3 py-1"
      >
        <span class="h-2 w-2 animate-pulse rounded-full bg-red-500" />
        <span class="text-xs font-medium text-red-400">LIVE</span>
      </div>
    </div>

    <!-- Skeleton -->
    <div v-if="loading" class="flex gap-3 justify-center">
      <div
        v-for="i in 7"
        :key="i"
        class="w-11 h-11 rounded-full bg-gray-800 animate-pulse"
      />
    </div>

    <!-- Balls -->
    <div v-else-if="result" class="flex flex-wrap items-center gap-3 justify-center">
      <TransitionGroup name="ball">
        <LotteryBall
          v-for="(num, idx) in result.numbers"
          :key="`${result.draw_term}-${idx}`"
          :number="num"
          type="normal"
          size="md"
          :animate="result.is_live"
        />
      </TransitionGroup>

      <!-- Separator -->
      <span class="text-gray-600 font-light text-xl mx-1">+</span>

      <!-- Special number -->
      <LotteryBall
        :number="result.special_number"
        type="special"
        size="md"
        :animate="result.is_live"
      />
    </div>

    <!-- Empty state -->
    <div v-else class="text-center py-4 text-gray-600 text-sm">
      尚無開獎資料
    </div>

    <!-- Footer -->
    <div v-if="result" class="mt-4 flex items-center justify-between text-xs text-gray-600">
      <span>{{ result.draw_date }}</span>
      <span v-if="result.source" class="flex items-center gap-1">
        <span class="h-1.5 w-1.5 rounded-full bg-green-500" />
        {{ result.source }}
      </span>
    </div>
  </div>
</template>

<style scoped>
.ball-enter-active {
  animation: ballPop 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.ball-leave-active {
  transition: opacity 0.2s;
}
.ball-leave-to {
  opacity: 0;
}
</style>
