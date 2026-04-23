from fastapi import HTTPException,Security
from fastapi.security.api_key import APIKeyHeader
from app.core.config import settings


api_key_header = APIKeyHeader(name="X-API-Key",auto_error=False)

async def verify_api_key(api_key:str | None = Security(api_key_header)):
    if not api_key or api_key != settings.API_KEY:
         raise HTTPException(status_code=403, detail="Invalid")
    