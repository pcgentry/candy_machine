from src.candy import Candy
from src.wuzzle import Wuzzle
from src.machine import Machine
from src.config import WORLD


class World():
  ''' The World object is what contains all the other things in Wuzzlopolis. Wuzzles, Candies, Candy Machines... etc.  This is where days become nights, 
  and history gets written.
  '''

  def __init__(self) -> None:
    self.config = WORLD
    self.initial_wuzzle_population = self.config["initial_wuzzle_population"]
    self.initial_candy_population =  self.config["initial_candy_population"]
    self.nights = 0


    self.hunger_rate = float(self.config["hunger_rate"])
    self.machine = Machine()
    self.generate_wuzzles()
    self.generate_candies()

    for wuzzle in self.wuzzles:
      wuzzle.find_candies(self.candies)
      wuzzle.generate_cookbooks()


  def night(self):
    ''' a day has passed, update hunger '''

    for candy in self.candies:
      candy.hunger += self.hunger_rate
      if candy.hunger >= self.config['hunger_death']:
        candy.life = 0
    
    for wuzzle in self.wuzzles:
      wuzzle.hunger += self.hunger_rate
      if wuzzle.hunger >= self.config['hunger_death']:
        wuzzle.life = 0
    
    self.nights += 1


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
    World Flavors: {self.config["flavors"]}
    """)

  def population_status(self) -> dict:
    status = {}

    status["population_wuzzle"] = 0
    status["dead_wuzzle"] = 0
    status["live_wuzzle"] = 0
    status["total_hunger_wuzzle"] = 0

    for wuzzle in self.wuzzles:
      status["population_wuzzle"] += 1
      if wuzzle.life == 1:
        status["live_wuzzle"] += 1
        status["total_hunger_wuzzle"] += wuzzle.hunger

    status["dead_wuzzle"] = status["population_wuzzle"] - status["live_wuzzle"]




    status["population_candy"] = 0
    status["dead_candy"] = 0
    status["live_candy"] = 0
    status["total_hunger_candy"] = 0

    for candy in self.candies:
      status["population_candy"] += 1
      if candy.life == 1:
        status["live_candy"] += 1
        status["total_hunger_candy"] += candy.hunger

    status["dead_candy"] = status["population_candy"] - status["live_candy"]

    return(status)