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
    return db.query(models.URL).filter(models.URL.new_url == new_url).first()


async def updated_url_obj(db: Session, url_obj):
    if url_obj := await url_obj:
        url_obj.clicks += 1
        db.commit()
        return url_obj
    return errors.raise_bad_request(message="Url was not found")


async def show_real_url_scheme(db: Session, new_url: str) -> schemas.URLScheme:
    url_obj = await updated_url_obj(db, get_url_by_key(db, new_url))
    return schemas.URLScheme(
        main_url=url_obj.main_url, new_url=url_obj.new_url, clicks=url_obj.clicks
    )
