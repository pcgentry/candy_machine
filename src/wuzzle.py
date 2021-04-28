from faker import Faker
import numpy as np
import random
from config import FLAVORS

class Wuzzle():
    '''
    Creates a wuzzle critter to eat CANDY.
    '''
    def __init__(self):
      self.fake = Faker()
      self.flavors = FLAVORS
      self.name = self.fake.name()
      self.generate_flavor_preferences()
      # self.dislikes = None


    def generate_flavor_preferences(self):
      preferences = []
      num_preferences = random.randint(1, len(self.flavors))

      for flavor in np.random.choice(self.flavors, replace=False, size=num_preferences):
        self.flavor_preferences = {flavor : random.uniform(0, 1)}


    # # @classmethod
    # def favorites(self):
    #   return random.choice(self.flavors)