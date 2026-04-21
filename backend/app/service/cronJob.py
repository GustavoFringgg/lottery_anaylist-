from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.core.database import AsyncSessionLocal
from app.service.fetchData import fetch_all
from app.service.saveData import save_draws
import asyncio


async def run_job():
    draws = fetch_all()
    async with AsyncSessionLocal() as session:
        await save_draws(session,draws)

scheduler = AsyncIOScheduler()
scheduler.add_job(run_job, "interval", minutes=5)



if __name__ == "__main__":
    asyncio.run(run_job())
