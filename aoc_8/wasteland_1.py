# Answer: 13771

with open('input.txt') as f:
    lines = f.read().splitlines()

instructions = list(lines[0])

nodes = {line.split('=')[0].strip(): tuple(line.split('=')[1].strip(" ()").split(", ")) for line in lines[2:]}

left_right = {'L': 0, 'R': 1}

next_node = 'AAA'
counter = 0
rounds = 0

while next_node != 'ZZZ':
    next_node = nodes[next_node][left_right[instructions[counter]]]
    print("Next node: ", next_node)
    counter += 1
    if counter == len(instructions):
        print("counter too high, resetting")
        counter = 0
        rounds += 1

print(rounds*len(instructions) + counter)
