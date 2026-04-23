import type { ApiResponseData } from "~/types/index"

export const useLotteryApi = () => {
  const config = useRuntimeConfig()

  const headers = {
    "X-API-Key": config.public.apiKey as string
  }

  const baseUrl = config.public.apiBase

  const getLatest = () => $fetch<{ draws: ApiResponseData[] }>(`${baseUrl}/api/lottery/latest`, { headers })

  const getBingoLatest = () => $fetch(`${baseUrl}/api/lottery/bingo/latest`, { headers })

  return { getLatest, getBingoLatest }
}
