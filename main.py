import validators
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud
from base import errors, models, schemas

app = FastAPI()


@app.post("/get-short-url", response_model=schemas.URLScheme)
async def get_short_url(url: schemas.URLBase, db: Session = Depends(models.get_db)):
    """Shorter for url"""
    if not validators.url(url.main_url):
        errors.raise_bad_request(message="Your provided URL is not valid")
    return await crud.create_short_url(db, url)


@app.post("/get-real-url")
async def get_real_url(new_url: str, db: Session = Depends(models.get_db)):
    """Get real url and update click counter"""
    return await crud.show_real_url_scheme(db, new_url)
