<script setup lang="ts">
import { formatDate } from "~/utils/formatDate"

const props = defineProps<{
  slug: string
  logoSrc: string
}>()

const SUB_FEATURES = [
  { label: "歷年開獎號碼", value: "history" },
  { label: "分布走勢圖", value: "trend" },
  { label: "各期統計分析", value: "stats" },
  { label: "三分區分佈圖", value: "zone" },
  { label: "單雙比分析圖", value: "odd-even" },
  { label: "首數分析圖", value: "first-digit" },
  { label: "尾數分析圖", value: "last-digit" }
]

const LIMIT_OPTIONS = [10, 20, 30]
const PAGE_SIZE = 8

const { getDraws } = useLotteryApi()

const limit = ref(10)
const activeFeature = ref("history")
const featureOpen = ref(false)
const currentPage = ref(1)

const { data } = await useAsyncData(`lottery-history-${props.slug}`, () => getDraws(props.slug, limit.value), {
  watch: [limit]
})

const gameName = computed(() => data.value?.name ?? "")

const rows = computed(() =>
  (data.value?.draw_list ?? []).map((item) => ({
    term: item.term,
    date: formatDate(item.draw_date).date,
    numbers: item.numbers,
    special: item.special ?? null
  }))
)

const totalPages = computed(() => Math.ceil(rows.value.length / PAGE_SIZE))

const pagedRows = computed(() => {
  const start = (currentPage.value - 1) * PAGE_SIZE
  return rows.value.slice(start, start + PAGE_SIZE)
})

const activeLabel = computed(() => SUB_FEATURES.find((f) => f.value === activeFeature.value)?.label)

function selectFeature(value: string) {
  activeFeature.value = value
  featureOpen.value = false
}

const hasSpecial = computed(() => rows.value.some((row) => row.special !== null))
</script>

<template>
  <div class="bg-[#f0ede6] min-h-screen">
    <div class="max-w-[1200px] mx-auto px-2 sm:px-0 py-0">
      <!-- 頁面標題列 -->
      <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-4">
        <h1 class="sr-only">{{ gameName }} 歷史開獎號碼查詢</h1>
        <img :src="logoSrc" :alt="gameName" class="h-[61px] sm:h-[80px] w-auto object-contain" />

        <!-- 功能下拉（右側） -->
        <div class="relative w-full sm:w-auto">
          <button
            class="flex items-center gap-2 bg-white border border-[#007979] rounded-[5px] px-4 py-2 font-bold text-[#545454] w-full sm:min-w-[200px] justify-between"
            @click="featureOpen = !featureOpen"
          >
            {{ activeLabel }}
            <span class="text-xs">▼</span>
          </button>
          <div
            v-if="featureOpen"
            class="absolute right-0 top-full mt-1 bg-white border border-[#007979] rounded z-20 min-w-[200px] shadow"
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

      <!-- 查詢控制列 -->
      <div class="rounded-[20px] px-6 py-4 mb-4" style="background-color: #59adbc">
        <h2 class="text-center font-bold text-[#ffe868] sm:text-[30px] text-[20px] mb-3">歷年開獎號碼查詢</h2>
        <hr class="border-[#007979] mb-[24px] mt-[15px]" />
        <div class="flex items-center gap-3">
          <span class="font-bold text-[#ffe868] sm:text-[20px] text-[16px] shrink-0">期號範圍</span>
          <div class="relative flex-1">
            <select
              v-model="limit"
              class="appearance-none w-full px-4 pr-10 rounded-[5px] font-bold text-[#333] bg-white cursor-pointer sm:text-[20px] text-[16px] sm:h-[54px] h-[33px]"
            >
              <option v-for="opt in LIMIT_OPTIONS" :key="opt" :value="opt">前{{ opt }}期</option>
            </select>
            <span class="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-[#333] text-xs">▼</span>
          </div>
        </div>
      </div>

      <!-- 桌面版表格 -->
      <div class="hidden sm:block border border-[#007979] rounded overflow-hidden">
        <table class="w-full border-collapse">
          <thead>
            <tr class="font-bold text-white text-center text-[24px]">
              <th class="py-6 w-[16.6%] border border-[#007979]" style="background: #ff4100">開獎期數</th>
              <th class="py-6 w-[16.6%] border border-[#007979]" style="background: #ff4100">開獎日期</th>
              <th class="py-6 border border-[#007979]" style="background: #2db38d">
                {{ hasSpecial ? "開獎號碼 + 特別號" : "開獎號碼 (5個)" }}
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(row, i) in pagedRows"
              :key="row.term"
              class="text-center text-[24px] border-t border-[#007979]"
              :style="i % 2 === 0 ? 'background:#fff' : 'background:#a9d9ce'"
            >
              <td class="h-[92px] font-medium text-[#2b2b2b] border border-[#007979]">{{ row.term }}</td>
              <td class="h-[92px] font-medium text-[#2b2b2b] border border-[#007979]">{{ row.date }}</td>
              <td class="h-[92px] border border-[#007979]">
                <div class="flex items-center justify-center gap-[21px]">
                  <span
                    v-for="n in row.numbers"
                    :key="n"
                    class="rounded-full inline-flex items-center justify-center font-bold border-2 border-gray-300 bg-white text-black w-[57px] h-[57px] text-[26px] shrink-0"
                  >
                    {{ String(n).padStart(2, "0") }}
                  </span>
                  <span
                    v-if="row.special !== null"
                    class="rounded-full inline-flex items-center justify-center font-bold bg-[#ff4100] text-white w-[57px] h-[57px] text-[26px] shrink-0"
                  >
                    {{ String(row.special).padStart(2, "0") }}
                  </span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- 手機版卡片列表 -->
      <div class="sm:hidden space-y-2">
        <div
          v-for="(row, i) in pagedRows"
          :key="row.term"
          class="border border-[#007979] rounded overflow-hidden"
          :style="i % 2 === 0 ? 'background:#fff' : 'background:#a9d9ce'"
        >
          <div class="grid grid-cols-2 border-b border-[#007979]" style="background: #2db38d">
            <div class="py-2 text-white font-bold text-[16px] text-center border-r border-[#007979]">開獎期數</div>
            <div class="py-2 text-white font-bold text-[16px] text-center">開獎日期</div>
          </div>
          <div class="grid grid-cols-2 border-b border-[#007979]">
            <div class="py-3 text-[#2b2b2b] font-medium text-[16px] text-center border-r border-[#007979]">
              {{ row.term }}
            </div>
            <div class="py-3 text-[#2b2b2b] font-medium text-[16px] text-center">{{ row.date }}</div>
          </div>
          <div
            class="py-2 text-white font-bold text-[16px] text-center border-b border-[#007979]"
            style="background: #2db38d"
          >
            開獎號碼
          </div>
          <div class="py-3 flex items-center justify-center gap-2">
            <span
              v-for="n in row.numbers"
              :key="n"
              class="rounded-full inline-flex items-center justify-center font-bold border-2 border-gray-300 bg-white text-black w-[33px] h-[33px] text-[15px] shrink-0"
            >
              {{ String(n).padStart(2, "0") }}
            </span>
            <span
              v-if="row.special !== null"
              class="rounded-full inline-flex items-center justify-center font-bold bg-[#ff4100] text-white w-[33px] h-[33px] text-[15px] shrink-0"
            >
              {{ String(row.special).padStart(2, "0") }}
            </span>
          </div>
        </div>
      </div>

      <Pagination v-if="totalPages > 1" v-model:currentPage="currentPage" :totalPages="totalPages" />
    </div>
  </div>
</template>
