#%%

from collections import Counter

import pandas as pd
# %%

pwds = pd.read_table('input.txt', header=None).iloc[:, 0]
# %%

print(pwds)
# %%

def parse_row(pwd):

    min_max, char, phrase = pwd.split()
    min_max = [int(x) for x in min_max.split('-')]
    char = char.strip(':')

    return min_max, char, phrase


def check_pwd_one(pwd, verbose=False):

    min_max, char, phrase = parse_row(pwd)
    counts = Counter(phrase)

    if verbose:
        print(f'Key char: {char}')
        print(f'Min: {min_max[0]}')
        print(f'Max: {min_max[1]}')
        print(f'Count: {counts[char]}')

    return min_max[0] <= counts[char] <= min_max[1]


def check_pwd_two(pwd):

    min_max, char, phrase = parse_row(pwd)
    pos1 = min_max[0] - 1
    pos2 = min_max[1] - 1

    return ((phrase[pos1] == char) + (phrase[pos2] == char) == 1)


#%%

pwds.apply(check_pwd_one).value_counts()
# %%
pwds.apply(check_pwd_two).value_counts()

# %%
