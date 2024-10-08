#this program is used to mine for association rules in our sequence dataset
#things that need to be done:
#   -read data from all simplified files and put into correct formatting:
#       -The desired formatting is a list of interactions where each
#           interaction is a list that consists of a sequence_id,
#           a timestamp and an event set which is itself a list
#           of events.
#       -note that all atmoic elements of this datastructure must be integers
from apyori import apriori
import sys


def load_data(filename):
    data = {}
    with open(filename, "r") as in_file:
        for line in in_file:
            cur_line = line.split("\t")
            cur_line[-1] = cur_line[-1].strip("\n")
            action = cur_line[-1]
            cur_line = cur_line[2:-1]
            for x in range(len(cur_line)):
                cur_line[x] = int(cur_line[x])
            
            if action not in data:
                data[action] = []
            data[action].append(cur_line)

    return data

def load_event_keys(key_file):
    data_key = {}
    with open(key_file, "r") as my_file:
        for line in my_file:
            cur_line = line.split("\t")
            cur_line[-1] = cur_line[-1].strip("\n")
            data_key[cur_line[0]] = cur_line[1]
    return data_key

def print_result(event_key, result):
    for rule in list(result):
        output = "{ "
        items = list(list(rule)[0])
        for item in items:
            output += event_key[str(item)] + ", "
        output += "} support: " + str(list(rule)[1])
        print(output)



def main():
    data_file = sys.argv[1]
    key_file = sys.argv[2]
    data_size = int(sys.argv[3])
    support = float(sys.argv[4])

    my_data = load_data(data_file)
    event_key = load_event_keys(key_file)

    for action in my_data:
        result = apriori(transactions=my_data[action][0:data_size], min_support=support)
        #print_output(event_key, output)
        print("\n", event_key[str(action)])
        print_result(event_key, result)

if __name__ == "__main__":
    main()
