<script setup lang="ts">
import { formatDate } from "~/utils/formatDate"

const props = defineProps<{
  slug: string
  logoSrc: string
}>()

const PAGE_SIZE = 8

const { getDraws } = useLotteryApi()

const limit = ref(10)
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

const hasSpecial = computed(() => rows.value.some((row) => row.special !== null))
</script>

<template>
  <div class="bg-[#f0ede6] min-h-screen">
    <div class="max-w-[1200px] mx-auto px-2 sm:px-0 py-0">
      <LotteryPageHeader :logoSrc="logoSrc" :gameName="gameName" title="分布走勢圖" v-model="limit" />

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
