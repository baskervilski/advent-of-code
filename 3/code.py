#%%

import pandas as pd
import numpy as np
from functools import reduce

# %% Read the data

rows = pd.read_table('input.txt', header=None).iloc[:, 0]

# %% Convert to a 2D array and replace '.' with 0 and '#' with 1

class Track:

    def __init__(self, tree_pattern):
        self.tree_pattern = tree_pattern
        self.pattern_width = self.tree_pattern.shape[1]
        self.track_len = self.tree_pattern.shape[0]

    def is_tree(self, location):
        loc_corrected = [location[0], location[1] % self.pattern_width]
        return self.tree_pattern[tuple(loc_corrected)] == 1

    
class Tobogan:

    def __init__(self, start_pos):
        self.start_pos = start_pos
        self.current_pos = self.start_pos
    
    def move_once(self, slope):
        self.current_pos[0] += slope[0]
        self.current_pos[1] += slope[1]



#%%


tree_pattern = np.array([[1 if c == '#' else 0 for c in r] for r in rows])
track = Track(tree_pattern=tree_pattern)

#%%

# tobogan = Tobogan(start_pos=[0, 0])

# Y and X slope

slopes = [
    [1, 1],
    [1, 3],
    [1, 5],
    [1, 7],
    [2, 1],
]

trees_hit_per_slope = []

for slope in slopes:

    tobogan = Tobogan(start_pos=[0, 0])
    trees_hit = 0

    print('START!')

    while tobogan.current_pos[0] < track.track_len - 1:
        tobogan.move_once(slope)
        tree_here = track.is_tree(tobogan.current_pos)
        trees_hit += tree_here

        # print(tobogan.current_pos)
        # print(tree_here)
        # print(trees_hit)
    
    trees_hit_per_slope.append(trees_hit)

trees_hit_product = reduce((lambda x, y: x * y), trees_hit_per_slope)

print(trees_hit_per_slope)
print(trees_hit_product)

# %%


# %%
