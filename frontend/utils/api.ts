import type { ApiResponseData, BingoApiResponse, DrawsResponse } from "~/types/index"

export const useLotteryApi = () => {
  const getLatest = () => $fetch<ApiResponseData[]>("/api/lottery/latest")
  const getBingoLatest = () => $fetch<BingoApiResponse>("/api/lottery/bingo_latest")
  const getDraws = (slug: string, limit: number) =>
    $fetch<DrawsResponse>(`/api/lottery/draws/${slug}`, { query: { limit } })
  return { getLatest, getBingoLatest, getDraws }
}
