from src.config import FLAVORS
import numpy as np
import random


class Flavors():
  ''' 
  Flavors in this context are actually representations of outputs from different matching models. Each Wuzzle has a queue for each flavor, and 
  wuzzles will like flavors with different probabilities. It is the job of the Candy Machine to figure these out and feed each wuzzle an ideal 
  mix of flavors.
  '''

  def __init__(self) -> None:
      self.flavors = FLAVORS
  

  def make_flavors(self, number_of_flavors=1):

    flavor_set = {}
    for flavor in np.random.choice(self.flavors, replace=False, size=number_of_flavors):
      flavor_set[flavor] = random.uniform(0, 1)

    return flavor_set


