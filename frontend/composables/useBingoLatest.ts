import { formatDate } from "~/utils/formatDate"

export const useBingoLatest = () => {
  const { getBingoLatest } = useLotteryApi()

  const { data, error, refresh } = useAsyncData("bingo-latest", () => getBingoLatest())

  let intervalTimer: ReturnType<typeof setInterval> | null = null
  let initialTimer: ReturnType<typeof setTimeout> | null = null

  onMounted(() => {
    const INTERVAL = 5 * 60 * 1000
    const OFFSET = (2 * 60 + 20) * 1000 // 基準分鐘2/7/12...後20秒才打
    const now = new Date()
    const msUntilNextMark = INTERVAL - ((now.getTime() - OFFSET) % INTERVAL)

    initialTimer = setTimeout(() => {
      console.log("[Bingo] 整點5分自動更新", new Date().toLocaleTimeString())
      refresh()
      intervalTimer = setInterval(() => {
        console.log("[Bingo] 整點5分自動更新", new Date().toLocaleTimeString())
        refresh()
      }, INTERVAL)
    }, msUntilNextMark)
  })

  onUnmounted(() => {
    if (initialTimer) clearTimeout(initialTimer)
    if (intervalTimer) clearInterval(intervalTimer)
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
