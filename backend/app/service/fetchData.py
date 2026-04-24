import httpx
from datetime import datetime
from app.core.config import settings


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

# TODO: 可以補上 timeout的catch
def fetch_last_number() -> dict:
    res = httpx.get(settings.LAST_NUMBER_URL, headers=HEADERS, timeout=10)
    res.raise_for_status()
    data = res.json()
    if data["rtCode"] != 0:
        raise Exception(f"API 錯誤: {data['rtMsg']}")
    return data["content"]


def fetch_next_draw_date() -> dict:
    res = httpx.get(settings.NEXT_DRAW_URL, headers=HEADERS, timeout=10)
    res.raise_for_status()
    data = res.json()
    if data["rtCode"] != 0:
        raise Exception(f"API 錯誤: {data['rtMsg']}") 
    result = {}
    for item in data["content"]["nextDrawDateList"]:
        raw = item["drawDate"]
        if len(raw) == 12:  
            result[item["gameCode"]] = datetime.strptime(raw, "%Y%m%d%H%M")
        else: 
            result[item["gameCode"]] = datetime.strptime(raw, "%Y%m%d")
    return result


def fetch_all_withoutBingo() -> list[dict]:
    content = fetch_last_number()
    next_draw_map = fetch_next_draw_date()

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


def fetch_bingo() -> list[dict]:
    content = fetch_last_number()
    next_draw_map = fetch_next_draw_date()

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
    for draw in fetch_all_withoutBingo():
        print(draw)
    print(fetch_bingo())
