<template>
  <div class="rounded-[20px] px-6 py-4 mb-4" style="background-color: #59adbc">
    <h2 class="text-center font-bold text-[#ffe868] sm:text-[30px] text-[20px] mb-3">{{ title }}</h2>
    <hr class="border-[#007979] mb-[24px] mt-[15px]" />
    <div class="flex items-center gap-3">
      <span class="font-bold text-[#ffe868] sm:text-[20px] text-[16px] shrink-0">期號範圍</span>
      <div class="relative flex-1">
        <select
          :value="modelValue"
          @change="$emit('update:modelValue', Number(($event.target as HTMLSelectElement).value))"
          class="appearance-none w-full px-4 pr-10 rounded-[5px] font-bold text-[#333] bg-white cursor-pointer sm:text-[20px] text-[16px] sm:h-[54px] h-[33px]"
        >
          <option v-for="opt in options" :key="opt" :value="opt">前{{ opt }}期</option>
        </select>
        <span class="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-[#333] text-xs">▼</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const options = [10, 20, 30]

defineProps<{
  title: string
  modelValue: number
}>()

defineEmits<{
  'update:modelValue': [value: number]
}>()
</script>
