<script setup lang="ts">
interface HotNumber {
  number: number
  count: number
  percentage: number
}

interface Props {
  numbers: HotNumber[]
  loading?: boolean
}

withDefaults(defineProps<Props>(), {
  loading: false,
})
</script>

<template>
  <div class="glass-card p-6">
    <h3 class="section-title">熱門號碼 (近 30 期)</h3>

    <div v-if="loading" class="space-y-3">
      <div v-for="i in 6" :key="i" class="h-8 rounded-lg bg-gray-800 animate-pulse" />
    </div>

    <div v-else class="space-y-3">
      <div
        v-for="item in numbers.slice(0, 8)"
        :key="item.number"
        class="flex items-center gap-3"
      >
        <LotteryBall :number="item.number" type="normal" size="sm" />
        <div class="flex-1">
          <div class="relative h-2 rounded-full bg-gray-800 overflow-hidden">
            <div
              class="absolute inset-y-0 left-0 rounded-full bg-gradient-to-r from-brand-500 to-brand-600 transition-all duration-700"
              :style="{ width: `${item.percentage}%` }"
            />
          </div>
        </div>
        <span class="w-8 text-right text-xs text-gray-500">{{ item.count }}次</span>
      </div>
    </div>
  </div>
</template>
