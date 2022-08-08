from sqlalchemy import Column, Integer, String

from base import database


class URL(database.Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    new_url = Column(String, unique=True, index=True)
    main_url = Column(String, index=True)
    clicks = Column(Integer, default=0)


database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
