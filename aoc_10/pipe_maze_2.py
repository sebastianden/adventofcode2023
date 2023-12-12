# Answer: 269

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

        count += 1

    return count_matrix


if __name__ == '__main__':
    # Read input
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    maze = np.array([list(line) for line in data])
    print(maze)
    start = np.where(maze == 'S')

    count_matrix = traverse_maze((start[0][0], start[1][0]), (start[0][0], start[1][0] - 1))
    max_count = np.max(count_matrix)
    print(count_matrix)

    cross_counter = 0
    in_counter = 0
    in_matrix = np.zeros(count_matrix.shape)
    # Go over the matrix from left to right
    for y in range(count_matrix.shape[0]-1):
        for x in range(count_matrix.shape[1]):
            print(x, y)
            # If cell is on path and the cell below is also on the path (account for start)
            if ((count_matrix[y, x] != 0 or maze[y, x] == 'S') and count_matrix[y+1, x] != 0):
                # If the count of the current field is exactly 1 larger than the one below it we are in the loop and increase the cross counter
                if (count_matrix[y+1, x] - count_matrix[y, x] == -1) or (count_matrix[y, x] == 0 and count_matrix[y+1, x] == max_count):
                    cross_counter += 1
                    print('cross counter increased')
                # If the count of the current field is exactly 1 smaller than the one below it we are out of the loop and decrease the in counter
                elif (count_matrix[y+1, x] - count_matrix[y, x] == 1) or (count_matrix[y, x] == max_count and count_matrix[y+1, x] == 0):
                    cross_counter -= 1
                    print('cross counter decreased')
                # if the current field is not part of the pipeline and the cross counter is not null we found a field enclosed by the loop
            if (count_matrix[y, x] == 0 and maze[y, x] != 'S') and cross_counter != 0:
                in_counter += 1
                in_matrix[y, x] = 1
    print(in_counter)
    print(in_matrix)

    # Save in matrix to file
    np.savetxt('in_matrix.txt', in_matrix, fmt='%i')
