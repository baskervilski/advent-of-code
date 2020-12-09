#%%

from itertools import combinations

#%%

with open('input.txt') as f:
    numbers = [int(l.strip()) for l in f.readlines()]
# %%
numbers
# %%

window = 25

for curr_pos in range(window, len(numbers)):

    valid_nums = [
        x + y
        for x, y
        in combinations(numbers[curr_pos - window:curr_pos], 2)
    ]

    if numbers[curr_pos] not in valid_nums:
        invalid_num = numbers[curr_pos]
        print("pos:", curr_pos)
        print("val:", invalid_num)
        break

#%%

for start, stop in list(combinations(range(len(numbers)), 2)):

    rng = numbers[start:stop + 1]
    if sum(rng) == invalid_num:
        print("Range:", rng)
        print(f"Min = {min(rng):,}")
        print(f"Max = {max(rng):,}")
        print(f"Min + Max = {min(rng) + max(rng):,}")
        break
# %%
# %%
