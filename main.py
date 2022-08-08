import validators
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud
from .base import errors, models, schemas

app = FastAPI()


@app.post("/get-short-url", response_model=schemas.URLScheme)
async def get_short_url(url: schemas.URLBase, db: Session = Depends(models.get_db)):
    pass


@app.post("/get-real-url")
async def get_real_url(new_url: str, db: Session = Depends(models.get_db)):
    pass
