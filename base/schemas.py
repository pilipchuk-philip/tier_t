from pydantic import BaseModel


class URLBase(BaseModel):
    main_url: str


class URLScheme(URLBase):
    clicks: int
    new_url: str

    class Config:
        orm_mode = True

