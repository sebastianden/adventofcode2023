# Answer: 970

from collections import defaultdict
from heapq import heappop, heappush
from math import inf


def dijkstra(grid, hi):
    # Get the dimensions of the grid
    n, m = len(grid), len(grid[0])
    # dists is a dictionary that maps (i, j, d) to the minimum cost to reach
    # by default, the cost is infinity
    dists = defaultdict(lambda: inf)
    # Initialize a priority queue with the starting positions and directions
    # going right and down
    heap = [(0, (0, 0, (0, 1))), (0, (0, 0, (1, 0)))]
    # While the priority queue is not empty
    while heap:
        # Get the minimum cost and position from the priority queue
        cost, (i, j, d) = heappop(heap)
        # If we have reached the bottom right corner (goal), return the cost
        if (i, j) == (n - 1, m - 1):
            return cost
        # If the cost to reach this position is smaller than the minimum cost
        # for this position
        if cost <= dists[i, j, d]:
            # Get the direction of the previous step
            di, dj = d
            # Get possible next direction by doing a 90 degree turn (switch x
            # and y and negate one of them)
            for ndi, ndj in ((-dj, di), (dj, -di)):
                # Calculate the next position and cost
                ncost = cost
                # Explore all steps into a direction until the limit is reached
                for dist in range(1, hi + 1):
                    # Calculate the next position
                    ni, nj = i + ndi * dist, j + ndj * dist
                    # If the next position is within the grid
                    if 0 <= ni < n and 0 <= nj < m:
                        # The cost is the sum of the previous cost and the
                        # value of the next position
                        ncost += int(grid[ni][nj])
                        # If the cost is smaller than the minimum cost for this
                        k = (ni, nj, (ndi, ndj))
                        if ncost < dists[k]:
                            # Save the cost for this position
                            dists[k] = ncost
                            # Add the next position and cost to the priority queue
                            heappush(heap, (ncost, k))
    return -1


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    print(dijkstra(data, 3))
