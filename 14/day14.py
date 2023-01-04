import numpy as np

up, down, left, right = (-1,0), (1,0), (0,-1), (0,1)

def drop_sand_unit(scan, source, true_source, roll_back_optim=True):
    loc = np.array(source)
    prev_loc = loc
    while True:
        for dest in [loc+down, loc+down+left, loc+down+right]:
            if np.any(dest<0) or np.any(dest>=scan.shape):
                return False, None
            if not scan[tuple(dest)]:
                if roll_back_optim:
                    roll_back[tuple(dest)] = loc
                loc = dest
                break
        else:
            scan[tuple(loc)] = 1
            return tuple(loc) != tuple(true_source), tuple(loc)
        
def get_count(scan, source, roll_back_optim=True):
    no_stop = True
    count = 0
    loc = tuple(source)
    while no_stop:
        count += 1
        no_stop, loc = drop_sand_unit(scan, roll_back.get(loc,source), source, roll_back_optim)
    return count

data = np.loadtxt("input",dtype="str",delimiter="#")
pairs = [(eval(pos1),eval(pos2)) for line in data for pos1,pos2 in zip(line.split(" -> ")[:-1],line.split(" -> ")[1:])]
mini, maxi = np.min(pairs,axis=(0,1)), np.max(pairs,axis=(0,1))
mini[1] = 0

scan = np.zeros(maxi-mini+1).astype(int)
rocks_ind = np.concatenate([np.linspace(*pair,abs(np.diff(pair,axis=0).sum())+1).astype(int)
                            for pair in pairs]) - mini
scan[tuple(rocks_ind.T)] = -1
scan = scan.T
save_scan = scan.copy()

roll_back = {}
count = get_count(scan,((500,0)-mini)[::-1],roll_back_optim=True)
    
print(f"The number of units of sand at rest is {count-1}")

full_scan = np.zeros((scan.shape[0]+2,2*(scan.shape[0]+2))).astype(int)
insert_ind = mini[0]-500+full_scan.shape[0]
full_scan[:-2,insert_ind:insert_ind+scan.shape[1]] = save_scan
full_scan[-1] = -1

roll_back = {}
count = get_count(full_scan,(0,full_scan.shape[0]),roll_back_optim=True)
    
print(f"The number of units of sand at rest is now {count}")