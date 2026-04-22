from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.core.database import AsyncSessionLocal
from app.service.fetchData import fetch_all_withoutBingo,fetch_bingo
from app.service.saveData import save_draws
import asyncio

async def run_games_job():
    draws = fetch_all_withoutBingo()
    async with AsyncSessionLocal() as session:
        await save_draws(session,draws)

async def run_bingo_job():
    draw = fetch_bingo()
    async with AsyncSessionLocal() as session:
        await save_draws(session,draw)

scheduler = AsyncIOScheduler()
scheduler.add_job(run_bingo_job, "interval", minutes=5)
scheduler.add_job(run_games_job, "cron", hour=21, minute=35)

if __name__ == "__main__":
    async def main():
        await run_games_job()
        await run_bingo_job()
    asyncio.run(main())
