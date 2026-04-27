import httpx
from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()


@router.head("")
def health_check():
    return {"status": "ok"}


@router.get("/debug-fetch")
async def debug_fetch():
    results = {}
    for label, url in [("LAST_NUMBER_URL", settings.LAST_NUMBER_URL), ("NEXT_DRAW_URL", settings.NEXT_DRAW_URL)]:
        try:
            async with httpx.AsyncClient() as client:
                res = await client.get(url, timeout=10)
                results[label] = {"status": res.status_code, "ok": res.is_success}
        except httpx.ConnectTimeout:
            results[label] = {"error": "ConnectTimeout", "url": url}
        except Exception as e:
            results[label] = {"error": type(e).__name__, "detail": str(e)}
    return results
