<template>
  <ins
    class="adsbygoogle w-full"
    style="display: block"
    :data-ad-client="adClient"
    :data-ad-slot="adSlot"
    data-ad-format="auto"
    data-full-width-responsive="true"
  />
</template>

<script setup lang="ts">
const props = defineProps<{
  adSlot: string
}>()

const adClient = "ca-pub-3532772519046674"

onMounted(() => {
  setTimeout(() => {
    // @ts-ignore
    ;(window.adsbygoogle = window.adsbygoogle || []).push({})
  }, 500)
})
</script>
