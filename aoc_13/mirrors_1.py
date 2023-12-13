# Answer: 30487

import numpy as np


def get_mirror_count(m, axis=0):

    count = 0

    ax_len = np.shape(m)[axis]
    if axis == 1:
        m = np.transpose(m)
    # Find two lines next to each other that are the same
    for i in range(ax_len-1):
        if (m[i] == m[i+1]).all():
            index = i
            print(f"Index {index}")
            # Verify that the center is found
            min_side = min(index, ax_len - index - 2)
            # Go left and right from the index until one side is reached and check that the lines are the same
            for j in range(0, min_side + 1):
                # print(m[index - j])
                # print(m[index + j + 1])
                if not (m[index - j] == m[index + j + 1]).all():
                    index = 0
                    # print("No mirror found")
                    break
            else:
                count += index + 1
                print(f"Mirror found, Axis: {axis}, Count: {count}")
    # print(count)
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()

    single_map = []
    map_list = []
    for line in data:
        if line != '':
            single_map.append(list(line))
        else:
            map_list.append(np.array(single_map))
            single_map = []
    map_list.append(np.array(single_map))

    count = 0
    for m in map_list:
        print(m)
        count += get_mirror_count(m, axis=1)
        count += 100 * get_mirror_count(m, axis=0)
    print(count)
