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
  showSortButtons?: boolean
  bgColor?: string
  logo?: string
}
const props = defineProps<{ game: Game }>()

const sortMode = ref<"draw" | "size">("draw")

const displayNumbers = computed(() =>
  sortMode.value === "size" ? [...props.game.numbers].sort((a, b) => a - b) : props.game.numbers
)
</script>

<template>
  <div
    class="game-card flex flex-col w-full max-w-[748px] mx-auto"
    :style="{ backgroundColor: game.bgColor ?? '#ffffff', borderRadius: '5px' }"
  >
    <div class="flex justify-center pt-4 pb-2">
      <img v-if="game.logo" :src="game.logo" :alt="game.name" class="h-[120px] w-auto object-contain" />
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
    <div class="flex flex-wrap items-center gap-1.5 px-3 py-3 min-h-[56px] flex-grow">
      <LotteryBall v-for="(num, i) in displayNumbers" :key="i" :number="num" type="normal" size="md" />
      <template v-if="game.special_number !== null">
        <span class="text-gray-400 font-light text-base">+</span>
        <LotteryBall :number="game.special_number" type="special" size="md" />
      </template>
    </div>

    <SortButtons v-if="game.showSortButtons !== false" v-model="sortMode" />
  </div>
</template>
