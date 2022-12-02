import numpy as np

data = [[]]
with open("input","r") as file:
    for line in file.read().splitlines():
        if line:
            data[-1].append(int(line))
        else:
            data.append([])

sums = np.array([np.sum(d) for d in data])
print(f"Le plus gros total de calories est de {np.max(sums)}")

print(f"La somme des trois plus gros totaux est de {np.sum(np.sort(sums)[-3:])}")