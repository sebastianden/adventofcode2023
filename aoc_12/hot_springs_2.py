# Answer: 4443895258186

from tqdm import tqdm
from functools import lru_cache, cache


@cache
def check_combination(combination, damaged_groups):
    if len(combination) == 0:
        return 1 if len(damaged_groups) == 0 else 0
    if combination.startswith('.'):
        return check_combination(combination.strip('.'), damaged_groups)
    if combination.startswith('?'):
        return check_combination(combination[1:], damaged_groups) + \
            check_combination(combination.replace('?', '#', 1), damaged_groups)
    if combination.startswith('#'):
        if len(damaged_groups) == 0:
            return 0
        if len(combination) < damaged_groups[0]:
            return 0
        if any(['.' in combination[:damaged_groups[0]]]):
            return 0
        if all([i == '#' for i in combination[:damaged_groups[0]]]):
            if len(combination) == damaged_groups[0]:
                return 1 if len(damaged_groups) == 1 else 0
            elif combination[damaged_groups[0]] == '#':
                return 0
            elif combination[damaged_groups[0]] == '.' or combination[damaged_groups[0]] == '?':
                return check_combination(combination[damaged_groups[0] + 1:], damaged_groups[1:])
        elif len(combination) >= damaged_groups[0]:
            # Replace the next question mark with a hash
            return check_combination(combination.replace('?', '#', 1), damaged_groups)
    raise Exception('Something went wrong')


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    data = [(line.split(' ')[0], tuple(int(i) for i in line.split(' ')[1].split(','))) for line in data]

    # Extend 5 times for part 2
    data = [('?'.join([line[0]]*5), line[1] * 5) for line in data]

    counter = 0
    for line in tqdm(data):
        counter += check_combination(line[0], line[1])
    print(counter)
