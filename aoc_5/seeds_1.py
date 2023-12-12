# Answer: 910845529


def string_to_list(string):
    return [int(i) for i in string.split('|')[0].split(' ') if i != '']


def parse_map(map_range):
    key = map_range.pop(0).split(' ')[0]
    val = []
    while map_range:
        val.append(string_to_list(map_range.pop(0)))
    return {key: val}


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

# Go through the seed list
location_list = []
for seed in seeds:
    index = seed
    for map_dict in map_list:
        for map_name, map_items in map_dict.items():
            for item in map_items:
                if index in range(item[1], item[1] + item[2]):
                    index = item[0] - item[1] + index
                    break
    location_list.append(index)
print(min(location_list))
