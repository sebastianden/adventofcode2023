# Answer: 77435348

from multiprocessing import Pool, cpu_count


def string_to_list(string):
    return [int(i) for i in string.split('|')[0].split(' ') if i != '']


def parse_map(map_range):
    key = map_range.pop(0).split(' ')[0]
    val = []
    while map_range:
        val.append(string_to_list(map_range.pop(0)))
    return {key: val}


def parse_seeds(seeds):
    seed_range = []
    while seeds:
        start = seeds.pop(0)
        ran = seeds.pop(0)
        seed_range.append((start, start + ran))
    return seed_range


def get_min_location(seed_range):
    min_location = 99999999999999999
    seeds = range(seed_range[0], seed_range[1])
    for seed in seeds:
        index = seed
        for map_dict in map_list:
            for map_items in map_dict.values():
                for item in map_items:
                    if index >= item[1] and index < item[1] + item[2]:
                        index = item[0] - item[1] + index
                        break
        if index < min_location:
            min_location = index
    print(min_location)


# Read input data
with open("input.txt") as f:
    data = f.read().splitlines()

# Parse input data
map_list = []
while data:
    line = data.pop(0)

    if "seeds:" in line:
        seeds = line.split(':')[1]
        seeds = string_to_list(seeds)

    map_range = []
    if "map:" in line:
        while data and line != "":
            map_range.append(line)
            line = data.pop(0)
        map_list.append(parse_map(map_range))


if __name__ == '__main__':

    # Go through the seed list
    seed_range = parse_seeds(seeds)
    # for (start, end) in seed_range:
    #     print(get_min_location(range(start, end), map_list))

    p = Pool(cpu_count())
    p.map(get_min_location, seed_range)


# Bruteforce no good, took 18 minutes
# 1526666011
# 562057898
# 3520380446
# 653925960
# 77435348 <-- Answer
