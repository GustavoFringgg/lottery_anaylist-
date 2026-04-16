"""
台彩官網 Selenium 爬蟲
爬取最新開獎結果並存入 Supabase PostgreSQL

執行方式：
    python -m scrapers.lottery_scraper
"""

import os
import time
from datetime import date, datetime

import psycopg2
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL_SYNC")  # psycopg2 格式，見下方說明

# ── 台彩官網各遊戲對應資訊 ────────────────────────────────────────────────────
GAMES = {
    "lotto649": {
        "name": "大樂透",
        "url": "https://www.taiwanlottery.com/lotto/lotto649/history.aspx",
    },
    "super_lotto": {
        "name": "威力彩",
        "url": "https://www.taiwanlottery.com/lotto/superlotto638/history.aspx",
    },
    "daily_cash": {
        "name": "今彩539",
        "url": "https://www.taiwanlottery.com/lotto/dailycash/history.aspx",
    },
}


def build_driver(headless: bool = True) -> webdriver.Chrome:
    """建立 Chrome WebDriver（自動下載對應版本 ChromeDriver）。"""
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def parse_lotto649(driver: webdriver.Chrome) -> dict | None:
    """解析大樂透最新一期開獎結果。"""
    driver.get(GAMES["lotto649"]["url"])
    wait = WebDriverWait(driver, 10)

    # 等待開獎號碼表格載入
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.td_hisory")))
    time.sleep(1)

    rows = driver.find_elements(By.CSS_SELECTOR, "table.td_hisory tr")
    if len(rows) < 2:
        return None

    # 第一筆資料列（最新期）
    cells = rows[1].find_elements(By.TAG_NAME, "td")
    if len(cells) < 3:
        return None

    draw_term = cells[0].text.strip()
    draw_date_str = cells[1].text.strip()  # e.g. "113/04/15"
    number_cells = cells[2].find_elements(By.CSS_SELECTOR, "span.ball_green, span.ball_red")

    numbers = []
    special_number = None
    for i, cell in enumerate(number_cells):
        val = int(cell.text.strip())
        if "ball_red" in cell.get_attribute("class"):
            special_number = val
        else:
            numbers.append(val)

    # 民國轉西元
    parts = draw_date_str.split("/")
    draw_date = date(int(parts[0]) + 1911, int(parts[1]), int(parts[2]))

    return {
        "game_type": "lotto649",
        "draw_term": draw_term,
        "draw_date": draw_date,
        "numbers": numbers,
        "special_number": special_number,
        "source": "taiwanlottery.com",
    }


def parse_super_lotto(driver: webdriver.Chrome) -> dict | None:
    """解析威力彩最新一期開獎結果。"""
    driver.get(GAMES["super_lotto"]["url"])
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.td_hisory")))
    time.sleep(1)

    rows = driver.find_elements(By.CSS_SELECTOR, "table.td_hisory tr")
    if len(rows) < 2:
        return None

    cells = rows[1].find_elements(By.TAG_NAME, "td")
    if len(cells) < 3:
        return None

    draw_term = cells[0].text.strip()
    draw_date_str = cells[1].text.strip()
    number_cells = cells[2].find_elements(By.CSS_SELECTOR, "span.ball_green, span.ball_red")

    numbers = []
    special_number = None
    for cell in number_cells:
        val = int(cell.text.strip())
        if "ball_red" in cell.get_attribute("class"):
            special_number = val
        else:
            numbers.append(val)

    parts = draw_date_str.split("/")
    draw_date = date(int(parts[0]) + 1911, int(parts[1]), int(parts[2]))

    return {
        "game_type": "super_lotto",
        "draw_term": draw_term,
        "draw_date": draw_date,
        "numbers": numbers,
        "special_number": special_number,
        "source": "taiwanlottery.com",
    }


def parse_daily_cash(driver: webdriver.Chrome) -> dict | None:
    """解析今彩539最新一期開獎結果。"""
    driver.get(GAMES["daily_cash"]["url"])
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.td_hisory")))
    time.sleep(1)

    rows = driver.find_elements(By.CSS_SELECTOR, "table.td_hisory tr")
    if len(rows) < 2:
        return None

    cells = rows[1].find_elements(By.TAG_NAME, "td")
    if len(cells) < 3:
        return None

    draw_term = cells[0].text.strip()
    draw_date_str = cells[1].text.strip()
    number_cells = cells[2].find_elements(By.CSS_SELECTOR, "span.ball_green")

    numbers = [int(c.text.strip()) for c in number_cells]

    parts = draw_date_str.split("/")
    draw_date = date(int(parts[0]) + 1911, int(parts[1]), int(parts[2]))

    return {
        "game_type": "daily_cash",
        "draw_term": draw_term,
        "draw_date": draw_date,
        "numbers": numbers,
        "special_number": None,
        "source": "taiwanlottery.com",
    }


def upsert_draw(conn, data: dict):
    """將開獎結果 upsert 進 Supabase PostgreSQL。"""
    sql = """
        INSERT INTO draw_results (game_type, draw_term, draw_date, numbers, special_number, source)
        VALUES (%(game_type)s, %(draw_term)s, %(draw_date)s, %(numbers)s, %(special_number)s, %(source)s)
        ON CONFLICT (draw_term) DO NOTHING;
    """
    with conn.cursor() as cur:
        cur.execute(sql, {**data, "numbers": data["numbers"]})
    conn.commit()
    print(f"[{datetime.now():%H:%M:%S}] Upsert {data['game_type']} {data['draw_term']} ✓")


def run():
    """爬取三種遊戲最新開獎並存入資料庫。"""
    if not DATABASE_URL:
        raise RuntimeError("請在 .env 設定 DATABASE_URL_SYNC")

    conn = psycopg2.connect(DATABASE_URL)
    driver = build_driver(headless=True)

    parsers = [parse_lotto649, parse_super_lotto, parse_daily_cash]
    try:
        for parser in parsers:
            result = parser(driver)
            if result:
                upsert_draw(conn, result)
            else:
                print(f"[WARN] {parser.__name__} 解析失敗，略過。")
    finally:
        driver.quit()
        conn.close()


if __name__ == "__main__":
    run()
