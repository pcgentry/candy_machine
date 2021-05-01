""" Testing Candy Cookbooks. In the grand scheme, a coobook represents a queue for each wuzzle output by a model. It contains a list of Candy matches
that later are used by the Candy Machine to fill the Wuzzle's Menu """
import numpy as np


def test_cookbook(TestCookbook):
  assert isinstance(TestCookbook.model_type, str)
  assert isinstance(TestCookbook.flavor, str)
