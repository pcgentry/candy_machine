""" Testing Candy """
import pytest

def test_candy_has_name(RandomCandy):
    assert RandomCandy.name, "CANDY has not named themself."


def test_candy_init(RandomCandy):
    assert RandomCandy.flavors, "Candy has no flavor."
    assert RandomCandy.uuid 
    assert isinstance(RandomCandy.flavors, dict), "Somethings wrong. CANDY flavor preferences are not a Dictionary"
    assert len(RandomCandy.flavors) > 0, "CANDY has zero flavor."

    for key, value in RandomCandy.flavors.items():

        assert isinstance(key, str), "The first part of a CANDY flavor should be the flavor"
        assert isinstance(value, float), "The second part of a CANDY flavor should be the likelihood of eating"