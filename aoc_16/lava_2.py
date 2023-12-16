# Answer: 7154

def energize(start_beam, data):
    energized = set()
    visited = set()
    beams = [start_beam]
    while beams:
        beam = beams.pop(0)
        coords = beam[0]
        row = coords[0]
        col = coords[1]
        direction = beam[1]

        if direction == "R":
            col += 1
        elif direction == "L":
            col -= 1
        elif direction == "U":
            row -= 1
        elif direction == "D":
            row += 1

        if 0 <= row < len(data) and 0 <= col < len(data[0]) and ((row, col), direction) not in visited:

            tile = data[row][col]

            visited.add(((row, col), direction))
            energized.add((row, col))

            if tile == ".":
                beams.append(((row, col), direction))
            elif tile == "/":
                if direction == "R":
                    beams.append(((row, col), "U"))
                elif direction == "L":
                    beams.append(((row, col), "D"))
                elif direction == "U":
                    beams.append(((row, col), "R"))
                elif direction == "D":
                    beams.append(((row, col), "L"))
            elif tile == "\\":
                if direction == "R":
                    beams.append(((row, col), "D"))
                elif direction == "L":
                    beams.append(((row, col), "U"))
                elif direction == "U":
                    beams.append(((row, col), "L"))
                elif direction == "D":
                    beams.append(((row, col), "R"))
            elif tile == "|":
                if direction == "U" or direction == "D":
                    beams.append(((row, col), direction))
                elif direction == "R" or direction == "L":
                    beams.append(((row, col), "U"))
                    beams.append(((row, col), "D"))
            elif tile == "-":
                if direction == "R" or direction == "L":
                    beams.append(((row, col), direction))
                elif direction == "U" or direction == "D":
                    beams.append(((row, col), "R"))
                    beams.append(((row, col), "L"))

    return len(energized)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    data = [list(line) for line in lines]

    energy = []

    for row in range(len(data)):
        energy.append(energize(((row, -1), "R"), data))
        energy.append(energize(((row, len(data[0])), "L"), data))
    for col in range(len(data[0])):
        energy.append(energize(((-1, col), "D"), data))
        energy.append(energize(((len(data), col), "U"), data))

    print(max(energy))
