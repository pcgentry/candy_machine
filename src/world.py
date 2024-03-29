"""The World Class."""
from src.candy import Candy
from src.config import WORLD
from src.wuzzle import Wuzzle

def list_to_strings(my_list):
    return [str(x) for x in my_list]

class World():
  ''' The World object is what contains all the other things in Wuzzlopolis. Wuzzles, Candies, Candy Machines... etc.  This is where days become nights, 
  and history gets written.
  '''

  def __init__(self, machine_object) -> None:
    self.config = WORLD
    self.initial_wuzzle_population = self.config["initial_wuzzle_population"]
    self.initial_candy_population =  self.config["initial_candy_population"]
    self.nights = 0
    self.lick_counter = 0
    self.nightly_lick_counter = 0

    # self.reward = 10
    # self.punishment = -100

    self.machine = machine_object

    self.wuzzle_hunger_rate = float(self.config["wuzzle_hunger_rate"])
    self.candy_hunger_rate = float(self.config["candy_hunger_rate"])
    self.generate_wuzzles()
    self.generate_candies()

    for wuzzle in self.wuzzles:
      wuzzle.find_candies(self.candies)
      wuzzle.generate_cookbooks()


  def wuzzles_eat_dinner(self):
    for wuzzle in self.wuzzles:
      if wuzzle.life == 1:
        wuzzle.find_candies(self.candies)

        self.machine.recommend_for_wuzzle(wuzzle, self.candies, self.config["menu_size"])

        wuzzle.check_menu(self.candies, self.machine)
        if wuzzle.nightly_lick_counter > 0:
          self.lick_counter += wuzzle.nightly_lick_counter
          self.nightly_lick_counter += wuzzle.nightly_lick_counter
          
    self.machine.save_model()


  def night(self):
    ''' a day has passed, lick, and update hunger '''
    self.nightly_lick_counter = 0

    self.wuzzles_eat_dinner()

    for candy in self.candies:
      candy.hunger += self.candy_hunger_rate
      if candy.hunger >= self.config['candy_hunger_death']:
        candy.life = 0
    
    for wuzzle in self.wuzzles:
      wuzzle.hunger += self.wuzzle_hunger_rate
      if wuzzle.hunger >= self.config['wuzzle_hunger_death']:
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

  def objects_report(self):

    w_report = {}
    w_list = []
    c_list = []
    f_list = list_to_strings(self.config["flavors"])

    for wuzzle in self.wuzzles:
      w_list.append(wuzzle.to_dict())

    for candy in self.candies:
      c_list.append(candy.to_dict())

    w_report["wuzzles"] = w_list
    w_report["candies"] = c_list
    w_report["flavors"] = f_list

    return w_report

  def population_status(self) -> dict:
    status = {}

    status["nightly_lick_counter"] = self.nightly_lick_counter
    status["lick_counter"] = self.lick_counter

    status["population_wuzzle"] = 0
    status["dead_wuzzle"] = 0
    status["live_wuzzle"] = 0
    status["total_hunger_wuzzle"] = 0

    for wuzzle in self.wuzzles:
      status["population_wuzzle"] += 1
      if wuzzle.life == 1:
        status["live_wuzzle"] += 1
        status["total_hunger_wuzzle"] += wuzzle.hunger

    self.wuzzle_population = status["live_wuzzle"]
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

    status["machine_accuracy"] = self.machine.report_accuracy()

    return(status)
