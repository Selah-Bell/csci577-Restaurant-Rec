filename = input()

with open(filename, "r") as my_file:
    for x in my_file:
        line = x.split("\t")
        if line[0] == "1":
            print(line)
