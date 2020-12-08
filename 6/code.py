from functools import reduce

#%% LOAD DATA

with open('input.txt') as f:
    all_groups = ''.join(f.readlines()).split('\n\n')

print(len(all_groups))
# %%

all_groups = [g.split() for g in all_groups]
# %% COUNT HOW MANY DISTINCT ANSWERS
sum([len(set(''.join(g))) for g in all_groups])

# %% COUNT COMMON ANSWERS

def count_common(answers):
    return len(reduce(
        lambda x, y: set(x).intersection(y),
        answers
        ))

print(sum([count_common(a) for a in all_groups]))
