台彩分析網站開發與競品技術規格書

1. 競品分析統整 (樂透研究院 pilio.idv.tw)
   目前市場排名第一的網站，具備高流量與強大的 SEO 排名，其技術特點如下：

前端架構： 傳統 ASP + jQuery。

通訊機制： 使用 Long Polling (長輪詢)。透過 articleMedia API 請求達成「不重整網頁即時更新」。(狀態常處於 pending 直到數據產出)。

數據來源： 透過 https://medium.gaii.ai/api/ 的第三方 API 獲取數據。

AI 應用： 陽春的 AI 自動生成文章，主要目的為 SEO 收錄 與長尾關鍵字佔領。

弱點： 手機端廣告繁雜、介面過時(90年代風格)、高流量下 Long Polling 對伺服器壓力極大。

2. 我方技術棧 (The "Fourth Place" Strategy)
   身為 Full-stack Engineer，我們採用現代化架構進行「降維打擊」：

前端 (Frontend)
框架： Nuxt 3 (SSR/SSG) 確保極致 SEO 與首屏載入速度。

樣式： Tailwind CSS 打造現代 Dashboard 質感。

部署： Vercel (利用 Edge Functions 達成極速分發)。

後端 (Backend)
框架： FastAPI (Python)。利用非同步特性 (Async/Await) 處理高併發 WebSocket。

資料庫： PostgreSQL (持久化歷史開獎數據) + Redis (即時數據快取)。

通訊： WebSocket。取代長輪詢，達成極低延遲的即時球號跳動體驗。

3. 核心數據邏輯與流程 (The Hybrid Moat)
   為了達成「全台最快」且「穩定」的目標，採用多源併行機制：

數據抓取層 (Scraper Layer):

Task A: 模擬對手 Request Header (Referer, User-Agent) 戳 gaii.ai API。

Task B: Python OpenCV + PaddleOCR 辨識 YouTube 直播畫面 (第一手資料)。

Task C: 定時爬取台彩官網 (最終核實來源)。

即時推播層 (Broadcaster):

號碼一旦由任何 Source 產出，FastAPI 立即透過 WebSocket 廣播。

持久化層 (Persistence):

確認後的數據存入 PostgreSQL，供 Nuxt 3 進行 SSR 渲染及歷史分析。

4. UI/UX 與產品差異化
   Mobile-First: 針對 91% 的手機用戶優化，極簡無廣告干擾。

即時感: 球號跳動動畫 (TransitionGroup)，增加開獎時的儀式感。

AI 功能: 未來導入 AI Agent 進行「投注回測」與「機率可視化」，而非單純產出文章。

5. 給 Claude Code 的指令建議 (Copy & Paste)
   「我正在開發一個台彩分析網站。後端使用 FastAPI + PostgreSQL + Redis，前端使用 Nuxt 3。
   目前已確認對手使用 Long Polling 戳 medium.gaii.ai 的 API。

請幫我寫一個 FastAPI 的 WebSocket Manager，負責廣播開獎號碼。

請幫我寫一個 Python 爬蟲範例，帶上 referer: https://www.pilio.idv.tw/ 模擬對手請求。

請幫我建立 PostgreSQL 的 schema，使用 INTEGER[] 存儲號碼。」
