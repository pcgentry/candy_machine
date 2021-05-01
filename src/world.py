from src.candy import Candy
from src.wuzzle import Wuzzle
from src.machine import Machine
from src.config import WORLD


class World():
  ''' The World object is what contains all the other things in Wuzzlopolis. Wuzzles, Candies, Candy Machines... etc.  This is where days become nights, 
  and history gets written.
  '''

  def __init__(self) -> None:
    self.initial_wuzzle_population = 10
    self.initial_candy_population = 10


    self.hunger_rate = .3
    self.machine = Machine()
    self.generate_wuzzles()
    self.generate_candies()

    for wuzzle in self.wuzzles:
      wuzzle.find_candies(self.candies)
      wuzzle.generate_cookbooks()


  def generate_wuzzles(self):
    ''' This is where we keep our Wuzzles '''

    self.wuzzles = []
    for i in range(self.initial_wuzzle_population):
      self.wuzzles.append(Wuzzle())


  def generate_candies(self):
    ''' This is where all the CANDY individuals live. '''

    self.candies = []
    for i in range(self.initial_candy_population):
      self.candies.append(Candy())

  def text_report(self):
    return (f""" 
    Wuzzles: {self.wuzzles}
    Candies: {self.candies}
    World Flavors: {WORLD["flavors"]}
    """)