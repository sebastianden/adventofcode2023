# Answer: 7674

from tqdm import tqdm


def generate_combinations(pattern, index=0):
    if index == len(pattern):  # Base case: all choices have been made
        return [pattern]
    elif pattern[index] == '?':  # Recursive case: replace '?' with '.' or '#'
        with_dot = generate_combinations(pattern[:index] + '.' + pattern[index+1:], index+1)
        with_hash = generate_combinations(pattern[:index] + '#' + pattern[index+1:], index+1)
        return with_dot + with_hash  # Combine the results
    else:  # Move to the next character if it's not a '?'
        return generate_combinations(pattern, index+1)


def get_damaged_groups(combination):
    damaged_groups = []
    counter = 0

    for i in range(len(combination)):
        if combination[i] == '#':
            counter += 1
        elif combination[i] == '.' and counter != 0:
            damaged_groups.append(counter)
            counter = 0
    if counter != 0:
        damaged_groups.append(counter)
    return tuple(damaged_groups)


def is_combination_valid(combination, damaged_groups):
    if combination.count('#') != sum(damaged_groups):
        return False
    if get_damaged_groups(combination) != damaged_groups:
        return False
    else:
        return True


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    data = [(line.split(' ')[0], tuple(int(i) for i in line.split(' ')[1].split(','))) for line in data]

    counter = 0
    for line in tqdm(data):
        combinations = generate_combinations(line[0])
        for combination in combinations:
            if is_combination_valid(combination, line[1]):
                counter += 1

    print(counter)
