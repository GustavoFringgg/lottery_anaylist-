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
    <DrawInfoBar
      :drawDate="game.draw_date"
      :drawTime="game.draw_time"
      :drawTerm="game.draw_term"
      :nextDraw="game.next_draw"
      nextDrawLabel="下期開獎："
    />

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

    <SortButtons v-model="sortMode" />
  </div>
</template>
