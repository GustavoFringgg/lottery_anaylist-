<script setup lang="ts">
interface Game {
  name: string
  nameColor: string
  draw_term: string
  draw_date: string
  draw_time: string
  next_draw: string
  numbers: number[]
  special_number: number | null
}

const props = defineProps<{ game: Game }>()

const sortMode = ref<'draw' | 'size'>('draw')

const displayNumbers = computed(() =>
  sortMode.value === 'size'
    ? [...props.game.numbers].sort((a, b) => a - b)
    : props.game.numbers
)
</script>

<template>
  <div class="game-card">
    <!-- Game logo / name -->
    <div class="py-2.5 px-3 text-center border-b border-gray-100 bg-white">
      <span class="text-base font-extrabold tracking-wide" :style="{ color: game.nameColor }">
        {{ game.name }}
      </span>
    </div>

    <!-- Draw info bar -->
    <div class="draw-info-bar">
      <div class="flex justify-between flex-wrap gap-1">
        <span>{{ game.draw_date }} {{ game.draw_time }}　第{{ game.draw_term }}期號碼</span>
        <span>下期開獎：{{ game.next_draw }}</span>
      </div>
    </div>

    <!-- Balls -->
    <div class="flex flex-wrap items-center gap-1.5 px-3 py-3 min-h-[56px]">
      <LotteryBall
        v-for="(num, i) in displayNumbers"
        :key="i"
        :number="num"
        type="normal"
        size="md"
      />
      <template v-if="game.special_number !== null">
        <span class="text-gray-400 font-light text-base">+</span>
        <LotteryBall :number="game.special_number" type="special" size="md" />
      </template>
    </div>

    <!-- Sort buttons -->
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
  </div>
</template>
