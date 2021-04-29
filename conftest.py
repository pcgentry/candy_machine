from src.wuzzle import Wuzzle 
from src.candy import Candy
import pytest


@pytest.fixture()
def RandomWuzzle():
  return Wuzzle()


@pytest.fixture()
def RandomCandy():
  return Candy()

