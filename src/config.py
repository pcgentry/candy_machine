"""Candy machine configuration."""
from faker import Faker
import numpy as np

FAKER = Faker()

WORLD = {
  "flavors": np.array(['apple', 'toenail', 'earwax']),
  "wuzzle_hunger_death": .75,
  "wuzzle_hunger_rate": .1,
  "candy_hunger_death": 75,
  "candy_hunger_rate": .001,
  "initial_candy_population": 20,
  "initial_wuzzle_population": 10,
  "menu_size": 3,
}
  # "flavors": np.array(['apple', 'toenail', 'earwax', 'green tea', 'peach', 'tarball', 'toe fuzz']),
