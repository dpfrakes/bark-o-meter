import matplotlib.pyplot as plt
import numpy as np
import os


def plot_signal(frames, seconds, occasion):
    frames = np.asarray(frames)
    timesteps = [1. * f / seconds for f in range(len(frames))]
    plt.fill_between(timesteps, frames, color='lightblue')
    plt.fill_between(timesteps, 0 - frames, color='lightblue')

    # Create output directory if none found
    if not os.path.exists("output"):
        os.mkdir("output")

    plt.savefig(os.path.join('output', 'output_{}.png'.format(occasion)))
    plt.show()
