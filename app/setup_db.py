from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from os import environ

# use these 2 lines to give the db metadata to alembic
from app.dao.model import (  # noqa F401
    directors,
    genres,
    movies,
    users,
    rtokens,
    favorites,
)
from app.dao.model.base import Base  # noqa


BASE_DIR = Path(__file__).parent

TESTING = environ.get("TESTING")  # this will be used by pytest

if TESTING:
    engine = create_engine(
        f"sqlite:///{BASE_DIR.parent}/movies_test.db",
        connect_args={"check_same_thread": False},
        echo=True,
    )

else:
    engine = create_engine(
        f"sqlite:///{BASE_DIR.parent}/data/movies.db",
        connect_args={"check_same_thread": False},
        echo=False,
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
