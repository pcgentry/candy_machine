import random

from src.config import WORLD


class Machine():
  ''' 
  Machine makes the decisions about which CANDY goes to which Wuzzle. It uses the Wuzzles internal cookbook and menu attributes to make decisions.
  '''

  def __init__(self, strategy="random") -> None:
    self.strategy = "random"


  def recommend_for_wuzzle(self, wuzzle, candies):
    ''' 
    
    Fill the menu for a Wuzzle. We want to be able to use multiple strategies for simulation, so this is basically intended to be a case statement. 
    
    Each strategy needs to eturn a list of candy ids.

    '''
    if self.strategy == "random":
      wuzzle.menu = self.suggest_by_random(wuzzle)


  def suggest_by_random(self, wuzzle) -> list:
    ''' this implements the random strategy. In theory it should perform badly as it will not be able to tell which candies the wuzzle likes more '''
    return random.choices(wuzzle.potential_candy_ids, k = WORLD["menu_size"])


