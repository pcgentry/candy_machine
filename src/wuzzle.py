import random
from src.config import FLAVORS, FAKER
import uuid
import numpy as np

class Wuzzle():
    '''
    Creates a wuzzle critter to eat CANDY. In the grand scheme of things, Wuzzles are actually simulated human consumers. The flavor preferences
    they have would not exist in our data set. It is the job of the Candy Machine to figure out what types of candy each Wuzzle likes best.

    The flavor preferences they have are actually the output of different models that would be making recommendations.
    '''
    def __init__(self):
      self.uuid = uuid.uuid1()
      self.flavors = FLAVORS
      self.name = FAKER.name()
      self.generate_flavor_preferences()
      self.hunger = 0 
      # self.dislikes = None


    def generate_flavor_preferences(self):
      preferences = []
      num_preferences = random.randint(1, len(self.flavors))

      for flavor in np.random.choice(self.flavors, replace=False, size=num_preferences):
        self.flavor_preferences = {flavor : random.uniform(0, 1)}

