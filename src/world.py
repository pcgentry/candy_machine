from src.flavors import Flavors
from src.candy import Candy
from src.wuzzle import Wuzzle
from src.machine import Machine


class World():
  ''' The World object is what contains all the other things in Wuzzlopolis. Wuzzles, Candies, Candy Machines... etc.  This is where days become nights, 
  and history gets written.
  '''

  def __init__(self) -> None:
    self.initial_wuzzle_population = 10
    self.initial_candy_population = 10
    self.hunger_rate = .3
    self.generate_wuzzles()
    self.generate_candies()


  def generate_wuzzles(self):
    ''' This is where we keep our Wuzzles '''

    self.wuzzles = []
    for i in range(self.initial_wuzzle_population):
      self.wuzzles.append(Wuzzle())


  def generate_candies(self):
    ''' This is where all the CANDY individuals live. '''

    self.candies = []
    for i in range(self.initial_candy_population):
      self.candies.append(Candy)
