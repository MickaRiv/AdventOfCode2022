import numpy as np
import re
from copy import deepcopy

data = np.loadtxt("input",dtype="str",delimiter="#")

mask_move = np.array(["move" in d for d in data])
starting, procedure = data[~mask_move], data[mask_move]

start_stacks = [[letter for letter in stack[-2::-1] if letter != " "]
                for stack in np.transpose([[char for char in line]
                                           for line in starting]) if stack[-1] != " "]
    
def update_stacks(stacks, cmd, reverse=True):
    n, orig, dest = [int(val) for val in re.split("move | from | to ",cmd)[1:]]
    slice_args = [None,-n-1,-1] if reverse else [-n,None,None]
    stacks[dest-1] += stacks[orig-1][slice(*slice_args)]
    stacks[orig-1] = stacks[orig-1][:-n]
    return stacks

stacks = deepcopy(start_stacks)
for cmd in procedure:
    stacks = update_stacks(stacks, cmd)
    
print(f"Top crates are {''.join([str(stack[-1]) for stack in stacks])}")

stacks = deepcopy(start_stacks)
for cmd in procedure:
    stacks = update_stacks(stacks, cmd, reverse=False)
    
print(f"Top crates are {''.join([str(stack[-1]) for stack in stacks])}")