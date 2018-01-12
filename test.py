import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])
plt.ion()

for i in range(20):
    y = np.random.random()
    plt.plot(y, i)
    plt.pause(0.5)

