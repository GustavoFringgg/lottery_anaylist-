<template>
  <ins
    class="adsbygoogle"
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
  // @ts-ignore
  ;(window.adsbygoogle = window.adsbygoogle || []).push({})
})
</script>
