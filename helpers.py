import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import pandas as pd
import numpy as np

from scipy.stats import norm
from src.simulation import Simulation

def run_strat(
    machine_object,
    description="Candy Machine", 
    num_simulations=5,
    image_prefix = "images/_",
    x_lims = (10, 30)
    ):

    print(type(machine_object))
    s = Simulation(machine_object=machine_object)
    simulations = []

    for i in range(num_simulations):
        simulations.append(Simulation(machine_object=machine_object))

    nights_df = pd.DataFrame(s.nightly_stats)
    # skull_chart(simulations, description, image_prefix)
    skull_hist(simulations, description, image_prefix, x_lims)

    return simulations, nights_df


def skull_hist(simulations, strategy_human, image_prefix, x_lims = (10, 30)):

    fig, ax1 = plt.subplots(1, 1, figsize=(20,5))

    max_nights = []

    for sim in simulations:
        nights_df = pd.DataFrame(sim.nightly_stats)
        max_nights.append(len(nights_df))

    max_nights = np.array(max_nights)

    global_nights_mean = max_nights.mean()
    global_nights_min = max_nights.min()
    global_nights_max = max_nights.max()


    plt.axvline(global_nights_mean, color="black", linewidth=1, alpha=1, label="Average day of Wuzzlpocalypse")
    plt.axvline(global_nights_mean, color="firebrick", linewidth=3, alpha=1)
    plt.axvline(global_nights_min, linestyle ="--", color="firebrick", linewidth=3, alpha=.5, label="Earliest Wuzzlpocalypse")
    plt.axvline(global_nights_max, linestyle ="--", color="firebrick", linewidth=3, alpha=.5, label="Latest Wuzzlpocalypse")
    plt.axvspan(global_nights_min, global_nights_max, alpha=0.2, color='firebrick')

    spread = max_nights.max() - max_nights.min()
    support = np.linspace(max_nights.min() - spread, max_nights.max() + spread, 500)

    ax1.hist(max_nights, color='red', bins=spread+1)
    ax1.set_title(f"Distribution of the LAST DAY - {strategy_human}")
    ax1.set_ylabel('Likelihood')
    ax1.set_xlabel('Days to Wuzzlpocalypse')
    ax1.set_xlim(x_lims)

    # skull_pixels = mpimg.imread('images/skull.jpeg')
    # imagebox = OffsetImage(skull_pixels, zoom=.25)
    # ab = AnnotationBbox(imagebox, (max_nights.mean(), 3))
    # ax1.add_artist(ab)

    plt.savefig(f"{ image_prefix }distribution_final_days.png");
    plt.show();
    



def skull_chart(simulations, strategy_human, image_prefix):

    fig, ax1 = plt.subplots(1, 1, figsize=(20,5))

    max_nights = []

    for sim in simulations:
        nights_df = pd.DataFrame(sim.nightly_stats)
        max_nights.append(len(nights_df))

    max_nights = np.array(max_nights)

    global_nights_mean = max_nights.mean()
    global_nights_min = max_nights.min()
    global_nights_max = max_nights.max()


    plt.axvline(global_nights_mean, color="black", linewidth=1, alpha=1, label="Average day of Wuzzlpocalypse")
    plt.axvline(global_nights_mean, color="firebrick", linewidth=3, alpha=1)
    plt.axvline(global_nights_min, linestyle ="--", color="firebrick", linewidth=3, alpha=.5, label="Earliest Wuzzlpocalypse")
    plt.axvline(global_nights_max, linestyle ="--", color="firebrick", linewidth=3, alpha=.5, label="Latest Wuzzlpocalypse")
    plt.axvspan(global_nights_min, global_nights_max, alpha=0.2, color='firebrick')

    dist = norm(loc=max_nights.mean(), scale=max_nights.std())

    spread = max_nights.max() - max_nights.min()
    support = np.linspace(max_nights.min() - spread, max_nights.max() + spread, 500)

    ax1.plot(support, dist.pdf(support), color='red')
    ax1.set_title(f"Distribution of the LAST DAY - {strategy_human}")
    ax1.set_ylabel('Likelihood')
    ax1.set_xlabel('Days to Wuzzlpocalypse')

    skull_pixels = mpimg.imread('images/skull.jpeg')
    imagebox = OffsetImage(skull_pixels, zoom=.25)
    ab = AnnotationBbox(imagebox, (max_nights.mean(), .2))
    ax1.add_artist(ab)

    plt.savefig(f"{ image_prefix }distribution_final_days.png");
    plt.show();
    