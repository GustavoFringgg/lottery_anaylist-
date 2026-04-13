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
  <div class="mx-4 my-2.5 rounded px-3 py-2"
    style="background: linear-gradient(to top, #daf6f0, #9ce2f9); border: 3px solid white; border-radius: 3px;"
  >
    <div class="text-xs font-bold text-center" style="color: #626262;">{{ drawDate }} {{ drawTime }}　第{{ drawTerm }}期</div>
    <div class="text-[10px] font-bold text-center mt-0.5" style="color: #626262;">{{ nextDrawLabel }}{{ nextDraw }}</div>
  </div>
</template>
