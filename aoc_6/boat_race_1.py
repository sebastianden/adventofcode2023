# Answer:

from functools import reduce

with open('input.txt') as f:
    lines = f.read().splitlines()


times = [int(n) for n in lines[0].split(' ')[1:] if n != '']
distances = [int(n) for n in lines[1].split(' ')[1:] if n != '']
races = [i for i in zip(times, distances)]


margin_list = []

for i, race in enumerate(races):
    count = 0
    for t_h in range(race[0]):
        d = t_h * (race[0] - t_h)
        if d > race[1]:
            count += 1

    margin_list.append(count)

# Multiply all the margins together
print(reduce(lambda x, y: x * y, margin_list))
