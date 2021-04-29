from src.config import FAKER
import uuid
import random

from src.config import FAKER
from src.flavors import Flavors


flavors = Flavors()


class Candy():

  def __init__(self) -> None:
    self.name = FAKER.name()
    self.num_flavors = random.randint(1, len(flavors.flavors))
    self.flavors = flavors.make_flavors(self.num_flavors)

