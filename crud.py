from sqlalchemy.orm import Session

from . import core
from .base import errors, models, schemas


async def create_short_url(db: Session, url: schemas.URLScheme):
    generate_url = models.URL(main_url=url.main_url, new_url=core.create_random_url())
    db.add(generate_url)
    db.commit()
    db.refresh(generate_url)
    return generate_url


async def get_url_by_key(db: Session, new_url: str):
    pass

async def updated_url_obj(db: Session, url_obj):
    pass

async def show_real_url_scheme(db: Session, new_url: str) -> schemas.URLScheme:
    pass
