""" Testing Wuzzles. """
from random import Random
import pytest

from src.candy import Candy



def test_wuzzle_has_name(RandomWuzzle):
    assert RandomWuzzle.name, "Wuzzle has not named themself."

def test_wuzzle_init_flavor_preferences(RandomWuzzle):
    assert RandomWuzzle.flavor_preferences, "Wuzzle has no flavor preferences"
    assert isinstance(RandomWuzzle.flavor_preferences, dict), "Somethings wrong. Wuzzle flavor preferences are not a Dictionary"
    assert len(RandomWuzzle.flavor_preferences) > 0, "Wuzzle has zero flavor preferences"
    assert RandomWuzzle.uuid
    assert RandomWuzzle.hunger ==  0, "Wuzzle needs hunger"
    assert RandomWuzzle.life ==  1, "Wuzzle needs to be alive"
    # assert isinstance(RandomWuzzle.menu, list), "Wuzzles need to own a menu to be filled by the Candy Machine"

    for key, value in RandomWuzzle.flavor_preferences.items():

        assert isinstance(key, str), "The first part of a Wuzzle pref should be the flavor"
        assert isinstance(value, float), "The second part of a Wuzzle pref should be the likelihood git of licking"

def test_wuzzle_cookbook_init(RandomWuzzle):
    assert isinstance(RandomWuzzle.cookbooks, list)
    assert len(RandomWuzzle.cookbooks) == len(RandomWuzzle.flavor_preferences)

def test_wuzzle_find_candies(RandomWuzzle, CandySet):
    assert isinstance(RandomWuzzle.find_candies(CandySet), list)

def test_wuzzle_generate_cookbooks(RandomWuzzle, CandySet):
    Test_Wuz = RandomWuzzle
    Test_Wuz.find_candies(CandySet)
    Test_Wuz.generate_cookbooks()
    assert isinstance(Test_Wuz.cookbooks, list)

    Test_Wuz.populate_cookbooks(CandySet)
    assert isinstance(Test_Wuz.cookbooks[0].flavor, str)


def test_wuzzle_check_menu(RandomWuzzle, CandySet):
    test_wuzz = RandomWuzzle.check_menu(CandySet)
