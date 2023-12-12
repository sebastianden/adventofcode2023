# Answer: 803

import numpy as np

# Read input txt as np array (and flip it to extraoplate left)
data = np.flip(np.loadtxt('input.txt', dtype=int), axis=1)
print(data)

last_values = []
for sample in data:
    der = sample
    while der.any():
        last_values.append(der[-1])
        der = np.diff(der)
print(sum(last_values))
