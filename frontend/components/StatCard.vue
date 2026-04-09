<script setup lang="ts">
interface Props {
  title: string
  value: string | number
  subtitle?: string
  trend?: 'up' | 'down' | 'neutral'
}

defineProps<Props>()
</script>

<template>
  <div class="glass-card p-4">
    <p class="text-xs text-gray-500 uppercase tracking-wider">{{ title }}</p>
    <p class="mt-1 text-2xl font-bold text-white">{{ value }}</p>
    <p v-if="subtitle" class="mt-0.5 text-xs text-gray-500">{{ subtitle }}</p>
  </div>
</template>
