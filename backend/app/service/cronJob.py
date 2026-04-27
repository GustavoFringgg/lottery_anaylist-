from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.core.database import AsyncSessionLocal
from app.service.fetchData import fetch_all_withoutBingo,fetch_bingo
from app.service.saveData import save_draws
import asyncio
import logging
logger = logging.getLogger(__name__)

async def run_games_job():
    logger.info("開始抓取最新樂透資料")
    try:
        draws = await fetch_all_withoutBingo()
        async with AsyncSessionLocal() as session:
            await save_draws(session, draws)
        logger.info(f"完成，最新日期：{draws[0]['draw_date']}")
    except Exception as e:
        logger.error(f"樂透資料抓取失敗：{e}")

async def run_bingo_job():
    logger.info("開始抓取最新BingoBingo資料")
    try:
        draw = await fetch_bingo()
        async with AsyncSessionLocal() as session:
            await save_draws(session, draw)
        logger.info(f"完成，最新日期：{draw[0]['draw_date']}")
    except Exception as e:
        logger.error(f"BingoBingo 抓取失敗：{e}")


scheduler = AsyncIOScheduler(timezone="Asia/Taipei")
scheduler.add_job(
      run_bingo_job,
      "cron",
      day_of_week="mon-sun",
      hour="7-23",
      minute="*/5", 
  )
scheduler.add_job(run_games_job, "cron", day_of_week="mon-sat",hour = 21, minute = 30)

if __name__ == "__main__":
    async def main():
        await run_games_job()
        await run_bingo_job()
    asyncio.run(main())
