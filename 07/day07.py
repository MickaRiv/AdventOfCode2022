import numpy as np

def set_dict_val(dic, keys, value):
    for key in keys[:-1]:
        dic = dic[key]
    dic[keys[-1]] = value

filesystem = {"/":{}}
path = []
with open("input","r") as fich:
    for line in fich.readlines():
        if line.startswith("$ cd"):
            directory = line.split()[-1]
            direc = "/".join(path[-1:]+[directory])
            path = path[:-1] if directory == ".." else path+[direc]
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            _, direc = line.split()
            direc = "/".join(path[-1:]+[direc])
            set_dict_val(filesystem, path+[direc], {})
        else:
            size, file = line.split()
            file_name = "/".join(path[-1:]+[file])
            set_dict_val(filesystem, path+[file_name], int(size))
            
def get_dir_size(data, name, logs):
    if isinstance(data,int):
        return data
    else:
        size = np.sum([get_dir_size(dir_data,dir_name,logs)
                        for dir_name,dir_data in data.items()])
    logs[name] = size
    return size

logs = {}
get_dir_size(filesystem,"/",logs)

print(f"The sum of directories below 100000 is {np.sum([val for val in logs.values() if val<=100_000])}")

required_space = 30_000_000 - (70_000_000 - logs["/"])
print(f"The smallest dir above threshold is of size {next(size for size in np.sort(list(logs.values())) if size>=required_space)}")