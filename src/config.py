"""Candy machine configuration."""
import uuid

import faker
from faker import Faker
import numpy as np

FAKER = Faker()

WORLD = {
  "cookbook_num_pages": 2,
  "cookbook_page_length": 3,
  "flavors": np.array(['apple', 'toenail', 'earwax', 'green tea', 'peach', 'tarball', 'toe fuzz']),
  "hunger_death": .75,
  "hunger_rate": .2,
  "initial_candy_population": 20,
  "initial_wuzzle_population": 20,
  "menu_size": 3,
}
