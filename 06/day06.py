import numpy as np

data = str(np.loadtxt("input",dtype="str"))

def get_SO(stream, N):
    return next(i for i in range(N,len(data)) if len(set(data[i-N:i]))==N)

print(f"First start-of-packet found at {get_SO(data,4)}")

print(f"First start-of-message found at {get_SO(data,14)}")