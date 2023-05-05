#this program is used to mine for association rules in our sequence dataset
#things that need to be done:
#   -read data from all simplified files and put into correct formatting:
#       -The desired formatting is a list of interactions where each
#           interaction is a list that consists of a sequence_id,
#           a timestamp and an event set which is itself a list
#           of events.
#       -note that all atmoic elements of this datastructure must be integers
from pycspade.helpers import spade, print_result


my_data = [
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
print(my_data)
#result = spade(data=data, support=0.5)
#print(result["seqstrm"])




def load_data():
    filenames = ["session.1996-Q3", "session.1996-Q4", "session.1997-Q1", "session.1997-Q2", "session.1997-Q3", "session.1997-Q4", "session.1998-Q1", "session.1998-Q2", "session.1998-Q3", "session.1998-Q4", "session.1999-Q1", "session.1999-Q2"]
    data = []
    for filename in filenames:
        print(filename)
        with open("simple_data/" + filename + ".simple", "r") as in_file:
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
                
                interaction = [cur_line[0], cur_line[1], event_set]
                data.append(interaction)
                #print(interaction)
                #input()
    return data




def main():
    my_data = load_data()
    print(my_data[0:5])
    result = spade(data=my_data[0:300], support=0.5)
    print(result["seqstrm"])


if __name__ == "__main__":
    main()
