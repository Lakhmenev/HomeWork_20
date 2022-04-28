from unittest.mock import MagicMock

import pytest

from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    don = Director(id=1, name='Don')
    dima = Director(id=2, name='Dima')
    kely = Director(id=3, name='Kely')

    director_dao.get_one = MagicMock(return_value=don)
    director_dao.get_all = MagicMock(return_value=[don, dima, kely])

    director_dao.create = MagicMock(return_value=Director(id=2))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        director_dict = {
            "name": "Dima"
        }

        director = self.director_service.create(director_dict)

        assert director.id is not None

    def test_update(self):
        director_dict = {
            "id": 3,
            "name": "Kely"
        }

        self.director_service.update(director_dict)

    def test_delete(self):
        self.director_service.delete(1)
