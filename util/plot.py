import matplotlib.pyplot as plt


def plot_signal(frames, seconds):
    timesteps = [1. * f / seconds for f in range(len(frames))]
    plt.plot(timesteps, frames)
    plt.show()
