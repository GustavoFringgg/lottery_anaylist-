<script setup lang="ts">
const sortMode = defineModel<'size' | 'draw'>({ default: 'draw' })
</script>

<template>
  <div class="flex border-t border-gray-100">
    <button
      class="btn-sort"
      :class="{ active: sortMode === 'size' }"
      @click="sortMode = 'size'"
    >
      大小順序
    </button>
    <div class="w-px bg-white/40" />
    <button
      class="btn-sort"
      :class="{ active: sortMode === 'draw' }"
      @click="sortMode = 'draw'"
    >
      開出順序
    </button>
  </div>
</template>
