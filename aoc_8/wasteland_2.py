# Answer: 13129439557681
from functools import reduce
from math import lcm

with open('input.txt') as f:
    lines = f.read().splitlines()

instructions = list(lines[0])

nodes = {line.split('=')[0].strip(): tuple(line.split('=')[1].strip(" ()").split(", ")) for line in lines[2:]}

left_right = {'L': 0, 'R': 1}

next_nodes = [n for n in nodes if n.endswith('A')]  # List of nodes ending with Z
start_nodes = next_nodes.copy()
count_to_z = [0] * len(next_nodes)
counter = 0

# while not next_nodes == start_nodes or sum(count_to_z) == 0:
while not all([n.endswith('Z') for n in next_nodes]):
    for i, node in enumerate(next_nodes):
        # if node == start_nodes[i] and count_to_z[i] != 0:
        if node.endswith('Z'):
            pass
        else:
            next_nodes[i] = nodes[node][left_right[instructions[counter]]]
            count_to_z[i] += 1

    counter += 1
    if counter == len(instructions):
        counter = 0

print(count_to_z)
# Least Common Multiple of all the counts
print(lcm(*count_to_z))
