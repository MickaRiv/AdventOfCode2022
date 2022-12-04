import numpy as np

data = np.loadtxt("input",dtype="str",delimiter=",")
bounds = np.array([[[int(n) for n in d.split("-")] for d in dat] for dat in data])

complete_overlaps = np.prod(np.diff(bounds.transpose(0,2,1),axis=2)[:,:,0],axis=1)<=0

print(f"Number of complete overlaps found: {np.sum(complete_overlaps)}")

partial_overlaps = np.diff(bounds,axis=-1)[:,:,0].sum(axis=1) >= bounds.max(axis=(1,2))-bounds.min(axis=(1,2))

print(f"Number of partial overlaps found: {np.sum(partial_overlaps)}")