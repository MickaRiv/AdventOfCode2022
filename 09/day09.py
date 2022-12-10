import numpy as np

trad = {"R":[1,0], "U":[0,1], "L":[-1,0], "D":[0,-1]}

def move(knots,cmd):
    knots[0] += trad[cmd]
    for i in range(1,len(knots)):
        knots[i] = follow(knots[i-1],knots[i])
    return knots
    
def follow(H,T):
    dist = H-T
    if np.max(np.abs(dist)) > 1:
        T += [d//abs(d) if d!=0 else 0 for d in dist]
    return T
        
knots = np.zeros((2,2)).astype(int)

def track_tail(knots):
    T_history = []
    with open("input","r") as fich:
        for line in fich.readlines():
            cmd,N = line.split()
            for _ in range(int(N)):
                knots = move(knots,cmd)
                T_history.append(tuple(knots[-1]))
    return T_history

T_history = track_tail(knots)

print(f"Tail has visited {len(set(T_history))} tiles")
        
knots = np.zeros((10,2)).astype(int)
T_history2 = track_tail(knots)

print(f"Tail has visited {len(set(T_history2))} tiles")