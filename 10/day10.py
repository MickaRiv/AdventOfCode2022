import numpy as np

with open("input","r") as fich:
    data = []
    for line in fich.readlines():
        if "noop" in line:
            data.append(0)
        else:
            val = int(line.split()[-1])
            data.append(val)
            data.append(0)

cum = np.cumsum(data) + 1
inds= np.arange(0,221)[20::40]
X = np.concatenate(([1,1],cum))
print(f"Sum of signal strenghs is {np.dot(inds,X[inds-1])}")

line_length = 40
symb = []
for i in range(6):
    symb.append(["#" if k-1 <= X[i*line_length+k] <= k+1 else " " for k in range(line_length)])
    
for line in symb:
    print("".join(line))