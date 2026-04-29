from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.core.database import AsyncSessionLocal
from app.service.fetchData import fetch_all_withoutBingo,fetch_bingo
from app.service.saveData import save_draws
import asyncio
import logging
import json
import httpx
from datetime import date, datetime
logger = logging.getLogger(__name__)

async def run_games_job():
    logger.info("開始抓取最新樂透資料")
    try:
        draws = await fetch_all_withoutBingo()
        async with AsyncSessionLocal() as session:
            await save_draws(session, draws)
        logger.info(f"完成，最新日期：{draws[0]['draw_date']}")

        now = datetime.now()
        iso = now.isocalendar()
        day_map = {1:"mon",2:"tue",3:"wed",4:"thu",5:"fri",6:"sat",7:"sun"}

        def default_serializer(obj):
            if isinstance(obj, (datetime, date)):
                return obj.isoformat()
            return str(obj)

        content = f"[樂透抓取 log] {now.strftime('%Y-%m-%d %H:%M')}\n\n" + \
                  json.dumps(draws, ensure_ascii=False, indent=2, default=default_serializer)

        try:
            async with httpx.AsyncClient() as client:
                await client.post(
                    "https://snap-thought.onrender.com/api/v1/notes",
                    json={
                        "year": iso[0],
                        "week": iso[1],
                        "dayKey": day_map[iso[2]],
                        "content": content,
                        "tags": ["Claude筆記"],
                    },
                    timeout=10,
                )
        except Exception as log_err:
            logger.warning(f"SnapThought log 寫入失敗：{log_err}")

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
      minute="2/5", 
      second="10"
  )
scheduler.add_job(run_games_job, "cron", day_of_week="mon-sat", hour=21, minute=30)

if __name__ == "__main__":
    async def main():
        await run_games_job()
        await run_bingo_job()
    asyncio.run(main())
