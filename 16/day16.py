import numpy as np

def paths_to_dists(orig):
    dists = {}
    for valve in paths[orig]:
        dists[valve] = 2
    for i in range(len(names)):
        new_dists = {}
        for valve,dist in dists.items():
            if dist == i+2:
                for dest in paths[valve]:
                    if dest not in dists and dest != orig:
                        new_dists[dest] = i+3
        dists.update(new_dists)
    return dists

data = np.loadtxt("input",dtype="str",delimiter="#")
names = [d.split()[1] for d in data]
power = {name:int(d.split("=")[1].split(";")[0]) for name,d in zip(names,data)}
power = {name:flow for name,flow in power.items() if flow>0 or name=="AA"}
paths = {name:d.replace("valve ","valves ").split("valves ")[-1].split(", ") for name,d in zip(names,data)}
dists = {name:paths_to_dists(name) for name in power}
restricted_dists = {name:{dest:dist for dest,dist in childs.items() if dest in power} for name,childs in dists.items()}

def get_best(loc,remaining_time,visited=[]):
    if remaining_time<=0:
        return 0
    res = [get_best(dest,remaining_time-dist,visited+[dest]) for dest,dist in restricted_dists[loc].items() if not dest in visited]
    add = 0 if len(res)==0 else np.max(res)
    return power[loc]*remaining_time + add

print(f"Maximum released pressure is {get_best('AA',30)}")

# =============================================================================
# from itertools import combinations
# 
# interesting_valves = [key for key in power.keys() if key!="AA"]
# my_valves = [["AA"]+list(c) for i in range(len(power)) for c in combinations(interesting_valves,i+1)]
# eleph_valves = [["AA"]+[v for v in interesting_valves if v not in my_v] for my_v in my_valves]
# pressures = []
# for i,(my_v,el_v) in enumerate(zip(my_valves,eleph_valves)):
#     if i%(len(my_valves)//100) == 0:
#         print(f"\r{100*i//len(my_valves)}%",end="")
#     pressures.append(get_best('AA',26,my_v) + get_best('AA',26,el_v))
# 
# print(f"\rMaximum released pressure with elephant is {np.max(pressures)}")
# =============================================================================

from collections import defaultdict

save = defaultdict(lambda: 0)
def get_best(loc,remaining_time,visited=[]):
    