import matplotlib.pyplot as plt
import numpy as np


def plot_signal(frames, seconds):
    frames = np.asarray(frames)
    timesteps = [1. * f / seconds for f in range(len(frames))]
    plt.fill_between(timesteps, frames, color='lightblue')
    plt.fill_between(timesteps, 0 - frames, color='lightblue')
    plt.show()
