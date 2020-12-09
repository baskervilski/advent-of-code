
#%%

from collections import Counter
import re

# %% BASIC PREP FUNCTIONS

def parse_rule(r):
    bag_type, contents = r.replace('bags', 'bag').split(' contain ')
    return bag_type, [c.strip() for c in contents.split(',')]


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


def find_direct_carry(rules, our_bag):
    return [
        bag_type for bag_type, contents in rules.items() 
        if our_bag in contents
        ]

#%%

def recursive_expand(bag_type, rule_dict):

    if not rule_dict[bag_type]:
        return Counter()

    tmp_counter = Counter(rule_dict[bag_type])

    for sub_bag, sub_count in rule_dict[bag_type].items():
        sub_expanded = {
            key: val*sub_count 
            for key, val in recursive_expand(sub_bag, rule_dict).items()
        }
        tmp_counter.update(sub_expanded)

    return tmp_counter


#%% LOAD DATA

with open('input.txt') as f:
    rules = [l.strip().strip('.') for l in f.readlines()]


# %%
len(rules)
#%%

parsed_rules = [parse_rule(r) for r in rules]

rule_dict = {
    bag_type: contents
    for bag_type, contents in [count_bags_inside(pr) for pr in parsed_rules]
}

# %%


expanded_rules = {
    bag_type: recursive_expand(bag_type, rule_dict)
    for bag_type, _ in rule_dict.items()
    }

# expanded_rules
#%% HOW MANY BAGS CAN CARRY SHINY GOLD?

our_bag = "shiny gold"

dc = find_direct_carry(expanded_rules, our_bag)

#%% HOW MANY BAGS DOES A SHINY GOLD CONTAIN?

sum(expanded_rules[our_bag].values())

