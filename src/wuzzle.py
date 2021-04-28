from faker import Faker
import numpy as np
import random

class Wuzzle():
    '''
    Creates a wuzzle critter to eat CANDY.
    '''
    def __init__(self):
      self.fake = Faker()
      self.flavors = ['apple', 'toenail', 'earwax', 'green tea', 'peach', 'tarball', 'toe fuzz']
      self.name = self.fake.name()
      self.generate_flavor_preferences()
      self.dislikes = None

    def generate_flavor_preferences(self):
      self.flavor_preferences = {random.choice(self.flavors): .6}

    @classmethod
    def favorites(self):
      return self.flavors - self.dislikes