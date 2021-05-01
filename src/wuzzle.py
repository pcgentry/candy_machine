import random
import uuid

import numpy as np

from src.config import FAKER, WORLD
from src.cookbook import Cookbook


class Wuzzle():
    '''
    Creates a wuzzle critter to eat CANDY. In the grand scheme of things, Wuzzles are actually simulated human consumers. The flavor preferences
    they have would not exist in our data set. It is the job of the Candy Machine to figure out what types of candy each Wuzzle likes best.

    The flavor preferences they have are actually the output of different models that would be making recommendations.
    '''
    def __init__(self):
      self.uuid = uuid.uuid1()
      self.name = FAKER.name()
      self.hunger = 0 
      self.generate_flavor_preferences()
      self.generate_cookbooks()
      self.licked_candy_ids = []
      self.potential_candy_ids = []


    def generate_flavor_preferences(self):
      preferences = []
      num_preferences = random.randint(1, len(WORLD["flavors"]))

      for flavor in np.random.choice(WORLD["flavors"], replace=False, size=num_preferences):
        self.flavor_preferences = {flavor : random.uniform(0, 1)}


    def generate_cookbooks(self):
      ''' Creates the cookbooks for this Wuzzle based on preferences '''
      self.cookbooks = []
      
      for flavor in self.flavor_preferences:
        self.cookbooks.append(Cookbook(flavor))


    def find_candies(self, candies):
      ''' get all candies that this Wuzzle can lick
      
      Keyword Arguments:
      candies -- This is a list containing candy objects that could be found. 
      '''

      if len(candies) == 0:
        return []

      for candy in candies:
        print(f"type: {candy.name}")
        if not candy.uuid in self.licked_candy_ids:
          self.potential_candy_ids.append(candy.uuid)
          
      return self.potential_candy_ids



    # def populate_menu(self):
    #   ''' populate the menu using cookbooks and flavors '''
    #   raise NotImplementedError


    # def can_lick_candy(candy):
    #   ''' Determine if a Candy is eligible for licking. '''

    #   raise NotImplementedError


    def lick_candy(candy):
      ''' Licking a candy means we have considered the Candy and decided to lick it. 
      
      Append to the licked list.'''

      self.licked_candy_ids.append(candy)
