# Answer: 597102953699891

import numpy as np
from tqdm import tqdm

# Size of the input 131 x 131
# Steps 26501365
# 26501365 / 131 = 202300 with a remainder of 65 (half the size of the input)


def get_points(data):
    # Extend the grid by 2 grids to each side
    data = np.tile(data, (5, 5))
    start = (len(data)//2, len(data)//2)

    queue = set()
    queue.add(start)

    points = []

    max_steps = 65 + 131 * 2
    for n in tqdm(range(max_steps)):
        new_queue = set()
        for cur in queue:
            # If left, right, up, down are not walls, or they are already in the
            # queue, add them to the queue
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new = (cur[0] + direction[0], cur[1] + direction[1])
                if data[new[0]][new[1]] != '#':
                    new_queue.add(new)
        queue = new_queue
        if n in [64, 64 + 131, 64 + 131 * 2]:
            points.append((n + 1, len(queue)))
    return points


def f(n):
    return (14590 * n**2)/17161 + (28214 * n)/17161 - 135409/17161


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()

    data = np.array([list(line) for line in lines])

    points = get_points(data)
    print(points)

    # Quadratic equation with 3 unknows -> calculate 3 points
    # f(x) = ax^2 + bx + c
    # f(65) = 3691
    # f(65 + 131) = 32975
    # f(65 + 131 * 2) = 91439
    # f(26501365) = ???
    # Result of solving the equation:
    # (14590 x^2)/17161 + (28214 x)/17161 - 135409/17161≈0.850184 x^2 + 1.64408 x - 7.89051
    # (data is perfectly fit by a 2nd degree polynomial)
    print(f(65))
    print(f(65 + 131))
    print(f(65 + 131 * 2))
    print(f(26501365))
