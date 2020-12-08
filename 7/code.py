
#%%

from collections import Counter
import re

#%% LOAD DATA

with open('sample_input.txt') as f:
    rules = [l.strip().strip('.') for l in f.readlines()]


# %%
len(rules)

# %%

def parse_rule(r):
    bag_type, contents = r.replace('bags', 'bag').split(' contain ')
    return bag_type, [c.strip() for c in contents.split(',')]

parsed_rules = [parse_rule(r) for r in rules]
# %%


def extract_type(content_string):
    m = re.search(
        r'(?P<num>[1-9]) (?P<type>[a-zA-Z]* [a-zA-Z]*) bag', 
        content_string
        )

    if m:
        return Counter({m.group('type'): int(m.group('num'))})
    else:
        return Counter()


def count_bags_inside(parsed_rule):

    bag_type = parsed_rule[0].replace(' bag', '')
    bag_contents = parsed_rule[1]
    content_dict = Counter()
    for c in bag_contents:
        content_dict.update(extract_type(c))

    return bag_type, content_dict



#%%
rule_dict = {
    bag_type: contents
    for bag_type, contents in [count_bags_inside(pr) for pr in parsed_rules]
}

# %%
rule_dict
# %%

our_bag = "shiny gold"

# WHICH BAG CAN CONTAIN AT LEAST ONE
def find_direct_carry(rules, our_bag):
    return [
        bag_type for bag_type, contents in rules.items() 
        if our_bag in contents
        ]

# %%

def expand_one_level(contained_bags, rules):
    full_contents = Counter(contained_bags)
    # print(full_contents)
    for contained_bag in contained_bags:
        full_contents.update(rules[contained_bag])

    return full_contents

def recursive_expand(bag_type, rule_dict):

    x = Counter(rule_dict[bag_type])

    len_old, len_new = len(x), -1

    while len_old != len_new:
        len_old = len(x)
        x = expand_one_level(x, rule_dict)
        len_new = len(x)
        # print(len_new)

    return x

# %%

expanded_rules = {
    bag_type: recursive_expand(bag_type, rule_dict)
    for bag_type, _ in rule_dict.items()
    }

expanded_rules
    # %%

dc = find_direct_carry(expanded_rules, 'shiny gold')

#%%

sum(expanded_rules['shiny gold'].values())

# %%

expanded_rules['shiny gold']
# %%

# %%
