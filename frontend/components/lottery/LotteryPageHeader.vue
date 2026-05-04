<template>
  <div>
    <!-- Logo + 功能下拉：卡片外層，無背景 -->
    <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-4">
      <h1 class="sr-only">{{ gameName }}</h1>
      <img :src="logoSrc" :alt="gameName" class="h-[61px] sm:h-[80px] w-auto object-contain" />

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
            v-for="f in features"
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

    <!-- Title + 期號範圍：#59adbc 卡片 -->
    <div class="rounded-[20px] px-6 py-4 mb-4" style="background-color: #59adbc">
      <h2 class="text-center font-bold text-[#ffe868] sm:text-[30px] text-[20px] mb-3">{{ title }}</h2>
      <hr class="border-[#007979] mb-[24px] mt-[15px]" />
      <div class="flex items-center gap-3">
        <span class="font-bold text-[#ffe868] sm:text-[20px] text-[16px] shrink-0">期號範圍</span>
        <div class="relative flex-1">
          <select
            :value="limit"
            @change="limit = Number(($event.target as HTMLSelectElement).value)"
            class="appearance-none w-full px-4 pr-10 rounded-[5px] font-bold text-[#333] bg-white cursor-pointer sm:text-[20px] text-[16px] sm:h-[54px] h-[33px]"
          >
            <option v-for="opt in options" :key="opt" :value="opt">前{{ opt }}期</option>
          </select>
          <span class="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-[#333] text-xs">▼</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const SUB_FEATURES = [
  { label: "歷年開獎號碼", value: "history" },
  { label: "分布走勢圖", value: "trend" },
  { label: "各期統計分析", value: "stats" },
  { label: "三分區分佈圖", value: "zone" },
  { label: "單雙比分析圖", value: "odd-even" },
  { label: "首數分析圖", value: "first-digit" },
  { label: "尾數分析圖", value: "last-digit" },
]

const GAMES_WITH_SPECIAL = ['big-lotto', 'power-lotto', 'bingo']

const options = [10, 20, 30]

const props = defineProps<{
  logoSrc: string
  gameName: string
  title: string
}>()

const limit = defineModel<number>({ required: true })

const router = useRouter()
const route = useRoute()

const features = computed(() => {
  const slug = route.params.slug as string
  const extra = GAMES_WITH_SPECIAL.includes(slug)
    ? [{ label: "特別號分析", value: "special" }]
    : []
  return [...SUB_FEATURES, ...extra]
})

const activeFeature = computed(() => route.path.split("/").pop() ?? "")

const activeLabel = computed(() => features.value.find((f) => f.value === activeFeature.value)?.label)

const featureOpen = ref(false)

function selectFeature(value: string) {
  featureOpen.value = false
  const slug = route.params.slug as string
  router.push(`/lotto/${slug}/${value}`)
}
</script>
