import type { ApiResponseData } from "~/types/index"

export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig(event)
  return $fetch<ApiResponseData[]>(`${config.public.apiBase}/api/lottery/latest`, {
    headers: { "X-API-Key": config.apiKey }
  })
})
