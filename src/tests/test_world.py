""" Testing the World environment as a whole.. Wuzzlopolis """
import numpy as np


def test_world_init(RandomWorld):
  assert isinstance(RandomWorld.initial_wuzzle_population, int)
  assert isinstance(RandomWorld.initial_candy_population, int)
