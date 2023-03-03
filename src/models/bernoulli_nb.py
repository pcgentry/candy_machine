"""The DecisionTree class."""
from os import path
from typing import List
import random

from joblib import dump, load
from river import tree, metrics, compat

from sklearn.naive_bayes import BernoulliNB as BNB

from src.config import WORLD


class BernoulliNB():

  def __init__(self, load_from_file=False):
    """Create a persistent model file if there isn't one. If one exists, use it."""

    self.file_path = 'models/decision_tree.joblib'
    self.include_hunger = False
    self.accuracy_metric_float = 0.0
    self.accuracy = metrics.Accuracy()
    self.trainings = 0


    if load_from_file and path.exists(self.file_path):
      self.model = load(self.file_path)
    else:
      # self.model = compat.convert_sklearn_to_river(
      #     estimator=MLPClassifier(random_state=1, max_iter=300),
      #     classes=[0, 1]
      # )

      self.model = compat.convert_sklearn_to_river(
          estimator=BNB(binarize=.1),
          classes=[0, 1]
      )

      self.save_model()


  def suggest(self, wuzzle, candies, menu_size=3) -> List[int]:
    """Return a suggestion."""


    if WORLD["menu_size"] > len(wuzzle.potential_candy_ids):
      menu_size = len(wuzzle.potential_candy_ids)
    else:
      menu_size = WORLD["menu_size"]

    suggestions = []

    for candy in candies:
      if candy.uuid in wuzzle.potential_candy_ids:
        features = wuzzle.get_features(candy, include_hunger=False)

        if self.predict(features) == 1: suggestions.append(candy.uuid)

    if len(suggestions) > menu_size:
      return random.choices(suggestions, k=menu_size)

    menu_diff = menu_size - len(suggestions)
    menu_random = random.choices(wuzzle.potential_candy_ids, k=menu_diff)
    suggestions.extend(menu_random)

    # Learning loop
    for predicted_candy in suggestions:
      for candy in candies:
        if candy.uuid == predicted_candy:
          wuzzle.consider_candy(candy, self, train=True)

    return suggestions


  def train_one(self, X, y):
    y_pred = self.model.predict_one(X)
    self.accuracy = self.accuracy.update(y, y_pred)
    self.model.learn_one(x=X, y=y)
    self.accuracy_metric_float = self.accuracy.get()
    self.trainings += 1


  def save_model(self):
    dump(self.model, self.file_path)


  def predict(self, X):
    return self.model.predict_one(X)
