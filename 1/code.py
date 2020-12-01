#%%

import pandas as pd
import numpy as np
from itertools import combinations
from functools import reduce

#%% READ INPUT

vals = pd.read_csv('input.csv', header=None).iloc[:, 0].values

target_sum = 2020

#%% FIND THE COMBINATION

def find_combo(vals, target_sum, combo_len):
    # We iterate over all combinations of values
    for combo in list(combinations(vals, r=combo_len)):
        if sum(combo) == target_sum:
            print('Combo:', combo)
            product = reduce((lambda x, y: x * y), combo)
            print('Product:', product)

#%%
find_combo(vals, target_sum, combo_len=2)
# %%
find_combo(vals, target_sum, combo_len=3)
