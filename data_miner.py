#this program is used to mine for association rules in our sequence dataset
#things that need to be done:
#   -read data from all simplified files and put into correct formatting:
#       -The desired formatting is a list of interactions where each
#           interaction is a list that consists of a sequence_id,
#           a timestamp and an event set which is itself a list
#           of events.
#       -note that all atmoic elements of this datastructure must be integers
from pycspade.helpers import spade, print_result


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
]
print(my_data)"""
#result = spade(data=data, support=0.5)
#print(result["seqstrm"])

def load_event_keys

def load_data(filename):
    data = []
    y = 0
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

def main():
    my_data = load_data()

    result = spade(data=my_data[0:44400], support=support)
    output = result["mined_objects"]
    data_key = translate_data(event_translation_file)
    #print(data_key)
    for x in range(len(output)):
        output[x] = str(output[x])
        to_replace = ""
        i = 0
        while output[x][i] != "(":
            i += 1
        i += 1
        while output[x][i] != ")":
            to_replace += output[x][i]
            i += 1
        #print(to_replace)
        output[x] = output[x].replace(to_replace, data_key[to_replace])
    for x in output:
        print(x)
    #print("count:", count)


if __name__ == "__main__":
    main()
