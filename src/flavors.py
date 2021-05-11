"""The Flavor class."""
import random
from typing import Dict

import numpy as np

from src.config import WORLD

class Flavors():
  """Flavors in this context are actually representations of outputs from different matching models. Each Wuzzle has a queue for each flavor, and
  wuzzles will like flavors with different probabilities.

  It is the job of the Candy Machine to figure these out and feed each wuzzle an ideal mix of flavors.
  """

  def __init__(self):
      self.flavors = WORLD["flavors"]


  def make_flavors(self, number_of_flavors=1) -> Dict[str, float]:

    flavor_set = {}
    for flavor in np.random.choice(self.flavors, replace=False, size=number_of_flavors):
      flavor_set[flavor] = random.uniform(0, 1)

    return flavor_set
