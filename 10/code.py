#%%
import pandas as pd
from itertools import combinations
#%%

with open('input.txt') as f:
    input_list = [int(l.strip()) for l in f.readlines()]
    voltages = pd.Series([0] + input_list + [max(input_list) + 3]).sort_values().reset_index(drop=True)
# %%
counts = voltages.diff().value_counts()
# %% SOLUTION 1:
print(counts[1] * counts[3])

# %% WHICH CONNECTIONS ARE VALID?

valid_jumps = []
for i, j in combinations(range(len(voltages)), 2):
    pair_diff = voltages[j] - voltages[i]
    if 1 <= pair_diff <= 3:
        valid_jumps.append([i, j])

valid_jumps = pd.DataFrame(valid_jumps, columns=['i', 'j']) 

#%% GOING BACKWARDS, CALCULATE THE NUMBER OF VALID DOWNSTREAM PATHS

for idx in list(valid_jumps.index)[-1::-1]:
    if idx == len(valid_jumps) - 1:
        valid_jumps.loc[idx, 'downstream_options'] = 1
    else:
        i, j = valid_jumps.loc[idx, ['i', 'j']]
        valid_jumps.loc[idx, 'downstream_options'] = valid_jumps.loc[valid_jumps.i == j, 'downstream_options'].sum()

#%% CORRECT!

print(valid_jumps.set_index('i').loc[0, 'downstream_options'].sum())
