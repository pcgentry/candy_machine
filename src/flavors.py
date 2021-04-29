from src.config import FLAVORS
import numpy as np
import random


class Flavors():
  ''' This Class handles common flavor functionality. '''

  def __init__(self) -> None:
      self.flavors = FLAVORS
  

  def make_flavors(self, number_of_flavors=1):

    flavor_set = {}
    for flavor in np.random.choice(self.flavors, replace=False, size=number_of_flavors):
      flavor_set[flavor] = random.uniform(0, 1)

    return flavor_set


