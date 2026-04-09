<script setup lang="ts">
interface DrawRecord {
  draw_term: string
  draw_date: string
  numbers: number[]
  special_number: number | null
}

interface Props {
  records: DrawRecord[]
  loading?: boolean
}

withDefaults(defineProps<Props>(), {
  loading: false,
})
</script>

<template>
  <div class="glass-card p-6">
    <h3 class="section-title">近期開獎記錄</h3>

    <div v-if="loading" class="space-y-3">
      <div v-for="i in 5" :key="i" class="h-10 rounded-lg bg-gray-800 animate-pulse" />
    </div>

    <div v-else class="overflow-x-auto">
      <table class="w-full text-sm">
        <thead>
          <tr class="border-b border-white/10 text-left text-xs text-gray-500">
            <th class="pb-3 font-medium">期別</th>
            <th class="pb-3 font-medium">日期</th>
            <th class="pb-3 font-medium">號碼</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-white/5">
          <tr v-for="record in records" :key="record.draw_term" class="py-3">
            <td class="py-3 text-gray-400">{{ record.draw_term }}</td>
            <td class="py-3 text-gray-500 text-xs whitespace-nowrap">{{ record.draw_date }}</td>
            <td class="py-3">
              <div class="flex flex-wrap gap-1.5 items-center">
                <LotteryBall
                  v-for="(num, i) in record.numbers"
                  :key="i"
                  :number="num"
                  type="normal"
                  size="sm"
                />
                <span class="text-gray-700 text-xs">+</span>
                <LotteryBall :number="record.special_number" type="special" size="sm" />
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
