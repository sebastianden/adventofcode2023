# Answer: 66530

def get_in_between_coordinates(start, end):
    # Find which coordinate is different
    diff_index = None
    for i in range(len(start)):
        if start[i] != end[i]:
            if diff_index is not None:
                raise ValueError("More than one coordinate differs, list cannot extend in more than one direction.")
            diff_index = i
    # If no difference is found, the start and end are the same
    if diff_index is None:
        return [start]
    # Create the range for the different coordinate
    coord_range = range(start[diff_index], end[diff_index] + 1)
    # Create the list of coordinates
    in_between_coordinates = [start[:diff_index] + [val] + start[diff_index+1:] for val in coord_range]
    return in_between_coordinates


def is_supported_by(block, blocks):
    # Go through the x and y coordinates of the block and see if there is
    # another block directly below any of them
    # If yes return the blocks that are supporting it
    coords = blocks[block]['coordinates']
    x1, y1, z1 = coords[0]
    x2, y2, z2 = coords[-1]
    z = z1 - 1
    # Ground
    if z == 0:
        return 'G'
    supporting = []
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for k, v in blocks.items():
                if [x, y, z] in v['coordinates']:
                    supporting.append(k)
    # print(f"Block {block} is supported by {supporting}")
    return supporting if supporting else None


def count_falling(block, blocks):
    falling = set()
    falling.add(block)
    queue = [block]
    while queue:
        slab = queue.pop(0)
        # Check if the falling block was supporting any other blocks
        for supported in blocks[slab]['supports']:
            # A block is falling if all its supports are in the falling set
            if blocks[supported]['supported_by'].issubset(falling):
                # If it is, add it to the falling set and add it to the queue
                falling.add(supported)
                queue.append(supported)
    return len(falling) - 1


if __name__ == '__main__':
    # Parse input
    with open('input_settled.txt') as f:
        lines = f.read().splitlines()

    # Create a dictionary of blocks
    # blocks = {
    #     1: {
    #         'coordinates': [(1,1,1),(x,y,z)],
    #         'supports': [2],
    #         'supported_by': [3]
    #     },
    #     2: {
    #         ...
    #     }
    # }

    blocks = {}
    for i, line in enumerate(lines):
        coords = line.split('~')
        blocks[i+1] = {
            'coordinates': get_in_between_coordinates(
                list(map(int, coords[0].split(','))),
                list(map(int, coords[1].split(',')))
            ),
            'supports': set(),
            'supported_by': set()
        }

    # Go through blocks and if they're not supported by a block below them,
    # Move them down until they are. (This can take a while because I didn't
    # care to optimize it, use the already settled input to speed it up)
    change = True
    while change:
        change = False
        for block in blocks:
            # Get the blocks that are supporting this block
            while not is_supported_by(block, blocks):
                # Decrease the z coordinate of the block
                for coord in blocks[block]['coordinates']:
                    coord[2] -= 1
                change = True

    # Populate the supports and supported_by lists
    for block in blocks:
        supported_by = is_supported_by(block, blocks)
        if supported_by:
            blocks[block]['supported_by'] = set(supported_by)
            for support in supported_by:
                if support != 'G':
                    blocks[support]['supports'].add(block)

    # We have the tree of blocks
    counter = 0
    for block in blocks:
        falling = count_falling(block, blocks)
        counter += falling
    print(counter)
