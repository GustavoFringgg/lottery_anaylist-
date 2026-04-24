import type { ApiResponseData, BingoApiResponse } from "~/types/index"

export const useLotteryApi = () => {
  const getLatest = () => $fetch<ApiResponseData[]>("/api/lottery/latest")
  const getBingoLatest = () => $fetch<BingoApiResponse>("/api/lottery/bingo_latest")
  return { getLatest, getBingoLatest }
}
