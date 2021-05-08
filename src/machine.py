import random
from joblib import dump, load

from river import compose
from river import linear_model
from river import metrics
from river import preprocessing
from river import datasets


from src.config import WORLD


class Machine():
  ''' 
  Machine makes the decisions about which CANDY goes to which Wuzzle. It uses the Wuzzles internal cookbook and menu attributes to make decisions.
  '''

  # def __init__(self, strategy="random", reward=10, punishment=-100) -> None:
  def __init__(self, strategy="logistic_regression", reward=10, punishment=-100) -> None:
    self.strategy = strategy


  def recommend_for_wuzzle(self, wuzzle, candies, menu_size=3):
    ''' 
    
    Fill the menu for a Wuzzle. We want to be able to use multiple strategies for simulation, so this is basically intended to be a case statement. 
    
    Each strategy needs to return a list of candy ids.

    '''
    if self.strategy == "random":
      # print(wuzzle.potential_candy_ids)s
      wuzzle.menu = self.suggest_by_random(wuzzle, candies)
      # print(wuzzle.menu)

    if self.strategy == "logistic_regression":
      wuzzle.menu = self.suggest_by_logistic_regression(wuzzle, candies)


  def suggest_by_random(self, wuzzle, candies, menu_size=3) -> list:
    ''' this implements the random strategy. In theory it should perform badly as it will not be able to tell which candies the wuzzle likes more '''

    if WORLD["menu_size"] > len(wuzzle.potential_candy_ids):
      menu_size = len(wuzzle.potential_candy_ids)
    else:
      menu_size = WORLD["menu_size"]

    return random.choices(wuzzle.potential_candy_ids, k=menu_size)


  def suggest_by_logistic_regression(self, wuzzle, candies, menu_size=3) -> list:
    ''' this implements the random strategy. In theory it should perform badly as it will not be able to tell which candies the wuzzle likes more '''

    if WORLD["menu_size"] > len(wuzzle.potential_candy_ids):
      menu_size = len(wuzzle.potential_candy_ids)
    else:
      menu_size = WORLD["menu_size"]

    return random.choices(wuzzle.potential_candy_ids, k=menu_size)


