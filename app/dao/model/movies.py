from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.dao.model.directors import DirectorBM
from app.dao.model.genres import GenreBM
from sqlalchemy.orm import relationship, RelationshipProperty
from app.dao.model.base import Base
import ujson


class Movie(Base):
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    director_id = Column(Integer, ForeignKey("director.id"), nullable=False)
    genre_id = Column(Integer, ForeignKey("genre.id"), nullable=False)
    rating = Column(Float, default=0.0)
    title = Column(String, nullable=False)
    trailer = Column(String, default="#")
    year = Column(Integer, nullable=False)
    director: RelationshipProperty = relationship("Director")
    genre: RelationshipProperty = relationship("Genre")

    def __repr__(self):
        return f"<Movie {self.title}>"


class MovieUpdateBM(BaseModel):
    description: str
    director_id: int
    genre_id: int
    rating: float
    title: str
    trailer: Optional[str]
    year: int

    class Config:
        orm_mode = True
        json_loads = ujson.loads


class MovieBMSimple(MovieUpdateBM):
    id: Optional[int]


class MovieBM(MovieBMSimple):
    director: DirectorBM
    genre: GenreBM
