import numpy as np

data_str = np.loadtxt("input",dtype="str")
data = np.array([[d for d in line] for line in data_str]).astype(int)

visible = np.full_like(data,True).astype(bool)

for i,line in enumerate(data[1:-1]):
    for j,val in enumerate(line[1:-1]):
        aligned = [data[i+1,:j+1],data[i+1,j+2:],data[:i+1,j+1],data[i+2:,j+1]]
        if np.all([np.max(height)>=data[i+1,j+1] for height in aligned]):
            visible[i+1,j+1] = False
            
print(f"{np.sum(visible)} trees are visible")

def get_view(heights, my_height):
    try:
        view = next(i+1 for i,height in enumerate(heights) if height>=my_height)
    except StopIteration:
        view = len(heights)
    return view

scenic_score = np.zeros_like(data)

for i,line in enumerate(data[1:-1]):
    for j,val in enumerate(line[1:-1]):
        aligned_ordered = [data[i+1,:j+1][::-1],data[i+1,j+2:],data[:i+1,j+1][::-1],data[i+2:,j+1]]
        scenic_score[i+1,j+1] = np.prod([get_view(heights, data[i+1,j+1]) for heights in aligned_ordered])

print(f"Best scenic score is {np.max(scenic_score)}")