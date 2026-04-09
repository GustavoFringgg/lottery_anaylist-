<script setup lang="ts">
interface DrawResult {
  draw_term: string
  draw_date: string
  numbers: number[]
  special_number: number | null
  is_live: boolean
  source?: string
}

interface HotNumber {
  number: number
  count: number
  percentage: number
}

interface DrawRecord {
  draw_term: string
  draw_date: string
  numbers: number[]
  special_number: number | null
}

// --- Mock Data ---
const latestDraw: DrawResult = {
  draw_term: '114000030',
  draw_date: '2026-04-08',
  numbers: [3, 12, 19, 27, 33, 38],
  special_number: 7,
  is_live: false,
  source: '台彩官網',
}

const historyRecords: DrawRecord[] = [
  { draw_term: '114000030', draw_date: '2026-04-08', numbers: [3, 12, 19, 27, 33, 38], special_number: 7 },
  { draw_term: '114000029', draw_date: '2026-04-05', numbers: [5, 11, 22, 24, 36, 41], special_number: 15 },
  { draw_term: '114000028', draw_date: '2026-04-03', numbers: [1, 9, 18, 26, 31, 45], special_number: 23 },
  { draw_term: '114000027', draw_date: '2026-04-01', numbers: [7, 13, 20, 28, 34, 42], special_number: 4 },
  { draw_term: '114000026', draw_date: '2026-03-29', numbers: [2, 16, 21, 30, 37, 44], special_number: 10 },
  { draw_term: '114000025', draw_date: '2026-03-27', numbers: [6, 14, 23, 29, 35, 43], special_number: 18 },
  { draw_term: '114000024', draw_date: '2026-03-25', numbers: [4, 10, 17, 25, 32, 40], special_number: 8 },
  { draw_term: '114000023', draw_date: '2026-03-22', numbers: [8, 15, 24, 31, 39, 46], special_number: 12 },
  { draw_term: '114000022', draw_date: '2026-03-20', numbers: [2, 11, 19, 28, 36, 43], special_number: 5 },
  { draw_term: '114000021', draw_date: '2026-03-18', numbers: [9, 13, 22, 27, 34, 41], special_number: 20 },
]

const hotNumbers: HotNumber[] = [
  { number: 12, count: 8, percentage: 100 },
  { number: 27, count: 7, percentage: 87.5 },
  { number: 19, count: 6, percentage: 75 },
  { number: 33, count: 6, percentage: 75 },
  { number: 5,  count: 5, percentage: 62.5 },
  { number: 38, count: 5, percentage: 62.5 },
  { number: 22, count: 4, percentage: 50 },
  { number: 41, count: 4, percentage: 50 },
]

const stats = [
  { title: '本期獎號', value: latestDraw.draw_term, subtitle: '期別' },
  { title: '開獎日期', value: latestDraw.draw_date, subtitle: '最新一期' },
  { title: '數據來源', value: latestDraw.source ?? '--', subtitle: '更新來源' },
]

useHead({
  title: '台彩分析 - 即時大樂透開獎資訊',
})
</script>

<template>
  <div class="space-y-6">
    <!-- Page header -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-bold text-white">大樂透</h1>
        <p class="mt-1 text-sm text-gray-500">即時開獎 · 歷史查詢 · 號碼統計</p>
      </div>
      <span class="text-xs text-gray-600">資料每 30 秒自動更新</span>
    </div>

    <!-- Stats row -->
    <div class="grid grid-cols-3 gap-4">
      <StatCard
        v-for="stat in stats"
        :key="stat.title"
        :title="stat.title"
        :value="stat.value"
        :subtitle="stat.subtitle"
      />
    </div>

    <!-- Two-column main layout -->
    <div class="grid grid-cols-1 gap-6 lg:grid-cols-3">
      <!-- Left: Live draw + recent history (2/3 width) -->
      <div class="space-y-6 lg:col-span-2">
        <LiveDrawCard :result="latestDraw" game-name="大樂透" />
        <RecentDrawsTable :records="historyRecords" />
      </div>

      <!-- Right: Hot numbers sidebar (1/3 width) -->
      <div class="space-y-6">
        <HotNumbersChart :numbers="hotNumbers" />
        <div class="glass-card p-6">
          <h3 class="section-title">遺漏號碼</h3>
          <p class="text-xs text-gray-600">功能即將上線，敬請期待</p>
        </div>
      </div>
    </div>
  </div>
</template>
