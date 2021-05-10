from os import path
import random

from joblib import dump, load
from river import compose, linear_model, metrics, preprocessing

from src.config import WORLD



class LogisticRegression():

  def __init__(self) -> None:
    ''' Create a persistent model file if there isn't one. If one exists, use it. '''

    self.file_path = 'models/logistic_regression.joblib'

    if path.exists(self.file_path):
      self.model = load(self.file_path)
    else:
      self.model = compose.Pipeline(
          preprocessing.StandardScaler(),
          linear_model.LogisticRegression()
      )
      self.save_model()


  def suggest(wuzzle, menu_size=3) -> list:
    ''' this implements the random strategy. In theory it should perform badly as it will not be able to tell which candies the wuzzle likes more '''

    if WORLD["menu_size"] > len(wuzzle.potential_candy_ids):
      menu_size = len(wuzzle.potential_candy_ids)
    else:
      menu_size = WORLD["menu_size"]

    return random.choices(wuzzle.potential_candy_ids, k=menu_size)

  def save_model(self):
    dump(model, self.file_path)
