from src.world import World
from src.config import WORLD


class Simulation():

    def __init__(self, max_nights=1000):
        Wuzzlopolis = World()
        self.world_objects = Wuzzlopolis.objects_report()
        self.nightly_stats = []
        self.nightly_stats.append(Wuzzlopolis.population_status())

        for i in range(max_nights):
            Wuzzlopolis.night()
            w_snapshot = Wuzzlopolis.population_status()

            self.nightly_stats.append(w_snapshot)

            if Wuzzlopolis.wuzzle_population == 0:
                break

        self.simulation_length = len(self.nightly_stats)-1
