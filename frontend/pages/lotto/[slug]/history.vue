<script setup lang="ts">
const route = useRoute()
const slug = route.params.slug as string

const LOGO_MAP: Record<string, string> = {
  "539": "/images/logos/539lotto.png",
  "big-lotto": "/images/logos/lotto.png"
}

const logoSrc = LOGO_MAP[slug] ?? "/images/logos/favicon.png"
</script>

<template>
  <LotteryHistory :slug="slug" :logoSrc="logoSrc" />
</template>
