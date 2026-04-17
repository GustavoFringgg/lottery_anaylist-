# 台彩分析 Lottery Analyst

台彩即時開獎分析平台。前端 Nuxt 3 SSR + 後端 FastAPI，WebSocket 即時推播。

---

## 專案結構

```
Lottery_Anaylist/
├── frontend/   # Nuxt 3 + TypeScript + Tailwind CSS
└── backend/    # FastAPI + PostgreSQL + Redis
```

---

## 環境需求

- Node.js >= 18
- Python >= 3.11
- PostgreSQL（預設 `localhost:5432`）
- Redis（預設 `localhost:6379`）

---

## 後端啟動

```bash
cd backend

# 建立虛擬環境（第一次）
python3 -m venv venv
source venv/bin/activate       # macOS / Linux
# venv\Scripts\activate        # Windows

# 安裝依賴（第一次）
pip install -r requirements.txt

# 複製環境變數範本並填入設定（第一次）
cp .env.example .env

# 啟動開發伺服器（port 8000）
python3 main.py
```

預設連線：

- PostgreSQL：`postgresql+asyncpg://postgres:postgres@localhost:5432/lottery`
- Redis：`redis://localhost:6379`

---

## 前端啟動

```bash
cd frontend

# 安裝依賴（第一次）
npm install

# 啟動開發伺服器（port 3000）
npm run dev
```

---

## 同時啟動前後端（根目錄捷徑）

```bash
# 安裝根目錄依賴（第一次）
npm install

# 啟動前端
npm run dev:frontend

# 啟動後端（另開終端機）
npm run dev:backend
```

---

## 常用指令

| 指令                              | 說明               |
| --------------------------------- | ------------------ |
| `npm run dev:frontend`            | 啟動前端開發伺服器 |
| `npm run dev:backend`             | 啟動後端開發伺服器 |
| `cd frontend && npm run build`    | 建置前端           |
| `cd frontend && npm run generate` | 靜態輸出前端       |
| `cd frontend && npm run preview`  | 預覽前端建置結果   |

---

## API 文件

後端啟動後可至以下路徑查看：

- Swagger UI：`http://localhost:8000/docs`
- ReDoc：`http://localhost:8000/redoc`
