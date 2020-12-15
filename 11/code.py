#%%

import numpy as np
import itertools

#%%

with open('input.txt') as f:
    start_state = np.array([[c for c in line.strip()] for line in f.readlines()])

start_state


#%%

stable_state_sample = (
    """
    #.#L.L#.##
    #LLL#LL.L#
    L.#.L..#..
    #L##.##.L#
    #.#L.LL.LL
    #.#L#L#.##
    ..L.L.....
    #L#L##L#L#
    #.LLLLLL.L
    #.#L#L#.##
    """
)

stable_arr = np.array([[c for c in line] for line in stable_state_sample.split()])
# %%

def valid_point(point, nrows, ncols):
    i, j = point
    return (0 <= i < nrows) & (0 <= j < ncols)


def get_neighbor_indices(point, array_shape, neighbor_limit):

    i, j = point
    nrows, ncols = array_shape

    neighbors = dict(
        north = [(i - x, j) for x in range(1, neighbor_limit + 1) if valid_point((i - x, j), nrows, ncols)],
        south = [(i + x, j) for x in range(1, neighbor_limit + 1) if valid_point((i + x, j), nrows, ncols)],
        east = [(i, j + x) for x in range(1, neighbor_limit + 1) if valid_point((i, j + x), nrows, ncols)],
        west = [(i, j - x) for x in range(1, neighbor_limit + 1) if valid_point((i, j - x), nrows, ncols)],

        northwest = [(i - x, j - x) for x in range(1, neighbor_limit + 1) if valid_point((i - x, j - x), nrows, ncols)],
        southwest = [(i + x, j - x) for x in range(1, neighbor_limit + 1) if valid_point((i + x, j - x), nrows, ncols)],
        northeast = [(i - x, j + x) for x in range(1, neighbor_limit + 1) if valid_point((i - x, j + x), nrows, ncols)],
        southeast = [(i + x, j + x) for x in range(1, neighbor_limit + 1) if valid_point((i + x, j + x), nrows, ncols)]
    )
    
    return neighbors

#%%

def count_around(point, array, reach='immediate'):

    if reach == 'immediate':
        neighbor_limit = 1
    elif reach == 'full_diagonals':
        neighbor_limit = min(array.shape)
    else:
        raise ValueError(f'Unknown reach type {reach}')

    neighbors = get_neighbor_indices(point, array.shape, neighbor_limit)

    counter = 0
    for axis, points in neighbors.items():
        for point in points:
            if array[point] == '#':
                counter += 1
                break
            elif array[point] == 'L':
                break

    return counter


def get_next_state(point, old_state, reach, bailout_occupancy=4, verbose=False):

    occupied_neighbors = count_around(point, old_state, reach=reach)

    if verbose:
        print("Occupied neighbors:", occupied_neighbors)

    current = old_state[tuple(point)]
    if current == '.':
        return current
    elif (current == 'L') & (occupied_neighbors == 0):
        return '#'
    elif (current == '#') & (occupied_neighbors >= bailout_occupancy):
        return 'L'
    else:
        return current


def get_new_state_all(old_state, reach='immediate', bailout_occupancy=4):

    new_state = old_state.copy()
    for i in range(old_state.shape[0]):
        for j in range(old_state.shape[1]):
            new_state[i, j] = get_next_state(
                point=(i, j),
                old_state=old_state, 
                reach=reach,
                bailout_occupancy=bailout_occupancy
                )

    return new_state

#%%

# %%
old_state = start_state.copy()

verbose = True
max_iter = 1000

for i in range(max_iter):
    new_state = get_new_state_all(old_state, reach='full_diagonals', bailout_occupancy=5)
    # print(new_state)
    old_state_similarity = (new_state == old_state).mean()
    if verbose:
        print(old_state_similarity)
        # print(new_state)

    if (old_state_similarity == 1):
        print('Done!', "Iteration:", i)
        break
    old_state = new_state.copy()

#%%

print(i)
print(old_state)
print(get_next_state((1, 2), old_state, reach='full_diagonals', bailout_occupancy=5, verbose=True))

#%%

sum(sum(new_state == '#'))

# %%
i, j = 5, 1
occupied_neighbors = count_around((i, j), old_state)
print(i, j)
print(old_state)
print(occupied_neighbors)
print("Current state:", old_state[(i, j)])
print('Next state', get_next_state(old_state[(i, j)], occupied_neighbors))
# %%

get_neighbor_indices((1, 1), old_state.shape, 2)
# %%
