import type { ApiResponseData, BingoApiResponse } from "~/types/index"

export const useLotteryApi = () => {
  const config = useRuntimeConfig()

  const headers = {
    "X-API-Key": config.apiKey as string
  }

  const baseUrl = config.public.apiBase

  const getLatest = () => $fetch<{ draws: ApiResponseData[] }>(`${baseUrl}/api/lottery/latest`, { headers })

  const getBingoLatest = () => $fetch<BingoApiResponse>(`${baseUrl}/api/lottery/bingo/latest`, { headers })

  return { getLatest, getBingoLatest }
}
