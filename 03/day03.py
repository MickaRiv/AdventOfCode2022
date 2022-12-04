import numpy as np

data = np.loadtxt("input",dtype="str")

def get_prio(letter):
    return (ord(letter)-97)%58+1

common_elems = []
for backpack in data:
    pocket1, pocket2 = backpack[:len(backpack)//2], backpack[len(backpack)//2:]
    common_elems.append((set(pocket1)&set(pocket2)).pop())
    
print(f"Sum of priorities is {np.sum([get_prio(elem) for elem in common_elems])}")

badges = []
data_grouped = data.reshape(-1,3)
for backpacks in data_grouped:
    badges.append(set.intersection(*[set(backpack) for backpack in backpacks]).pop())
    
print(f"Sum of new priorities is {np.sum([get_prio(badge) for badge in badges])}")