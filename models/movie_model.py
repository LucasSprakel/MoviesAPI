from core.configs import settings

from sqlalchemy import Column, String, Integer


class MovieModel(settings.DBBaseModel):
    __tablename__ = 'movies'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    nota: int = Column(Integer)
    sinopse: str = Column(String())