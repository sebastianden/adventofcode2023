# Answer: 46334


def shoe_lace(polygon):
    polygon.append(polygon[0])
    area = 0
    for i in range(len(polygon) - 1):
        area += polygon[i][1] * polygon[i + 1][0]
        area -= polygon[i][0] * polygon[i + 1][1]
    area = abs(area) / 2
    return area


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()

    data = [(line.split(' ')[0], int(line.split(' ')[1])) for line in data]

    # Make a list of coordinates
    coords = [(0, 0)]
    for instruction in data:
        last = coords[-1]
        if instruction[0] == 'R':
            coords.append((last[0], last[1] + instruction[1]))
        if instruction[0] == 'L':
            coords.append((last[0], last[1] - instruction[1]))
        if instruction[0] == 'U':
            coords.append((last[0] - instruction[1], last[1]))
        if instruction[0] == 'D':
            coords.append((last[0] + instruction[1], last[1]))

    shoe_lace_area = shoe_lace(coords)
    area = shoe_lace_area + sum([dist for dir, dist in data])/2 + 1

    print(int(area))
