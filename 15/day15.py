import numpy as np

regexp = r"(-?\d+)"
data = np.fromregex('input', regexp, [('pos', np.int64)])
data = data["pos"].reshape(data.shape[0]//4,2,-1)

sensor_clear_radius = np.linalg.norm(data[:,0]-data[:,1],axis=1,ord=1).astype(int)

row = 2_000_000

clear_cols = set()
for pos,radius in zip(data[:,0],sensor_clear_radius):
    margin = radius - abs(pos[1]-row)
    if margin >= 0:
        clear_cols.update(np.arange(pos[0]-margin,pos[0]+margin+1).astype(int))
beacon_on_row = set([x for x,y in data[:,1] if y==row])

print(f"Exactly {len(clear_cols.difference(beacon_on_row))} positions cannot contain a beacon")

comb = [lambda i,N: (i,N-i), lambda i,N: (-N+i,i), lambda i,N: (-i,-N+i), lambda i,N: (N-i,-i)]
def circle_points(center,N):
    return center + np.array([c(i,N) for c in comb for i in range(N)])

from scipy.spatial.distance import cdist

def get_beacon_position(sensors,sensor_clear_radius):
    for i,(pos,radius) in enumerate(zip(sensors,sensor_clear_radius)):
        points = circle_points(pos,radius+1)
        inside_points = points[np.logical_and(np.all(points >= 0,axis=1),np.all(points <= maxi,axis=1))]
        hidden = np.all(cdist(inside_points,sensors,metric="cityblock")>sensor_clear_radius,axis=1)
        if np.any(hidden):
            return inside_points[next(i for i,h in enumerate(hidden) if h)]
            
maxi = 2*row
lims = [0,maxi]
freqs = [4_000_000,1]

print(f"The tuning frequency of the distress beacon is {np.dot(freqs,get_beacon_position(data[:,0], sensor_clear_radius))}")