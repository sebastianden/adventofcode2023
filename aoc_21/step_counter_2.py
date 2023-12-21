# Answer:

import numpy as np

if __name__ == '__main__':
    with open('example_input.txt', 'r') as f:
        lines = f.read().splitlines()

    data = [list(line) for line in lines]

    # Find the starting point coordinates

    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == 'S':
                start = (row, col)
                break
    queue = [start]
    print(queue)

    max_steps = 64
    for n in range(max_steps):
        new_queue = []
        while queue:
            cur = queue.pop(0)
            # If left, right, up, down are not walls, or they are already in the
            # queue, add them to the queue
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new = (cur[0] + direction[0], cur[1] + direction[1])
                if data[new[0]][new[1]] != '#' and new not in new_queue:
                    new_queue.append(new)
        queue = new_queue
    print(queue)
    print(len(queue))

    # Replace the coordinates in the queue with "O"s in the data
    for coord in queue:
        data[coord[0]][coord[1]] = 'O'
    print(np.array(data))
