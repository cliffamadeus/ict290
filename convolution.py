import numpy as np

x = np.array([])
h = np.array([])
y = np.convolve(x, h, mode='full')

print(y)
