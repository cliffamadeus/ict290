import numpy as np

x = np.array([-2,-1,0,1,2,3,4])
h = np.array([])
y = np.convolve(x, h, mode='full')

print(y)
