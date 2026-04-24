import type { BingoApiResponse } from "~/types/index"

export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig(event)
  return $fetch<BingoApiResponse>(`${config.public.apiBase}/api/lottery/bingo/latest`, {
    headers: { "X-API-Key": config.apiKey }
  })
})
