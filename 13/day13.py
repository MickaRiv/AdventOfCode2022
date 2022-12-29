import numpy as np
from functools import cmp_to_key

def check_order(packet1, packet2):
    if isinstance(packet1, int) and isinstance(packet2, int):
        return (packet1 > packet2) - (packet1 < packet2)
    elif isinstance(packet1, int):
        packet1 = [packet1]
    elif isinstance(packet2, int):
        packet2 = [packet2]
    for p1, p2 in zip(packet1,packet2):
        if order := check_order(p1, p2):
            return order
    return check_order(len(packet1),len(packet2))

data = [eval(line) for line in np.loadtxt("input",dtype="str")]

orders = [check_order(pack1,pack2) for pack1,pack2 in zip(data[::2],data[1::2])]

print(f"Sum of indices of ordered pairs equals {np.sum([i+1 for i,o in enumerate(orders) if o==-1])}")

divider_packets = [[2],[6]]
ordered_data = sorted(data+divider_packets, key=cmp_to_key(check_order))

print(f"Product of the indices of divider packets equals {np.prod([i+1 for i,p in enumerate(ordered_data) if p in divider_packets])}")