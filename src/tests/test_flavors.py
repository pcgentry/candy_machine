""" Testing Flavors. In Wuzzlopolis, we access flavors a lot """
import numpy as np


def test_flavors_exist(RandomFlavors):
  assert isinstance(RandomFlavors.flavors, np.ndarray)
  assert len(RandomFlavors.flavors) > 0


def test_flavors_make_flavors(RandomFlavors):
    # assert RandomFlavors.make_flavors()
  assert isinstance(RandomFlavors.make_flavors(1), dict)
  assert len(RandomFlavors.make_flavors()) > 0

  for key, value in RandomFlavors.make_flavors(4).items():
      assert isinstance(key, str), "The first part of a flavor should be the flavor"
      assert isinstance(value, float), "The second part of a flavor should be a random number"

