from fastapi import APIRouter
from api.v1.endpoints import movie

api_router = APIRouter()

api_router.include_router(movie.router, prefix='/movies', tags=["movies"])


# api/v1/cursos
