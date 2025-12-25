from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from .schemas import CreateURLRequest, CreateURLResponse
from .services.url_service import URLService

app = FastAPI(title="URL Shortener")

url_service = URLService()


@app.post("/", response_model=CreateURLResponse, status_code=201)
async def create_short_url(payload: CreateURLRequest):
    short_id = await url_service.create_short_url(payload.url)
    return CreateURLResponse(short_id=short_id)


@app.get("/{short_id}")
async def redirect_to_original(short_id: str):
    original_url = await url_service.get_original_url(short_id)

    if not original_url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return RedirectResponse(url=original_url, status_code=307)
