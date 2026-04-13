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

const gridStyle = computed(() => {
  const cols = props.game.numbers.length <= 5 ? props.game.numbers.length : 4
  return { gridTemplateColumns: `repeat(${cols}, 55px)` }
})
</script>

<template>
  <div
    class="game-card flex flex-col w-full max-w-[595px] mx-auto"
    :style="{ backgroundColor: game.bgColor ?? '#ffffff', borderRadius: '5px' }"
  >
    <div class="flex justify-center pt-4 pb-2">
      <img v-if="game.logo" :src="game.logo" :alt="game.name" class="w-[200px] h-[80px] object-contain" />
    </div>
    <!-- Draw info bar -->
    <DrawInfoBar
      :drawDate="game.draw_date"
      :drawTime="game.draw_time"
      :drawTerm="game.draw_term"
      :nextDraw="game.next_draw"
      nextDrawLabel="下期開獎："
      class="sm:max-w-[507px] sm:ms-[46px]"
    />

    <!-- Balls -->
    <div class="grid justify-center gap-x-[15px] sm:gap-x-[59px] gap-y-[15px] sm:gap-y-[51px] px-4 sm:px-6 py-4" :style="gridStyle">
      <div v-for="(num, i) in displayNumbers" :key="i" class="flex flex-col items-center">
        <LotteryBall :number="num" type="normal" size="md" />
      </div>
      <div v-if="game.special_number !== null" class="flex flex-col items-center w-[60px]">
        <LotteryBall :number="game.special_number" type="special" size="md" />
        <span class="text-[12px] sm:text-[20px] text-red-500 font-bold mt-0.5">特別號</span>
      </div>
    </div>

    <SortButtons v-if="game.showSortButtons !== false" v-model="sortMode" class="mt-auto" />
  </div>
</template>
