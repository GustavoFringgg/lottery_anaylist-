# 前端串接後端 API 說明

後端部署於 Render，本地開發時 base URL 為 `http://localhost:8000`。

---

## Endpoint 一覽

### 1. 取得所有遊戲最新開獎（排除 BingoBingo）

```
GET /api/lottery/latest
```

**Response：**
```json
[
  {
    "game_code": 5118,
    "term": "113000001",
    "draw_date": "2026-04-22T20:32:00",
    "numbers": [1, 5, 12, 23, 39],
    "special": 7,
    "next_draw_date": "2026-04-23T20:32:00"
  }
]
```

- 頁面載入時打一次，不需要輪詢
- 共回傳 7 種遊戲（game_code：1121、1197、2108、2109、5118、5120、5134）
- `special`：有特別號的遊戲（大樂透 5118、威力彩 5134）回數字，其他回 `null`
- `numbers` 不含特別號（特別號已拆出至 `special`）
- `next_draw_date` 可能為 `null`

---

### 2. 取得 BingoBingo 最新開獎

```
GET /api/lottery/bingo/latest
```

**Response：**
```json
{
  "game_code": 1102,
  "term": "113000288",
  "draw_date": "2026-04-22T23:55:00",
  "numbers": [1, 3, 7, 12, 19, 22, 28, 33, 37, 40, 42, 45, 47, 51, 56, 60, 63, 66, 70, 74],
  "next_draw_date": "2026-04-23T00:00:00",
  "special": 49,
  "lot_big_small": "大",
  "lot_odd_even": "單"
}
```

- **每 5 分鐘輪詢一次**（用 `setInterval`）
- `special`：特別號（數字）
- `lot_big_small`：大 / 小
- `lot_odd_even`：單 / 雙

---

### 3. 取得單一遊戲歷史開獎（分析用）

```
GET /api/lottery/draws/{slug}?limit=20
```

**slug 對照表：**

| slug | 遊戲名稱 |
|------|---------|
| `big-lotto` | 大樂透 |
| `power-lotto` | 威力彩 |
| `539` | 今彩539 |
| `bingo` | BingoBingo |
| `39lotto` | 39樂合彩 |
| `49lotto` | 49樂合彩 |
| `3star` | 3星彩 |
| `4star` | 4星彩 |

**參數：**
- `limit`：筆數，預設 20，最大 30（可傳 10 / 20 / 30）

**Response（一般遊戲）：**
```json
{
  "slug": "big-lotto",
  "name": "大樂透",
  "draw_list": [
    {
      "game_code": 5118,
      "term": "113000001",
      "draw_date": "2026-04-22T20:32:00",
      "numbers": [1, 5, 12, 23, 39, 42],
      "special": 7
    }
  ]
}
```

**Response（BingoBingo）：**
```json
{
  "slug": "bingo",
  "name": "BingoBingo",
  "draw_list": [
    {
      "game_code": 1102,
      "term": "113000288",
      "draw_date": "2026-04-22T23:55:00",
      "numbers": [1, 3, 7, 12, 19, 22, 28, 33, 37, 40, 42, 45, 47, 51, 56, 60, 63, 66, 70, 74],
      "special": 49,
      "lot_big_small": "大",
      "lot_odd_even": "單"
    }
  ]
}
```

- bingo 的每筆多帶 `lot_big_small` / `lot_odd_even`，其他遊戲不含這兩個欄位
- `draw_list` 依開獎日期降序排列（最新在前）

---

## game_code 對照表

| game_code | 名稱 | slug | 有特別號 |
|-----------|------|------|---------|
| 1102 | BingoBingo | `bingo` | ✓ |
| 1121 | 49樂合彩 | `49lotto` | ✗ |
| 1197 | 39樂合彩 | `39lotto` | ✗ |
| 2108 | 3星彩 | `3star` | ✗ |
| 2109 | 4星彩 | `4star` | ✗ |
| 5118 | 大樂透 | `big-lotto` | ✓ |
| 5120 | 今彩539 | `539` | ✗ |
| 5134 | 威力彩 | `power-lotto` | ✓ |

---

## API Key 驗證

所有請求必須帶以下 header：

```
X-API-Key: <your-api-key>
```

未帶或錯誤會回傳 `403 Forbidden`。

前端環境變數建議：
```
NUXT_PUBLIC_API_KEY=your-api-key
```

請求範例：
```ts
const { data } = await useFetch('/api/lottery/latest', {
  headers: { 'X-API-Key': useRuntimeConfig().public.apiKey }
})
```

---

## 前端注意事項

- `draw_date` / `next_draw_date` 為 ISO 8601 格式（`datetime`），需自行格式化顯示
- BingoBingo 輪詢建議用 `setInterval(refresh, 5 * 60 * 1000)`，搭配 Nuxt `useAsyncData` 的 `refresh`
- `/latest` 不含 BingoBingo，兩支 API 分開處理
- 後端 CORS 已允許：`http://localhost:3000`、`https://www.539lto.co`、`https://lottery-anaylist.vercel.app`
