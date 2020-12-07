#%%

import numpy as np

#%%

with open('input.txt') as f:
    rows = [l.strip() for l in f.readlines()]


#%%
def bf_to_binary(x):
    return int("0" + x.replace('B', '0').replace('F', '1')\
                      .replace('R', '1').replace('L', '0'), 2)

# %%

def decypher_seat(seat_code):
    row = 127 - bf_to_binary(seat_code[:7])
    col = bf_to_binary(seat_code[7:])
    seat = row*8 + col

    return row, col, seat


arr = np.array([decypher_seat(x) for x in rows])

# %%
seat_nums = list(arr[:, 2])

for i in range(max(seat_nums)):
    if (i not in seat_nums) & ((i - 1) in seat_nums) & ((i + 1) in seat_nums):
        print(i)
# %%

decypher_seat('BBBBBBRRR')

# %%
