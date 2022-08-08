from sqlalchemy.orm import Session

from . import core
from .base import errors, models, schemas


async def create_short_url(db: Session, url: schemas.URLScheme):
    pass

async def get_url_by_key(db: Session, new_url: str):
    pass

async def updated_url_obj(db: Session, url_obj):
    pass

async def show_real_url_scheme(db: Session, new_url: str) -> schemas.URLScheme:
    pass
