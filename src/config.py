import numpy as np
import uuid
import faker
from faker import Faker

FAKER = Faker()

WORLD = {
  "flavors": np.array(['apple', 'toenail', 'earwax', 'green tea', 'peach', 'tarball', 'toe fuzz']),
  "cookbook_page_length": 3,
  "cookbook_num_pages": 2,
  "menu_size": 3,
  "initial_wuzzle_population": 40,
  "initial_candy_population": 40,
  "hunger_rate": .2,
  "hunger_death": .75,
}

