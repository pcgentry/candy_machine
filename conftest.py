from src.wuzzle import Wuzzle 
from src.candy import Candy
from src.flavors import Flavors
from src.world import World
import pytest


@pytest.fixture()
def RandomWorld():
  return World()

@pytest.fixture()
def RandomWuzzle():
  return Wuzzle()


@pytest.fixture()
def RandomCandy():
  return Candy()


@pytest.fixture()
def RandomFlavors():
  return Flavors()
