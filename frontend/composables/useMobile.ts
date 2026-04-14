import { ref, onMounted, onUnmounted } from "vue"

export function useMobile(width = 440) {
  const isMobile = ref(false)
  const query = `(max-width: ${width}px)`
  const handleChange = (e: MediaQueryListEvent | MediaQueryList) => {
    isMobile.value = e.matches
  }

  onMounted(() => {
    const mq = window.matchMedia(query)
    handleChange(mq)

    mq.addEventListener("change", handleChange)
    onUnmounted(() => {
      mq.removeEventListener("change", handleChange)
    })
  })
  return { isMobile }
}
