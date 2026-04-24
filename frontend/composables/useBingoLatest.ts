import { formatDate } from "~/utils/formatDate"

export const useBingoLatest = () => {
  const { getBingoLatest } = useLotteryApi()

  const { data, error, refresh } = useAsyncData("bingo-latest", () => getBingoLatest())

  let timer: ReturnType<typeof setInterval> | null = null

  onMounted(() => {
    timer = setInterval(
      () => {
        console.log("[Bingo] 5分鐘自動更新", new Date().toLocaleTimeString())
        refresh()
      },
      5 * 60 * 1000
    )
  })

  onUnmounted(() => {
    if (timer) clearInterval(timer)
  })

  const bingoCard = computed(() => {
    if (!data.value) return null
    const d = data.value
    const { date: drawDate, time: drawTime } = formatDate(d.draw_date)
    const nextDraw = d.next_draw_date ? formatDate(d.next_draw_date) : null
    return {
      draw_term: d.term,
      draw_date: drawDate,
      draw_time: drawTime,
      next_draw_date: nextDraw?.date ?? "-",
      next_draw_time: nextDraw?.time ?? "-",
      numbers: d.numbers,
      special_number: d.special,
      guess_big_small: d.lot_big_small ?? "-",
      guess_odd_even: d.lot_odd_even ?? "-"
    }
  })

  return { bingoCard, error, refresh }
}
