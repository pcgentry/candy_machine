from os import path
import random

from joblib import dump, load
from river import compose, tree, metrics, preprocessing

from src.config import WORLD



class DecisionTree():

  def __init__(self) -> None:
    ''' Create a persistent model file if there isn't one. If one exists, use it. '''

    self.file_path = 'models/decision_tree.joblib'

    if path.exists(self.file_path):
      self.model = load(self.file_path)
    else:
      self.model = tree.HoeffdingTreeClassifier(grace_period=50)
      self.save_model()


  def suggest(self, wuzzle, menu_size=3) -> list:
    ''' Use this model to make suggestions '''

    if WORLD["menu_size"] > len(wuzzle.potential_candy_ids):
      menu_size = len(wuzzle.potential_candy_ids)
    else:
      menu_size = WORLD["menu_size"]

    return random.choices(wuzzle.potential_candy_ids, k=menu_size)

  def train_one(self, X=[], y=[]):
    self.model.learn_one(X, y)

  
  def save_model(self):
    dump(self.model, self.file_path)
