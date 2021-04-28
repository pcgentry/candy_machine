from faker import Faker

class Wuzzle():
    '''
    Creates a wuzzle critter to eat CANDY.
    '''
    def __init__(self):
      fake = Faker()
      self.name = fake.name()
