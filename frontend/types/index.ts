export interface ApiResponseData {
  game_code: number
  term: string
  draw_date: string
  numbers: number[]
  special: number | null
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

export interface DrawItem {
  game_code: number
  term: string
  draw_date: string
  numbers: number[]
  special: number | null
}

export interface DrawsResponse {
  slug: string
  name: string
  draw_list: DrawItem[]
}

export interface BingoApiResponse {
  game_code: number
  term: string
  draw_date: string
  numbers: number[]
  special: number | null
  lot_big_small: string
  lot_odd_even: string
  next_draw_date: string | null
}
