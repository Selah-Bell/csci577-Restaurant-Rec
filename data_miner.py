#this program is used to mine for association rules in our sequence dataset
#things that need to be done:
#   -read data from all simplified files and put into correct formatting:
#       -The desired formatting is a list of interactions where each
#           interaction is a list that consists of a sequence_id,
#           a timestamp and an event set which is itself a list
#           of events.
#       -note that all atmoic elements of this datastructure must be integers
from pycspade.helpers import spade, print_result

data = [
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
result = spade(data=data, support=0.5)
print(result["seqstrm"])