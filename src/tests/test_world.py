""" Testing the World environment as a whole.. Wuzzlopolis """
import numpy as np


def test_world_init(RandomWorld):
  assert isinstance(RandomWorld.initial_wuzzle_population, int)
  assert isinstance(RandomWorld.initial_candy_population, int)
  assert isinstance(RandomWorld.hunger_rate, float)
  assert len(RandomWorld.wuzzles) > 0
  assert len(RandomWorld.candies) > 0
  assert RandomWorld.machine


def test_world_text_report(RandomWorld):
  assert isinstance(RandomWorld.text_report(), str)