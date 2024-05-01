import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics
matplotlib.use('TkAgg')  # remove or change based on your system

x_axis = np.arange(-20, 20, 0.01)
mean = statistics.mean(x_axis)
sd = statistics.stdev(x_axis)
plt.plot(x_axis, norm.pdf(x_axis, mean, sd))

plt.show()