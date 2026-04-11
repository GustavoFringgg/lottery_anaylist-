<script setup lang="ts">
interface Props {
  drawDate: string
  drawTime: string
  drawTerm: string
  nextDraw: string
  nextDrawLabel?: string
}

withDefaults(defineProps<Props>(), {
  nextDrawLabel: '下期開獎時間：',
})
</script>

<template>
  <div
    class="px-3 py-2 text-sm text-gray-700"
    style="background: linear-gradient(180deg, #e0f7f4 0%, #c8eef9 100%); border-bottom: 1px solid #a0d8ef;"
  >
    <div class="font-medium">{{ drawDate }} {{ drawTime }}　第{{ drawTerm }}期</div>
    <div class="text-xs text-gray-500 mt-0.5">{{ nextDrawLabel }}{{ nextDraw }}</div>
  </div>
</template>
