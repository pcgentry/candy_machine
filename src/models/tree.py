from os import path
import random

from joblib import dump, load
from river import compose, tree, metrics, preprocessing

from src.config import WORLD



class DecisionTree():

  def __init__(self) -> None:
    ''' Create a persistent model file if there isn't one. If one exists, use it. '''

    self.file_path = 'models/decision_tree.joblib'
    self.include_hunger = False
    self.accuracy_metric_float = 0.0
    self.accuracy = metrics.Accuracy()


    if path.exists(self.file_path):
      self.model = load(self.file_path)
    else:
      self.model = tree.HoeffdingTreeClassifier()
      self.save_model()


  def suggest(self, wuzzle, candies, menu_size=3) -> list:
    ''' Use this model to make suggestions '''

    if WORLD["menu_size"] > len(wuzzle.potential_candy_ids):
      menu_size = len(wuzzle.potential_candy_ids)
    else:
      menu_size = WORLD["menu_size"]
    # return random.choices(wuzzle.potential_candy_ids, k=menu_size)
    suggestions = []

    for candy in candies:
      if candy.uuid in wuzzle.potential_candy_ids:
        features = wuzzle.get_features(candy, include_hunger=False)
        if self.predict(features) == 1:
          suggestions.append(candy.uuid)

    if len(suggestions) > menu_size:
      return random.choices(suggestions, k=menu_size)
    else:
      menu_diff = menu_size - len(suggestions)
      menu_random = random.choices(wuzzle.potential_candy_ids, k=menu_diff)
      suggestions.extend(menu_random)

    return suggestions

  def train_one(self, X=[], y=[]):
    y_pred = self.model.predict_one(X)      # make a prediction
    self.accuracy = self.accuracy.update(y, y_pred)  # update the metric
    self.model.learn_one(X, y)

    self.accuracy_metric_float = self.accuracy.get()

  
  def save_model(self):
    dump(self.model, self.file_path)


  def predict(self, X):
    return self.model.predict_one(X)

