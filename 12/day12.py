import numpy as np
from matplotlib import pyplot as plt

data = np.array([[ord(letter)-97 for letter in line] for line in np.loadtxt("input",dtype="str")])

start_pos = next((i,j) for i,line in enumerate(data) for j,val in enumerate(line) if val==ord("S")-97)
end_pos = next((i,j) for i,line in enumerate(data) for j,val in enumerate(line) if val==ord("E")-97)
data[start_pos] = 0
data[end_pos] = 25

plt.matshow(data)
plt.plot(*start_pos[::-1],".",color="red")
plt.annotate("Start",start_pos[::-1],color="red")
plt.plot(*end_pos[::-1],".",color="red")
plt.annotate("End",end_pos[::-1],color="red")
plt.colorbar()
plt.show()

steps = ((0,1),(0,-1),(1,0),(-1,0))

def rule(start, end, data):
    return data[end] <= data[start]+1

def backward_rule(start, end, data):
    return rule(end, start, data)

def find_shortest_path_length(data, start_pos, end_pos, rule=rule):
    distances = {start_pos:0}
    for i in range(np.prod(data.shape)):
        new_dists = {}
        for pos,dist in distances.items():
            if dist==i:
                for step in steps:
                    loc = tuple(np.array(pos)+step)
                    if loc not in distances and np.all(np.array(loc) < data.shape) and np.all(np.array(loc) >= (0,0)):
                        if rule(pos,loc,data):
                            if loc in end_pos:
                                return i+1
                            new_dists[loc] = i+1
        distances.update(new_dists)

print(f"End reached with {find_shortest_path_length(data,start_pos,[end_pos])} steps")

low_pos = [(i,j) for i,line in enumerate(data==0) for j,low in enumerate(line) if low]

print(f"Shortest path from any low spot to end takes {find_shortest_path_length(data,end_pos,low_pos,rule=backward_rule)} steps")