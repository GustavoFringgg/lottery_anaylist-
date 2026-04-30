<template>
  <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-4">
    <h1 class="sr-only">{{ gameName }}</h1>
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
</template>

<script setup lang="ts">
interface Feature {
  label: string
  value: string
}

const props = defineProps<{
  logoSrc: string
  gameName: string
  features: Feature[]
}>()

const activeFeature = defineModel<string>("activeFeature", { required: true })

const featureOpen = ref(false)

const activeLabel = computed(() => props.features.find((f) => f.value === activeFeature.value)?.label)

function selectFeature(value: string) {
  activeFeature.value = value
  featureOpen.value = false
}
</script>
