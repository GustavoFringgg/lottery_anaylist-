import logging
import os
import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse
from app.service.cronJob import scheduler
from app.core.config import settings
from app.core.database import engine
from app.api.routers import lottery as lottery_router,health
from app.models import lottery

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 啟動時執行（yield 之前）
    # scheduler.start()    
    logger.info("Service started")
    yield
    # 關閉時執行（yield 之後）
    # scheduler.shutdown()
    logger.info("Service stopped")



app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0",
    description="Lottery Analysis API",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lottery_router.router,prefix='/api/lottery', tags=['lottery_router'])
app.include_router(health.router,prefix='/api/health', tags=['health'])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    is_dev = os.environ.get("APP_ENV", "development") == "development"
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=is_dev,
    )
