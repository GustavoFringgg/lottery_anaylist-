<script setup lang="ts">
const props = defineProps<{
  currentPage: number
  totalPages: number
}>()

const emit = defineEmits<{
  "update:currentPage": [page: number]
}>()

function goTo(page: number) {
  if (page < 1 || page > props.totalPages) return
  emit("update:currentPage", page)
}
</script>

<template>
  <div class="flex items-center justify-center sm:gap-28px gap-[32px] sm:py-2 py-1">
    <button
      class="font-bold text-[#2b2b2b] hover:text-[#007979] disabled:opacity-30 text-4xl"
      :disabled="currentPage === 1"
      @click="goTo(currentPage - 1)"
    >
      ‹
    </button>

    <button
      v-for="page in totalPages"
      :key="page"
      class="font-bold text-[20px] sm:text-[26px] sm:w-[18px] w-[13px] h-[45px] rounded-full transition"
      :class="page === currentPage ? 'text-[#007979]' : 'text-black hover:text-[#007979]'"
      @click="goTo(page)"
    >
      {{ page }}
    </button>

    <button
      class="font-bold text-[#2b2b2b] hover:text-[#007979] disabled:opacity-30 text-4xl"
      :disabled="currentPage === totalPages"
      @click="goTo(currentPage + 1)"
    >
      ›
    </button>
  </div>
</template>
