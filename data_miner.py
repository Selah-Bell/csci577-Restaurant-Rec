#this program is used to mine for association rules in our sequence dataset
#things that need to be done:
#   -read data from all simplified files and put into correct formatting:
#       -The desired formatting is a list of interactions where each
#           interaction is a list that consists of a sequence_id,
#           a timestamp and an event set which is itself a list
#           of events.
#       -note that all atmoic elements of this datastructure must be integers
from pycspade.helpers import spade, print_result
import sys

"""my_data = [
    [1, 10, [3, 4]],
    [1, 15, [1, 2, 3]],
    [1, 20, [1, 2, 6]],
    [1, 25, [1, 3, 4, 6]],
    [2, 15, [1, 2, 6]],
    [2, 20, [5]],
    [3, 10, [1, 2, 6]],
    [4, 10, [4, 7, 8]],
    [4, 20, [2, 6]],
    [4, 25, [1, 7, 8]]
]"""
#result = spade(data=data, support=0.5)
#print(result["seqstrm"])


def load_data(filename):
    data = []
    with open(filename, "r") as in_file:
        for line in in_file:
            cur_line = line.split("\t")
            cur_line[-1] = cur_line[-1].strip("\n")
            for i in cur_line:
                if " " in i:
                    print(filename)
                    print(line)
                    print(cur_line)
                    input()
            for x in range(len(cur_line)):
                cur_line[x] = int(cur_line[x])
            
            event_set = cur_line[2:]  
            
            transaction = [cur_line[0], cur_line[1], event_set]
            data.append(transaction)

    return data

def load_event_keys(key_file):
    data_key = {}
    with open(key_file, "r") as my_file:
        for line in my_file:
            cur_line = line.split("\t")
            cur_line[-1] = cur_line[-1].strip("\n")
            data_key[cur_line[0]] = cur_line[1]
    return data_key

def print_output(event_key, output):
    for line in output:
        inline = str(line)
        outline = ""
        x = 0
        while x < len(inline):
            if inline[x] == "(":
                outline += "("
                x += 1
                key = ""
                while inline[x] != ")":
                    while inline[x] != ")" and inline[x] != ",":
                        key += inline[x]
                        x += 1
                    outline += event_key[key]
                    if inline[x] == ",":
                        outline += ","
                        x += 1
                outline += ")"
            else:
                outline += inline[x]
            x += 1
        print(outline)


def main():
    data_file = sys.argv[1]
    key_file = sys.argv[2]
    data_size = int(sys.argv[3])
    support = float(sys.argv[4])

    my_data = load_data(data_file)
    event_key = load_event_keys(key_file)

    result = spade(data=my_data[0:data_size], support=support)
    output = result["mined_objects"]

    print_output(event_key, output)

if __name__ == "__main__":
    main()
