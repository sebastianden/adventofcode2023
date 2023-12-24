# Answer: 20963

X_MIN, X_MAX = 2e14, 4e14
Y_MIN, Y_MAX = 2e14, 4e14

# X_MIN, X_MAX = 7, 27
# Y_MIN, Y_MAX = 7, 27


def crossing(h1, h2):
    x1, y1, z1, v1x, v1y, v1z = h1
    x2, y2, z2, v2x, v2y, v2z = h2
    # Calculate where lines cross
    print("Hailstone A:", x1, y1, z1, v1x, v1y, v1z)
    print("Hailstone B:", x2, y2, z2, v2x, v2y, v2z)
    try:
        y = ((y1*v1x/v1y) - (y2*v2x/v2y) - x1 + x2)/(v1x/v1y - v2x/v2y)
        x = (y - y1)*v1x/v1y + x1
        t1 = (y - y1)/v1y
        t2 = (y - y2)/v2y
        if (X_MIN <= x <= X_MAX and Y_MIN <= y <= Y_MAX) and (t1 >= 0) and (t2 >= 0):
            print("Crossing within bounds", x, y, '\n')
            return True
        elif (X_MIN <= x <= X_MAX and Y_MIN <= y <= Y_MAX) and (t1 < 0 or t2 < 0):
            print("Crossing within bounds, but in the past", x, y, '\n')
            return False
        else:
            print("Not crossing within bounds", x, y, '\n')
            return False
    except ZeroDivisionError:
        print("Not crossing, parallel", '\n')
        return False


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        inp = f.read().splitlines()

    data = []
    for line in inp:
        d = line.replace(' @', ',')
        d = tuple(int(p) for p in d.split(','))
        data.append(d)

    count = 0
    for i, hail in enumerate(data):
        for j in range(i+1, len(data)):
            if crossing(hail, data[j]):
                count += 1
    print(count)
