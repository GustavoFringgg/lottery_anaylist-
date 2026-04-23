export interface ApiResponseData {
  game_code: number
  term: string
  draw_date: string
  numbers: number[]
  next_draw_date: string | null
}

export interface CardData {
  name: string
  game_code: number
  nameColor: string
  draw_term: string
  draw_date: string
  draw_time: string
  next_draw: string
  numbers: number[]
  special_number: number | null
  bgColor: string
  logo: string
  draw_days: number[]
  showSortButtons?: boolean
}
