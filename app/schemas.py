from pydantic import BaseModel, HttpUrl


class CreateURLRequest(BaseModel):
    url: HttpUrl


class CreateURLResponse(BaseModel):
    short_id: str
