import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
from statistics import stdev
from scipy.stats import norm

if os.name == 'posix':
    matplotlib.use('TkAgg')

rng = np.random.default_rng()  # random number generator


# Generates and plots data for coin flip trials
def generate_coin_histogram(big_n=1000, little_n=10):
    data = []
    for i in range(0, big_n):
        total = 0
        rolls = rng.integers(low=0, high=2, size=little_n)
        for j in rolls:
            total += j
        data.append(total)
    plt.hist(data, bins=range(0, little_n + 1), align='left', density=True, color='lightblue', edgecolor='black')
    x_axis = np.arange(0, little_n + 1, .01)
    mean1 = mean(data)
    sd = stdev(data)
    plt.plot(x_axis, norm.pdf(x_axis, mean1, sd))
    plt.xlabel('Successes')
    plt.ylabel('PDF')
    plt.title('Coin Flip histogram with N = ' + str(big_n) + ' and n = ' + str(little_n))
    plt.show()
    return


# Generates and plots data for dice roll trials
def generate_dice_histogram(big_n=1000, little_n=10):
    data = []
    for i in range(0, big_n):
        total = 0
        rolls = rng.integers(low=1, high=7, size=little_n)
        for j in rolls:
            total += j
        data.append(total)
    plt.hist(data, bins=range(little_n, little_n * 6 + 1), density=True, align='left', color='lightblue',
             edgecolor='black')
    x_axis = np.arange(little_n, little_n * 6, .01)
    mean1 = mean(data)
    sd = stdev(data)
    plt.plot(x_axis, norm.pdf(x_axis, mean1, sd))
    plt.xlabel('Successes')
    plt.ylabel('PDF')
    plt.title('Dice Roll histogram with N = ' + str(big_n) + ' and n = ' + str(little_n))
    plt.show()
    return


def mean(lst):
    total = 0.0
    ct = 0
    for x in lst:
        total += x
        ct += 1
    return total / ct


#  main script
for n in [10, 20, 40, 80]:
    generate_coin_histogram(little_n=n)
    generate_dice_histogram(little_n=n)
