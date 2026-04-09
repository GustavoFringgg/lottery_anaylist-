<script setup lang="ts">
type BallType = 'normal' | 'special'

interface Props {
  number: number | null
  type?: BallType
  size?: 'sm' | 'md'
}

withDefaults(defineProps<Props>(), {
  type: 'normal',
  size: 'md',
})
</script>

<template>
  <div
    class="rounded-full inline-flex items-center justify-center font-bold select-none shrink-0"
    :class="{
      'w-9 h-9 text-sm': size === 'md',
      'w-7 h-7 text-xs': size === 'sm',
      'bg-white border-2 border-gray-300 text-gray-800 shadow-sm': type === 'normal',
      'bg-red-500 border-2 border-red-600 text-white shadow-sm': type === 'special',
    }"
  >
    <span v-if="number !== null">{{ String(number).padStart(2, '0') }}</span>
    <span v-else class="text-gray-400">--</span>
  </div>
</template>
