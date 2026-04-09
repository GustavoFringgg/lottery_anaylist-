<script setup lang="ts">
type BallType = 'normal' | 'special' | 'bonus' | 'placeholder'

interface Props {
  number: number | null
  type?: BallType
  size?: 'sm' | 'md' | 'lg'
  animate?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  type: 'normal',
  size: 'md',
  animate: false,
})

const sizeClasses = {
  sm: 'w-8 h-8 text-sm font-semibold',
  md: 'w-11 h-11 text-base font-bold',
  lg: 'w-14 h-14 text-lg font-bold',
}

const colorClasses: Record<BallType, string> = {
  normal:
    'bg-gradient-to-br from-blue-500 to-blue-700 shadow-lg shadow-blue-500/30 text-white',
  special:
    'bg-gradient-to-br from-red-500 to-rose-700 shadow-lg shadow-red-500/30 text-white',
  bonus:
    'bg-gradient-to-br from-amber-400 to-orange-500 shadow-lg shadow-amber-400/30 text-gray-900',
  placeholder:
    'bg-gray-800 border border-dashed border-gray-700 text-gray-600',
}
</script>

<template>
  <div
    class="relative inline-flex items-center justify-center rounded-full select-none"
    :class="[
      sizeClasses[size],
      colorClasses[type],
      animate && number !== null ? 'animate-ball-pop' : '',
    ]"
  >
    <span v-if="number !== null" :class="animate ? 'animate-number-flip' : ''">
      {{ String(number).padStart(2, '0') }}
    </span>
    <span v-else class="text-gray-600">--</span>

    <!-- Shine overlay -->
    <div
      v-if="type !== 'placeholder'"
      class="absolute inset-0 rounded-full bg-gradient-to-b from-white/20 to-transparent pointer-events-none"
    />
  </div>
</template>
