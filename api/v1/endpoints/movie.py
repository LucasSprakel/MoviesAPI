from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.movie_model import MovieModel
from schemas.movie_schema import MovieSchema
from core.deps import get_session


router = APIRouter()


# POST curso
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=MovieSchema)
async def post_movie(movie: MovieSchema, db: AsyncSession = Depends(get_session)):
    novo_movie = MovieModel(titulo=movie.titulo, nota=movie.nota, sinopse=movie.sinopse)
    
    db.add(novo_movie)
    await db.commit()

    return novo_movie


#GET movie
@router.get('/', response_model=List[MovieSchema])
async def get_movies(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MovieModel)
        result = await session.execute(query)
        movies: List[MovieModel] = result.scalars().all()

        return movies


# GET movie
@router.get('/{movie_id}', response_model=MovieSchema, status_code=status.HTTP_200_OK)
async def get_movie(movie_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MovieModel).filter(MovieModel.id == movie_id)
        result = await session.execute(query)
        movie = result.scalar_one_or_none()

        if movie:
            return movie
        else:
            raise HTTPException(detail='Movie Not Found', status_code=status.HTTP_404_NOT_FOUND)


# PUT movie
@router.put('/{movie_id}', response_model=MovieSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_movie(movie_id: int, movie: MovieSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MovieModel).filter(MovieModel.id == movie_id)
        result = await session.execute(query)
        movie_up = result.scalar_one_or_none()

        if movie_up:
            movie_up.titulo = movie.titulo
            movie_up.nota = movie.nota
            movie_up.sinopse = movie.sinopse

            await session.commit()

            return movie_up
        else:
            raise HTTPException(detail='Movie Not Found', status_code=status.HTTP_404_NOT_FOUND)


# DELETE movie
@router.delete('/{movie_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(movie_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MovieModel).filter(MovieModel.id == movie_id)
        result = await session.execute(query)
        movie_del = result.scalar_one_or_none()

        if movie_del:
            
            await session.delete(movie_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)