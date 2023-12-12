# Answer: 1681758908

import numpy as np

# Read input txt as np array
data = np.loadtxt('input.txt', dtype=int)

last_values = []
for sample in data:
    print(sample)
    der = sample
    while der.any():
        last_values.append(der[-1])
        der = np.diff(der)
    print(sum(last_values))
    # last_values = []
