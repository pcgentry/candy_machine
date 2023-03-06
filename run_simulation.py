  #!./bin/python

from src.world import World

nights = 100
Wuzzlopolis = World()

print(Wuzzlopolis.text_report())
print(Wuzzlopolis.population_status())

for i in range(nights):
  Wuzzlopolis.night()
  print(f"Day: {i}")
  print(Wuzzlopolis.population_status())
  if Wuzzlopolis.wuzzle_population == 0:
    break