"""Candy machine configuration."""
from faker import Faker
import numpy as np

FAKER = Faker()

WORLD = {
  "flavors": np.array(['apple', 'toenail', 'earwax', 'green tea', 'peach', 'tarball', 'toe fuzz']),
  "hunger_death": .75,
  "hunger_rate": .2,
  "initial_candy_population": 20,
  "initial_wuzzle_population": 20,
  "menu_size": 3,
}
