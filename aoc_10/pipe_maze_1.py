# Answer: 6815

import numpy as np


def calculate_next(last, current, symbol):
    # Last = (x, y) of the field we came from
    # Current = (x, y) of the field of the symbol we're on
    x = current[1]
    y = current[0]

    # If we came from the left:
    if last[1] < current[1]:
        if symbol == '-':
            x += 1
        elif symbol == '7':
            y += 1
        elif symbol == 'J':
            y -= 1
    # If we came from the right:
    elif last[1] > current[1]:
        if symbol == '-':
            x -= 1
        elif symbol == 'F':
            y += 1
        elif symbol == 'L':
            y -= 1
    # If we came from the up:
    elif last[0] < current[0]:
        if symbol == '|':
            y += 1
        elif symbol == 'J':
            x -= 1
        elif symbol == 'L':
            x += 1
    # If we came from the down:
    elif last[0] > current[0]:
        if symbol == '|':
            y -= 1
        elif symbol == '7':
            x -= 1
        elif symbol == 'F':
            x += 1
    else:
        print('Something went wrong!')

    return (y, x)


def traverse_maze(start, next_step):
    last = start
    current = next_step
    symbol = 'S'

    count = 0
    count_matrix = np.zeros(maze.shape)

    while symbol != 'S' or count == 0:

        # Update the count matrix
        count_matrix[last] = count

        # Get the symbol of the current field
        symbol = maze[current]

        # Calculate the next step
        next = calculate_next(last, current, symbol)

        # Update last and current
        last = current
        current = next

        print(last, current, symbol)

        count += 1

    return count_matrix


if __name__ == '__main__':
    # Read input
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    maze = np.array([list(line) for line in data])
    start = np.where(maze == 'S')

    # 1. Start by going right
    first_count = traverse_maze((start[0][0], start[1][0]), (start[0][0], start[1][0] - 1))
    # 2. Start by going down
    second_count = traverse_maze((start[0][0], start[1][0]), (start[0][0] + 1, start[1][0]))

    print(np.max(np.minimum(first_count, second_count)))


# Go through the maze in both directions (there can only be two)
# How to walk through maze:
# 1. Start at "S"
# 2. Find a valid next step (we only have to check up/down/left/right, and not the one we're coming from)
# 3. Based on the symbol there calculate the next step, in a matrix put in the number of steps it took to get there
# 4. Repeat 3. until we reach "S" again
# 5. Do the same in the other direction, in another matrix put in the number of steps it took to get there

# Overlay the two matrices and keep the minimum value in each location
# Take the maximum value of the resulting matrix
