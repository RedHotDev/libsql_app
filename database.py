from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine("sqlite:///library.db", echo=True)

SessionLocal = sessionmaker(autocommit=False,  bind=engine)

class Base(DeclarativeBase):
    pass


def get_db():
    return SessionLocal()


