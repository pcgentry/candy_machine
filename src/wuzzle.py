import random
from typing import List
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
      self.life = 1
      self.hunger = 0.0
      self.lick_counter = 0
      self.nightly_lick_counter = 0
      self.licked_flavor_counter = dict.fromkeys(WORLD["flavors"], 0)

      self.uuid = uuid.uuid1()
      self.name = FAKER.name()

      self.generate_flavor_preferences()
      self.generate_cookbooks()
      
      self.licked_candy_ids = []
      self.potential_candy_ids = []
      self.menu = []


    def __repr__(self) -> str:
        return self.name

    def generate_flavor_preferences(self):
      preferences = []
      num_preferences = random.randint(1, len(WORLD["flavors"]))
      self.flavor_preferences = {}
      for flavor in np.random.choice(WORLD["flavors"], replace=False, size=num_preferences):
        self.flavor_preferences[flavor]= random.uniform(0, 1)


    def generate_cookbooks(self):
      ''' Creates the cookbooks for this Wuzzle based on preferences '''
      self.cookbooks = []
      
      for flavor in self.flavor_preferences:
        self.cookbooks.append(Cookbook(flavor))


    def populate_cookbooks(self, world_candies):
      for cookbook in self.cookbooks:
        current_flavor = cookbook.flavor

        for candy in world_candies:
          
          if candy.uuid in self.potential_candy_ids:
            if current_flavor in candy.flavors:
              cookbook.candy_ids.append(candy.uuid)


    def find_candies(self, candies) -> List:
      ''' get all candies that this Wuzzle can lick
      
      Keyword Arguments:
      candies -- This is a list containing candy objects that could be found. 
      '''
      self.potential_candy_ids = []

      if len(candies) == 0:
        return []

      for candy in candies:
        if not candy.uuid in self.licked_candy_ids:
          self.potential_candy_ids.append(candy.uuid)
          
      return self.potential_candy_ids


    def get_features(self, candy, include_hunger=True):
      # print(self.flavor_preferences)
      # print(candy.flavors)

      w_flavors = {"w_" + str(key): val for key, val in self.licked_flavor_counter.items()}
      c_flavors = {"c_" + str(key): val for key, val in candy.flavors.items()}
      feature_arr = {**w_flavors, **c_flavors}

      if include_hunger:
        feature_arr['w_hunger'] = self.hunger
        feature_arr['c_hunger'] = candy.hunger

      # print(feature_arr)
      return feature_arr


    def check_menu(self, candies, machine):
      ''' Go through the menu and decide whether to lick each candy. '''
      self.nightly_lick_counter = 0
      
      for candy_id in self.menu:
        # Pretty sure this is horribly expensive and wasteful way to do this
        for candy in candies:
          # print(candy.uuid)

          if candy.uuid == candy_id:
            training_target = 0

            if candy.life == 1:

              # At this point we have the right candy object and at least qualified it as alive
              # print (f"Trying to lick: {candy.name}")
              for flavor in candy.flavors:
                if flavor in self.flavor_preferences:
                  # print(f"likes {flavor}")
                  if random.uniform(0, 1) > self.flavor_preferences[flavor]:
                    # print(f"LICKS **** {flavor}")
                    self.lick_candy(candy, flavor)
                    training_target = 1
                    
            machine.train_one(self.get_features(candy, include_hunger=machine.include_hunger), training_target)



    def lick_candy(self, candy, flavor):
      ''' Licking a candy means we have considered the Candy and decided to lick it. 
      
      Append to the licked list.'''

      self.hunger = 0
      candy.hunger = 0
      self.licked_candy_ids.append(candy.uuid)
      self.lick_counter += 1
      self.nightly_lick_counter += 1
      self.licked_flavor_counter[flavor] += 1
      return 1
