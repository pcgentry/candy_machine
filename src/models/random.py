"""The Random class."""
import random
from typing import List

from river import metrics

from src.config import WORLD

class Random():

  def __init__(self):
    self.accuracy_metric_float = 0.0
    self.accuracy = metrics.Accuracy()
    self.trainings = 0
    self.include_hunger = True

  def suggest(self, wuzzle, candies=[], menu_size=3) -> List[int]:
    """Return a suggestion.

    In theory it should perform badly as it will not be able to tell which candies the wuzzle likes more.
    """

    if WORLD["menu_size"] > len(wuzzle.potential_candy_ids):
      menu_size = len(wuzzle.potential_candy_ids)
    else:
      menu_size = WORLD["menu_size"]

    return random.choices(wuzzle.potential_candy_ids, k=menu_size)

  def train_one(self, X=[], y=[]):
    self.trainings += 1
    pass

  def train_one(self, X=[], y=[]):
    self.accuracy = self.accuracy.update(y, 1)  # update the metric
    self.accuracy_metric_float = self.accuracy.get()

  def save_model(self):
    pass

  def predict(self, X):
    return 1
