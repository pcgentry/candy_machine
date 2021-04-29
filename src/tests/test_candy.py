""" Testing Candy """
import pytest

def test_candy_has_name(RandomCandy):
    assert RandomCandy.name, "CANDY has not named themself."