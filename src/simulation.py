"""The Simulation class."""
from src.world import World


class Simulation():
    """Contains and operates on the world.

    Has to be passed a machine object so that we can share a single Machine across sims."""
    
    def __init__(self, machine_object, max_nights=1000):
        Wuzzlopolis = World(machine_object=machine_object)

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
