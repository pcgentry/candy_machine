"""Candy machine configuration."""
from faker import Faker
import numpy as np

FAKER = Faker()

WORLD = {
  "flavors": np.array(['apple', 'toenail', 'earwax', 'cheese']),
  "wuzzle_hunger_death": 75,
  "wuzzle_hunger_rate": 25,
  "candy_hunger_death": 100,
  "candy_hunger_rate": 1,
  "initial_candy_population": 50,
  "initial_wuzzle_population": 50,
  "menu_size": 3,
}
  # "flavors": np.array(['apple', 'toenail', 'earwax', 'green tea', 'peach', 'tarball', 'toe fuzz']),
