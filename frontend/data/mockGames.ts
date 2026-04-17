// Mock 資料，模擬後端 GET /api/games 回傳格式
// 後端實際回傳結構：{ every5min, featured, grid }

export interface GameData {
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
  draw_days?: number[] // 0=日, 1=一 ... 6=六
}

export interface GamesResponse {
  every5min: GameData[]
  featured: GameData[] // 熱門遊戲，全寬顯示
  grid: GameData[] // 其餘遊戲，兩欄 grid 顯示
}

export const mockGames: GamesResponse = {
  every5min: [
    // BingoBingo 由獨立元件處理，此區塊保留給未來其他5分鐘遊戲
  ],
  //  熱門／全寬顯示
  featured: [
    {
      name: "今彩539",
      nameColor: "#e53935",
      draw_term: "115000079",
      draw_date: "115/03/30",
      draw_time: "15:00",
      next_draw: "115/04/01",
      numbers: [3, 29, 33, 27, 30],
      special_number: null,
      bgColor: "#E0E9AA",
      logo: "/images/logos/539lotto.png",
      draw_days: [1, 2, 3, 4, 5]
    },
    {
      name: "大樂透",
      nameColor: "#e65100",
      draw_term: "115000030",
      draw_date: "115/03/27",
      draw_time: "21:30",
      next_draw: "115/03/31",
      numbers: [3, 29, 33, 27, 30, 17],
      special_number: 9,
      bgColor: "#FFDFAA",
      logo: "/images/logos/lotto.png",
      draw_days: [2, 5]
    },
    {
      name: "威力彩",
      nameColor: "#7b1fa2",
      draw_term: "115000026",
      draw_date: "115/03/27",
      draw_time: "21:30",
      next_draw: "115/03/31",
      numbers: [3, 29, 33, 27, 30, 17],
      special_number: 9,
      bgColor: "#B6D7FF",
      logo: "/images/logos/power-lotto.png",
      draw_days: [1, 4]
    }
  ],

  // 下方兩欄 grid 顯示
  grid: [
    {
      name: "39樂合彩",
      nameColor: "#f57c00",
      draw_term: "115000079",
      draw_date: "115/03/30",
      draw_time: "15:00",
      next_draw: "115/04/01",
      numbers: [29, 27, 3, 33, 22],
      special_number: null,
      bgColor: "#D8D8D8",
      logo: "/images/logos/39lotto.png",
      draw_days: [1, 2, 3, 4, 5]
    },
    {
      name: "49樂合彩",
      nameColor: "#e65100",
      draw_term: "115000030",
      draw_date: "115/03/27",
      draw_time: "21:30",
      next_draw: "115/03/31",
      numbers: [3, 29, 33, 27, 2, 9],
      special_number: null,
      bgColor: "#FFB59E",
      logo: "/images/logos/49lotto.png",
      draw_days: [2, 5]
    },
    {
      name: "3星彩",
      nameColor: "#c8a000",
      draw_term: "115000079",
      draw_date: "115/03/30",
      draw_time: "13:30",
      next_draw: "115/04/01",
      numbers: [3, 2, 9],
      special_number: null,
      showSortButtons: false,
      bgColor: "#FFD269",
      logo: "/images/logos/3starts.png",
      draw_days: [1, 2, 3, 4, 5]
    },
    {
      name: "4星彩",
      nameColor: "#e65100",
      draw_term: "115000079",
      draw_date: "115/03/30",
      draw_time: "13:30",
      next_draw: "115/04/01",
      numbers: [3, 2, 9, 7],
      special_number: null,
      showSortButtons: false,
      bgColor: "#FFD269",
      logo: "/images/logos/4starts.png",
      draw_days: [1, 2, 3, 4, 5]
    }
  ]
}
