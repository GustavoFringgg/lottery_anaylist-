# 台彩分析 — 開發規範 & Figma 整合指南

## 1. 競品分析統整 (樂透研究院 pilio.idv.tw)

目前市場排名第一，其技術特點：
- **前端架構**：傳統 ASP + jQuery
- **通訊機制**：Long Polling，透過 articleMedia API 達成不重整更新
- **數據來源**：https://medium.gaii.ai/api/ 第三方 API
- **弱點**：手機廣告繁雜、介面過時、Long Polling 高負載

## 2. 我方技術棧

- **前端**：Nuxt 3 (SSR) + TypeScript + Tailwind CSS，部署 Vercel
- **後端**：FastAPI + PostgreSQL + Redis，WebSocket 即時推播
- **Monorepo**：`frontend/`（獨立 npm）+ `backend/`（獨立 Python venv）

## 3. 資料流架構

- Task A：模擬對手 Header 戳 gaii.ai API
- Task B：OpenCV + PaddleOCR 辨識 YouTube 直播
- Task C：定時爬取台彩官網（核實來源）
- 任一 Source 產出 → FastAPI WebSocket 廣播 → 存入 PostgreSQL

---

# Figma → Code 整合規範

## 4. 專案結構

```
frontend/
├── assets/css/main.css          # Tailwind 入口 + @layer 全域樣式
├── components/                  # Nuxt auto-import，無需手動引入
│   ├── LotteryBall.vue          # 原子：單顆球號（normal / special）
│   └── LotteryGameCard.vue      # 分子：遊戲卡片（logo + 資訊列 + 球號 + 按鈕）
├── layouts/default.vue          # Header (#59ADBC) + Footer
├── pages/
│   └── index.vue                # 首頁：倒數 + 每5分鐘區 + 每日區
├── nuxt.config.ts
└── tailwind.config.js
```

## 5. Design Tokens

所有 Token 定義於 `tailwind.config.js`，**不使用獨立 token 檔案**。

### 顏色

| 用途 | 值 | Tailwind / 用法 |
|------|-----|-----------------|
| 頁面底色 | `#F0EDE6` | `bg-cream`（custom）|
| Header 背景 | `#59ADBC` | inline style |
| Section banner | `#2da090 → #4ecdc4` | `.section-banner` CSS class |
| 資訊列背景 | sky-100 | `bg-sky-100` |
| 按鈕背景 | `#26a69a` | `.btn-sort` CSS class |
| 按鈕 hover | `#1e8a7e` | `.btn-sort:hover` |
| 按鈕 active | `#00796b` | `.btn-sort.active` |
| 卡片背景 | white | `bg-white` |

### 遊戲 Logo 顏色（`nameColor` prop）

| 遊戲 | 顏色 |
|------|------|
| 今彩539 | `#e53935` |
| 威力彩 | `#7b1fa2` |
| 大樂透 | `#e65100` |
| 49樂合彩 | `#e65100` |
| 39樂合彩 | `#f57c00` |
| 3星彩 | `#c8a000` |
| 4星彩 | `#e65100` |

### LotteryBall 球號顏色

| type | 樣式 |
|------|------|
| `normal` | `bg-white border-2 border-gray-300 text-gray-800 shadow-sm` |
| `special` | `bg-red-500 border-2 border-red-600 text-white shadow-sm` |

### 球號尺寸

| size | class |
|------|-------|
| `md`（預設）| `w-9 h-9 text-sm` |
| `sm` | `w-7 h-7 text-xs` |

## 6. 全域元件類別（`assets/css/main.css`）

```css
.section-banner   /* 綠色漸層區塊分隔 banner */
.game-card        /* 白色圓角卡片 + shadow */
.draw-info-bar    /* 淡藍色資訊列 */
.btn-sort         /* 排序按鈕（大小順序 / 開出順序）*/
```

## 7. 元件介面規範

### `LotteryBall.vue`
```ts
Props {
  number: number | null   // 顯示數字，null 顯示 '--'
  type?: 'normal' | 'special'  // 預設 'normal'
  size?: 'sm' | 'md'           // 預設 'md'
}
```

### `LotteryGameCard.vue`
```ts
Props {
  game: {
    name: string          // 遊戲名稱（顯示為 logo 文字）
    nameColor: string     // logo 文字顏色（hex）
    draw_term: string     // 期別
    draw_date: string     // 開獎日期
    draw_time: string     // 開獎時間
    next_draw: string     // 下期開獎日期
    numbers: number[]     // 主要號碼
    special_number: number | null  // 特別號（null = 不顯示）
  }
}
```

內建狀態：`sortMode: 'draw' | 'size'`，按鈕切換即時重排號碼。

## 8. 頁面佈局規則

- **行動優先（Mobile First）**：預設單欄，`sm:` 斷點切二欄
- **遊戲卡片格線**：`grid grid-cols-1 sm:grid-cols-2 gap-3`
- **頁面 max-width**：`max-w-5xl mx-auto px-2 sm:px-4`
- **區塊間距**：`space-y-3`

## 9. 廣告區塊

Figma 設計稿左右側有廣告區域，**不實作**，只做主要內容區。

## 10. Figma → 元件對應規則

從 Figma 稿件轉換時：
1. **顏色** → hex 對應 Tailwind token；若無對應加入 `tailwind.config.js` 或用 `bg-[#hex]`
2. **字型大小** → 對應 Tailwind `text-*` scale
3. **新元件** → 放 `components/`，PascalCase 命名
4. **全域可重用 class** → 定義在 `assets/css/main.css` 的 `@layer components`
5. **Logo 圖片** → 目前用有色文字代替，未來放 `public/logos/`

## 11. 資產管理

- 靜態資產 → `public/`（引用 `/filename`）
- CSS 內資產 → `assets/`（引用 `~/assets/`）
- `nuxt.config.ts` 的 `css` 陣列引入 `~/assets/css/main.css`
