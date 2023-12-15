# Answer: 288521
from collections import defaultdict


def hash(inp):
    val = 0
    for c in inp:
        val += ord(c)
        val *= 17
        val %= 256
    return val


def find(lense_list, label):
    for i, lense in enumerate(lense_list):
        if lense[0] == label:
            return i
    return None


def focusing_power(box_map):
    power = 0
    for box_nr, lenses in box_map.items():
        for slot_nr, lense in enumerate(lenses):
            power += ((box_nr + 1) * (slot_nr + 1) * int(lense[1]))
    return power


if __name__ == '__main__':
    # Read in the first line of the input file
    with open('input.txt', 'r') as f:
        line = f.readline().strip()

    data = [step for step in line.split(',')]

    box_map = defaultdict(list)

    for step in data:

        if "-" in step:
            label = step[:-1]
            box = hash(label)
            # Remove the label from the box
            i = find(box_map[box], label)
            if i is not None:
                box_map[box].pop(i)

        if "=" in step:
            label, focal_len = step.split('=')
            box = hash(label)
            i = find(box_map[box], label)
            if i is not None:
                box_map[box][i] = (label, focal_len)
            else:
                box_map[box].append((label, focal_len))

    print(focusing_power(box_map))
