import pytest
from src.fav_books import FavoriteBooks

@pytest.fixture
def mock_fb(mocker):
    return mocker.Mock(spec=FavoriteBooks)

