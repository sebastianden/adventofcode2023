# Answer: 38017587

from functools import reduce

with open('input.txt') as f:
    lines = f.read().splitlines()

time = int(''.join([n for n in lines[0].split(' ')[1:] if n != '']))
distance = int(''.join([n for n in lines[1].split(' ')[1:] if n != '']))


margin_list = []

count = 0
for t_h in range(time):
    d = t_h * (time - t_h)
    if d > distance:
        count += 1

margin_list.append(count)

# Multiply all the margins together
print(reduce(lambda x, y: x * y, margin_list))
