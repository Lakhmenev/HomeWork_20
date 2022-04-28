from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService

from dao.genre import GenreDAO
from dao.director import DirectorDAO


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_one = Movie(id=1, title='Фильм_1', description='Описание к Фильм_1', trailer='треллер Фильм_1',
                      year=2019, rating=8.5, genre_id=1, director_id=1, genre=GenreDAO, director=DirectorDAO)
    movie_two = Movie(id=2, title='Фильм_2', description='Описание к Фильм_2', trailer='треллер Фильм_2',
                      year=2020, rating=7.5, genre_id=2, director_id=2, genre=GenreDAO, director=DirectorDAO)
    movie_three = Movie(id=1, title='Фильм_1', description='Описание к Фильм_3', trailer='треллер Фильм_3',
                        year=2021, rating=6.5, genre_id=3, director_id=3, genre=GenreDAO, director=DirectorDAO)

    movie_dao.get_one = MagicMock(return_value=movie_one)
    movie_dao.get_all = MagicMock(return_value=[movie_one, movie_two, movie_three])

    movie_dao.create = MagicMock(return_value=Movie(id=2))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):

        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_dict = {
            "title": 'Фильм_2',
            "description": 'Описание к Фильм_2',
            "trailer": 'треллер Фильм_2',
            "year": 2020,
            "rating": 7.5,
            "genre_id": 2,
            "director_id": 2
        }

        movie = self.movie_service.create(movie_dict)

        assert movie.id is not None

    def test_update(self):
        movie_dict = {
            "title": 'Фильм_3',
            "description": 'Описание к Фильм_3',
            "trailer": 'треллер Фильм_3',
            "year": 2021,
            "rating": 6.5,
            "genre_id": 3,
            "director_id": 3
        }

        self.movie_service.update(movie_dict)

    def test_delete(self):
        self.movie_service.delete(1)
