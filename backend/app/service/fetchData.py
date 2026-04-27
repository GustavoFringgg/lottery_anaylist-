import httpx
import asyncio
import logging
from datetime import datetime
from app.core.config import settings
from tenacity import AsyncRetrying, stop_after_attempt, wait_fixed, retry_if_exception_type, before_sleep_log

HEADERS = {
    "User-Agent": settings.HEADER_USER_AGENT,
    "Accept": settings.HEADER_ACCEPT,
    "Accept-Language": settings.HEADER_ACCEPT_LANGUAGE,
    "Referer": settings.HEADER_REFERER,
}

GAME_NAMES = {
    1102: "BingoBingo",
    1121: "49樂合彩",
    1197: "39樂合彩",
    2108: "3星彩",
    2109: "4星彩",
    5118: "大樂透",
    5120: "今彩539",
    5134: "威力彩",
}

logger = logging.getLogger(__name__)


async def fetch_last_number() -> dict:
    async for attempt in AsyncRetrying(
        retry=retry_if_exception_type(httpx.TimeoutException),
        stop=stop_after_attempt(3),
        wait=wait_fixed(10),
        before_sleep=before_sleep_log(logger, logging.WARNING),
    ):
        with attempt:
            async with httpx.AsyncClient() as client:
                res = await client.get(settings.LAST_NUMBER_URL, headers=HEADERS, timeout=15)
                res.raise_for_status()
                data = res.json()
                if data["rtCode"] != 0:
                    raise Exception(f"fetch_last_number API 錯誤: {data['rtMsg']}")
                return data["content"]


async def fetch_next_draw_date() -> dict:
    async for attempt in AsyncRetrying(
        retry=retry_if_exception_type(httpx.TimeoutException),
        stop=stop_after_attempt(3),
        wait=wait_fixed(10),
        before_sleep=before_sleep_log(logger, logging.WARNING),
    ):
        with attempt:
            async with httpx.AsyncClient() as client:
                res = await client.get(settings.NEXT_DRAW_URL, headers=HEADERS, timeout=15)
                res.raise_for_status()
                data = res.json()
                if data["rtCode"] != 0:
                    raise Exception(f"fetch_next_draw_date API 錯誤: {data['rtMsg']}")
                result = {}
                for item in data["content"]["nextDrawDateList"]:
                    raw = item["drawDate"]
                    if len(raw) == 12:
                        result[item["gameCode"]] = datetime.strptime(raw, "%Y%m%d%H%M")
                    else:
                        result[item["gameCode"]] = datetime.strptime(raw, "%Y%m%d")
                return result


async def fetch_all_withoutBingo() -> list[dict]:
    content, next_draw_map = await asyncio.gather(
        fetch_last_number(),
        fetch_next_draw_date(),
    )
    results = []
    for item in content["lastNumberList"]:
        game_code = item["gameCode"]
        results.append({
            "game_code": game_code,
            "game_name": GAME_NAMES.get(game_code, str(game_code)),
            "term": item["period"],
            "draw_date": datetime.strptime(item["drawDate"], "%Y-%m-%d %H:%M:%S").date(),
            "numbers": item["lotNumber"],
            "next_draw_date": next_draw_map.get(game_code),
        })
    return results


async def fetch_bingo() -> list[dict]:
    content, next_draw_map = await asyncio.gather(
        fetch_last_number(),
        fetch_next_draw_date(),
    )
    results = []
    bingo = content["bingo"]
    game_code = bingo["gameCode"]
    results.append({
        "game_code": game_code,
        "game_name": GAME_NAMES.get(game_code, str(game_code)),
        "term": bingo["period"],
        "draw_date": datetime.strptime(bingo["drawDate"], "%Y-%m-%d %H:%M:%S"),
        "numbers": sorted(bingo["lotNumber"]),
        "next_draw_date": next_draw_map.get(game_code),
        "lot_special": bingo["lotSpecial"],
        "lot_big_small": bingo["lotBigSmall"],
        "lot_odd_even": bingo["lotOddEven"],
    })
    return results


if __name__ == "__main__":
    async def main():
        for draw in await fetch_all_withoutBingo():
            print(draw)
        print(await fetch_bingo())
    asyncio.run(main())
