from model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def init_db():
    Base.metadata.create_all(bind=engine)

def get_session():
    return Session(engine)


DATABASE_URL = "sqlite:///:feedings.db"

engine = create_engine(DATABASE_URL, echo=False)


