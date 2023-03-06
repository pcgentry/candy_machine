  #!./bin/python

import pandas as pd
import numpy as np
import os
import json
from datetime import datetime
import matplotlib.pyplot as plt


plt.style.use('seaborn-bright')

from scipy.stats import norm, skewnorm, skew
from src.simulation import Simulation
from src.machine import Machine

from helpers import run_strat

num_simulations=1

def create_output_folder(parent_dir="./"):
    # Create the simulation_outputs folder if it doesn't exist
    outputs_dir = os.path.join(parent_dir, "simulation_outputs")
    if not os.path.exists(outputs_dir):
        os.makedirs(outputs_dir)

    # Get the current date and time
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

    # Create a new folder with the current date and time as the name
    folder_name = os.path.join(outputs_dir, f"{date_time}")
    os.makedirs(folder_name)

    # Return the path to the new folder
    return os.path.abspath(folder_name)

new_folder = create_output_folder()
print(f"New output folder created: {new_folder}")

machine_object = Machine()
simulations, nights_df_arr = run_strat(machine_object=machine_object, num_simulations=num_simulations, x_lims = (15, 25))

print(f"Model trainings: {machine_object.model.trainings}")
print(f"Model saves: {machine_object.saves}")
print(f"Accuracy: {machine_object.report_accuracy()}")


# Initialize a counter to keep track of the simulation number
sim_counter = 1

# Loop over each simulation in the list of simulations
for sim in simulations:

    # Print a message to indicate that we are writing the simulation data
    print(f"Writing Simulation Data for Simulation {sim_counter}:")

    # Write the nightly summary data to a JSON file
    nightly_summary_filename = f"nightly-summary-{sim_counter}.json"
    nightly_summary_filepath = os.path.join(new_folder, nightly_summary_filename)
    print(f" ... Writing nightly summary to file: {nightly_summary_filename}")
    with open(nightly_summary_filepath, 'w') as f:
        json.dump(sim.nightly_stats, f)

    # Write the simulation objects data to a JSON file
    simulation_objects_filename = f"simulation-objects-{sim_counter}.json"
    simulation_objects_filepath = os.path.join(new_folder, simulation_objects_filename)
    print(f" ... Writing objects to file: {simulation_objects_filename}\n")
    with open(simulation_objects_filepath, 'w') as f:
        json.dump(sim.world_objects, f)

    # Increment the simulation counter
    sim_counter += 1
