from collections import OrderedDict
import numpy as np

with open("original_data/data/chicago.txt", "r") as my_file:
    attributes = {}
    for line in my_file:
        cur_line = line.split("\t")
        ats = cur_line[2].strip("\n").split(" ")
        for x in ats:
            if x not in attributes:
                attributes[x] = 0
            attributes[x] += 1

with open("original_data/data/features.txt", "r") as key_file:
    key = {}
    for line in key_file:
        split_line = line.strip("\n").split("\t")
        key[split_line[0]] = split_line[1]


dict = attributes
keys = list(dict.keys())
values = list(dict.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

for x in sorted_dict:
    print(key[x] + ": \t\t" + str(sorted_dict[x]))