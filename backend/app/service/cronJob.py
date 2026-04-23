from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.core.database import AsyncSessionLocal
from app.service.fetchData import fetch_all_withoutBingo,fetch_bingo
from app.service.saveData import save_draws
import asyncio
import logging
logger = logging.getLogger(__name__)

async def run_games_job():
    logger.info("開始抓取最新樂透資料")
    draws = fetch_all_withoutBingo()
    async with AsyncSessionLocal() as session:
        await save_draws(session,draws)
    logger.info(f"完成，開獎日期：{draws[0]['draw_date']}")
async def run_bingo_job():
    draw = fetch_bingo()
    async with AsyncSessionLocal() as session:
        await save_draws(session,draw)

scheduler = AsyncIOScheduler(timezone="Asia/Taipei")
# scheduler.add_job(run_bingo_job, "interval", minutes=5)
scheduler.add_job(run_games_job, "cron", hour=6, minute=30)

if __name__ == "__main__":
    async def main():
        await run_games_job()
        await run_bingo_job()
    asyncio.run(main())
