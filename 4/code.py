#%%

import pandas as pd
import re
#%%

def pass_to_dict(pass_string):
    return {p.split(':')[0]:p.split(':')[1] for p in pass_string.split()}


# %%

def val_byr(x):
    return 1920 <= int(x) <= 2002


def val_iyr(x):
    return 2010 <= int(x) <= 2020


def val_eyr(x):
    return 2020 <= int(x) <= 2030


def val_hgt(x):
    if x.endswith('cm'):
        return 150 <= int(x[:-2]) <= 193
    elif x.endswith('in'):
        return 59 <= int(x[:-2]) <= 76
    else:
        return False

def val_hcl(x):
    return bool(re.search(pattern="#([0-9a-f]{6})", string=x))


def val_ecl(x):
    return x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def val_pid(x: str):
    return x.isnumeric() & (len(x) == 9)

#%%

def check_passport(passport_dict: dict):
    required_fields = {
        "byr": val_byr,
        "iyr": val_iyr,
        "eyr": val_eyr,
        "hgt": val_hgt,
        "hcl": val_hcl,
        "ecl": val_ecl,
        "pid": val_pid,
        # "cid:",
    }
    for key, check in required_fields.items():
        if key in passport_dict:
            if not check(passport_dict[key]):
                print(f'Key: {key}')
                print(f'Invalid value: {passport_dict[key]}')
                return False
        else:
            return False
    else:
        return True

#%%

with open('input.txt') as f:
    all_passports = ''.join(f.readlines()).split('\n\n')

all_passports = [pass_to_dict(p) for p in all_passports]

sum([check_passport(p) for p in all_passports])
# %%
