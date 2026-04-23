import type { DrawItem, GameData } from "~/types/index"

const GAME_META: Record<
  number,
  Omit<
    GameData,
    | "game_code"
    | "draw_term"
    | "draw_date"
    | "draw_time"
    | "next_draw"
    | "numbers"
    | "special_number"
    | "special_number"
  >
> = {
  5120: {
    name: "今彩539",
    nameColor: "#e53935",
    logo: "/images/logos/539lotto.png",
    bgColor: "#E0E9AA",
    draw_days: [1, 2, 3, 4, 5]
  },
  5118: {
    name: "大樂透",
    nameColor: "#e65100",
    logo: "/images/logos/lotto.png",
    bgColor: "#FFDFAA",
    draw_days: [2, 5]
  },
  5134: {
    name: "威力彩",
    nameColor: "#7b1fa2",
    logo: "/images/logos/power-lotto.png",
    bgColor: "#B6D7FF",
    draw_days: [1, 4]
  },
  1197: {
    name: "39樂合彩",
    nameColor: "#f57c00",
    logo: "/images/logos/39lotto.png",
    bgColor: "#D8D8D8",
    draw_days: [1, 2, 3, 4, 5]
  },
  1121: {
    name: "49樂合彩",
    nameColor: "#e65100",
    logo: "/images/logos/49lotto.png",
    bgColor: "#FFB59E",
    draw_days: [2, 5]
  },
  2108: {
    name: "3星彩",
    nameColor: "#c8a000",
    logo: "/images/logos/3starts.png",
    bgColor: "#FFD269",
    draw_days: [1, 2, 3, 4, 5]
  },
  2109: {
    name: "4星彩",
    nameColor: "#e65100",
    logo: "/images/logos/4starts.png",
    bgColor: "#FFD269",
    draw_days: [1, 2, 3, 4, 5]
  }
}

const formatDate = (iso: string) => {
  const d = new Date(iso)
  const roc = d.getFullYear() - 1911
  const mm = String(d.getMonth() + 1).padStart(2, "0")
  const dd = String(d.getDate()).padStart(2, "0")
  const hh = String(d.getHours()).padStart(2, "0")
  const min = String(d.getMinutes()).padStart(2, "0")
  return {
    date: `${roc}/${mm}/${dd}`,
    time: `${hh}:${min}`
  }
}

const FEATURED_CODES = [5120, 5118, 5134]

export const useLotteryLatest = () => {
  const config = useRuntimeConfig()

  const { data, error } = useAsyncData("lottery-latest", () =>
    $fetch<{ draws: DrawItem[] }>(`${config.public.apiBase}/api/lottery/latest`, {
      headers: { "X-API-Key": config.public.apiKey }
    })
  )

  const games = computed<GameData[]>(() => {
    if (!data.value) return []
    return data.value.draws.map((item) => {
      const meta = GAME_META[item.game_code]
      const { date, time } = formatDate(item.draw_date)
      const nextDraw = item.next_draw_date ? formatDate(item.next_draw_date).date : "-"
      return {
        ...meta,
        game_code: item.game_code,
        draw_term: item.term,
        draw_date: date,
        draw_time: time,
        next_draw: nextDraw,
        numbers: item.numbers,
        special_number: null
      }
    })
  })

  const featured = computed(() => games.value.filter((g) => FEATURED_CODES.includes(g.game_code)))
  const grid = computed(() => games.value.filter((g) => !FEATURED_CODES.includes(g.game_code)))

  return { featured, grid, error }
}
