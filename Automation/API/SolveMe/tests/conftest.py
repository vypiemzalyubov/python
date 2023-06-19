import pytest
import requests
from configuration import SERVICE_URL
from src.generators.player import Player

@pytest.fixture
def fixture_get_users():
    response = requests.get(url=SERVICE_URL)
    return response

@pytest.fixture
def get_player_generator():
    """
    Пример фикстуры для инициализации объекта генератора и передачу его в
    тест.
    Fixture that initialize generator object and returns it into autotest.
    """
    return Player()