from .model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from contextlib import contextmanager


def init_db():
    Base.metadata.create_all(bind=engine)

@contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


DATABASE_URL = "sqlite:///feedings.db"

engine = create_engine(DATABASE_URL, echo=False)
