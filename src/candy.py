"""The Candy class."""
import random
import uuid

from src.config import FAKER
from src.flavors import Flavors


flavors = Flavors()

class Candy():
  """A Candy is an individual piece of Candy.

  They are fed to wuzzles and have different flavors. In the grand scheme of things, CANDY represents a match that a
  Wuzzle might like. In the non-metaphorical sense, a CANDY might be a particular movie, such as The Princess Bride, and
  its flavor corresponds to whatever recommender alg. it was recommended by. NOTE: flavor does NOT represent individual
  features in this metaphor.
  """

  def __init__(self):
    # We reverse the string here to differentiate Wuzzle names from CANDY names
    # ^^^^ I don't see a string being reversed.... where's the string reversal?
    self.life = 1
    self.hunger = 0.0
    self.name = FAKER.safe_color_name()
    self.uuid = uuid.uuid1()
    self.num_flavors = random.randint(1, len(flavors.flavors))
    self.flavors = flavors.make_flavors(self.num_flavors)


  def __repr__(self) -> str:
    return self.name
