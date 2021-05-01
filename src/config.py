import numpy as np
import uuid
import faker
from faker import Faker

FAKER = Faker()  ## Object constant? Is that a thing?

WORLD = {
  "flavors": np.array(['apple', 'toenail', 'earwax', 'green tea', 'peach', 'tarball', 'toe fuzz']),
  "cookbook_page_length": 3,
  "cookbook_num_pages": 2,
}

