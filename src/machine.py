"""The Macfhine class."""
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
  """Machine makes the decisions about which CANDY goes to which Wuzzle.

  It uses the Wuzzles internal cookbook and menu attributes to make decisions.
  """

  def __init__(self, strategy, reward=10, punishment=-100):
    self.strategy = strategy

    self.model = DecisionTree() if strategy == 'decision_tree' else Random()

    self.include_hunger = self.model.include_hunger
    self.stats = {}


  def recommend_for_wuzzle(self, wuzzle, candies, menu_size=3):
    """Fill the menu for a Wuzzle. We want to be able to use multiple strategies for simulation, so this is basically intended to be a case statement.

    Each strategy needs to return a list of candy ids.
    """

    wuzzle.menu = self.model.suggest(wuzzle, candies)


  def train_one(self, X=[], y=1):
    self.model.train_one(X, y)

  def save_model(self):
    self.model.save_model()

  def report_accuracy(self):
    return self.model.accuracy_metric_float
