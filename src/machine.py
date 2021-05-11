from joblib import dump, load

# from river import compose
# from river import linear_model
# from river import metrics
# from river import preprocessing
# from river import datasets


from src.config import WORLD
from src.models.random import Random
from src.models.tree import DecisionTree


class Machine():
  ''' 
  Machine makes the decisions about which CANDY goes to which Wuzzle. It uses the Wuzzles internal cookbook and menu attributes to make decisions.
  '''

  # def __init__(self, strategy="random", reward=10, punishment=-100) -> None:
  def __init__(self, strategy="random", reward=10, punishment=-100) -> None:
    self.strategy = strategy
    self.model = DecisionTree()


  def recommend_for_wuzzle(self, wuzzle, candies, menu_size=3):
    ''' 
    
    Fill the menu for a Wuzzle. We want to be able to use multiple strategies for simulation, so this is basically intended to be a case statement. 
    
    Each strategy needs to return a list of candy ids.

    '''
    if self.strategy == "random":
      # print(wuzzle.potential_candy_ids)s
      wuzzle.menu = Random.suggest(wuzzle, candies)
      # print(wuzzle.menu)

    if self.strategy == "decision_tree":
      # wuzzle.menu = self.suggest_by_logistic_regression(wuzzle, candies)
      wuzzle.menu = self.model.suggest(wuzzle, candies)

  def train_one(self, X=[], y=1):
    self.model.train_one(X, y)

  def save_model(self):
    self.model.save_model()

