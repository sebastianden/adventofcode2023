# Answer: 6658

max_steps = 0


def walk(steps, current_position, already_visited):

    possible_next_steps = [current_position]
    # From current position look left, right, up, down
    while len(possible_next_steps) == 1:
        current_position = possible_next_steps.pop()
        # print(current_position)
        steps += 1
        already_visited.add(current_position)
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # print(direction)
            next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
            # print(next_position)
            if next_position == goal:
                # print(steps, end=', ')
                global max_steps
                if steps > max_steps:
                    max_steps = steps
                    print(max_steps)
                return
            # If in grid and not a wall
            if next_position[0] > 0 and next_position[1] > 0 and next_position[0] < len(data) and next_position[1] < len(data[0]):
                next_tile = data[next_position[0]][next_position[1]]
                # print(next_tile)
                if next_position not in already_visited and next_tile != '#':
                    # print(next_position)
                    possible_next_steps.append(next_position)

    # If no possible next steps, return steps
    # if len(possible_next_steps) == 0:
        # print("Not a valid path")
    # If multiple possible next steps, go all of them
    if len(possible_next_steps) > 1:
        # print("Multiple possible next steps", possible_next_steps)
        for next_step in possible_next_steps:
            new_set = already_visited.copy()
            walk(steps, next_step, new_set)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    data = [list(line) for line in data]

    already_visited = set()
    current_position = (0, 1)
    goal = (len(data)-1, len(data[0])-2)

    walk(0, current_position, already_visited)

    print(max_steps)

    # Too low 6274, 6294, 6398
