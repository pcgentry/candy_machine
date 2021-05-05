#!./bin/python

from src.world import World

nights = 5
Wuzzlopolis = World()

print(Wuzzlopolis.text_report())
print(Wuzzlopolis.population_status())

for i in range(nights):
  Wuzzlopolis.night()
  print(Wuzzlopolis.population_status())