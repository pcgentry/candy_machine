import random

from src.config import WORLD


class Machine():
  ''' 
  Machine makes the decisions about which CANDY goes to which Wuzzle. It uses the Wuzzles internal cookbook and menu attributes to make decisions.
  '''

  def __init__(self, strategy="random") -> None:
    self.strategy = "random"


  def recommend_for_wuzzle(self, wuzzle, candies, menu_size=3):
    ''' 
    
    Fill the menu for a Wuzzle. We want to be able to use multiple strategies for simulation, so this is basically intended to be a case statement. 
    
    Each strategy needs to return a list of candy ids.

    '''
    if self.strategy == "random":
      # print(wuzzle.potential_candy_ids)s
      wuzzle.menu = self.suggest_by_random(wuzzle, candies)
      # print(wuzzle.menu)

  def suggest_by_random(self, wuzzle, candies, menu_size=3) -> list:
    ''' this implements the random strategy. In theory it should perform badly as it will not be able to tell which candies the wuzzle likes more '''

    if WORLD["menu_size"] > len(wuzzle.potential_candy_ids):
      menu_size = len(wuzzle.potential_candy_ids)
    else:
      menu_size = WORLD["menu_size"]

    return random.choices(wuzzle.potential_candy_ids, k=menu_size)


