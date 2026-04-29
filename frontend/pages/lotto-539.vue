<script setup lang="ts">
import { formatDate } from "~/utils/formatDate"

const LIMIT_OPTIONS = [10, 20, 30]
const SUB_FEATURES = [
  { label: "歷年開獎號碼", value: "history" },
  { label: "分布走勢圖", value: "trend" },
  { label: "各期統計分析", value: "stats" },
  { label: "三分區分佈圖", value: "zone" },
  { label: "單雙比分析圖", value: "odd-even" },
  { label: "首數分析圖", value: "first-digit" },
  { label: "尾數分析圖", value: "last-digit" },
]

const { getDraws } = useLotteryApi()

const limit = ref(10)
const activeFeature = ref("history")
const featureOpen = ref(false)

const { data, refresh } = await useAsyncData(
  "lotto-539-draws",
  () => getDraws("539", limit.value),
  { watch: [limit] }
)

const rows = computed(() =>
  (data.value?.draw_list ?? []).map((item) => ({
    term: item.term,
    date: formatDate(item.draw_date).date,
    numbers: item.numbers,
  }))
)

const activeLabel = computed(() => SUB_FEATURES.find((f) => f.value === activeFeature.value)?.label)

function selectFeature(value: string) {
  activeFeature.value = value
  featureOpen.value = false
}
</script>

<template>
  <div class="max-w-[1200px] mx-auto px-2 sm:px-0 py-4">

    <!-- 頁面標題列 -->
    <div class="flex items-center gap-3 mb-4">
      <img src="/images/logos/539lotto.png" alt="今彩539" class="h-[50px] w-auto object-contain" />
    </div>

    <!-- 查詢控制列 -->
    <div class="rounded-[20px] p-4 mb-4 flex flex-wrap items-center gap-3" style="background-color:#59adbc">
      <span class="font-bold text-[#ffe868] text-lg shrink-0">期號範圍</span>

      <!-- 期數選擇 -->
      <select
        v-model="limit"
        class="px-4 py-2 rounded font-bold text-[#333] bg-white cursor-pointer"
      >
        <option v-for="opt in LIMIT_OPTIONS" :key="opt" :value="opt">前{{ opt }}期</option>
      </select>

      <!-- 右側功能下拉 -->
      <div class="relative ml-auto">
        <button
          class="flex items-center gap-2 bg-white rounded px-4 py-2 font-bold text-[#545454] min-w-[160px] justify-between"
          @click="featureOpen = !featureOpen"
        >
          {{ activeLabel }}
          <span class="text-xs">▼</span>
        </button>
        <div
          v-if="featureOpen"
          class="absolute right-0 top-full mt-1 bg-white border border-[#007979] rounded z-20 min-w-[160px] shadow"
        >
          <button
            v-for="f in SUB_FEATURES"
            :key="f.value"
            class="w-full text-left px-4 py-2 text-sm hover:bg-gray-100 transition"
            :style="activeFeature === f.value ? 'color:#2db38d; font-weight:bold' : 'color:#545454'"
            @click="selectFeature(f.value)"
          >
            {{ f.label }}
          </button>
        </div>
      </div>
    </div>

    <!-- 表格 -->
    <div class="border border-[#007979] rounded overflow-hidden">
      <!-- 表頭 -->
      <div class="grid font-bold text-white text-center text-sm sm:text-base" style="grid-template-columns: 1fr 1fr 2fr">
        <div class="py-4" style="background:#ff4100">開獎期數</div>
        <div class="py-4" style="background:#ff4100">開獎日期</div>
        <div class="py-4" style="background:#2db38d">開獎號碼 (5個)</div>
      </div>

      <!-- 資料列 -->
      <div
        v-for="(row, i) in rows"
        :key="row.term"
        class="grid text-center text-sm sm:text-base border-t border-[#007979]"
        style="grid-template-columns: 1fr 1fr 2fr"
        :style="i % 2 === 0 ? 'background:#fff' : 'background:#a9d9ce'"
      >
        <div class="py-4 font-medium text-[#2b2b2b]">{{ row.term }}</div>
        <div class="py-4 font-medium text-[#2b2b2b]">{{ row.date }}</div>
        <div class="py-4 flex items-center justify-center gap-2">
          <div
            v-for="n in row.numbers"
            :key="n"
            class="rounded-full inline-flex items-center justify-center font-bold border-2 border-gray-300 bg-white text-[#2b2b2b] w-[40px] h-[40px] sm:w-[50px] sm:h-[50px] text-sm sm:text-lg shrink-0"
          >
            {{ String(n).padStart(2, "0") }}
          </div>
        </div>
      </div>
    </div>

  </div>
</template>
