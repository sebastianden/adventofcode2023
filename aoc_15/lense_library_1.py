# Answer: 506437

def hash(inp):
    val = 0
    for c in inp:
        val += ord(c)
        val *= 17
        val %= 256
    return val


if __name__ == '__main__':
    # Read in the first line of the input file
    with open('input.txt', 'r') as f:
        line = f.readline().strip()

    data = [step for step in line.split(',')]

    total = 0
    for step in data:
        total += hash(step)
    print(total)
