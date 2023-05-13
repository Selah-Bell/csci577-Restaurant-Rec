#this program takes claean data and simplifies it to make it less cumbersome to process

#Things to do:
#   -convert timestamps into compact ordinal values (1-n where n is the number of visits by a user)
#       -we assume that the data is in order which should be true
#   -convert unique client addresses to compact nominal values (1-n where n is the number of unique client addresses)
def load_restaurant_features():
    restaurant_features = {}
    with open("original_data/data/chicago.txt", "r") as in_file:
        for line in in_file:
            cur_line = line.split("\t")

            cur_line[-1] = cur_line[-1].strip("\n")
            cur_line[0] = cur_line[0].lstrip("0")

            #example element:
            #{"71": ["026", "023", "123"]}
            restaurant_features[cur_line[0]] = cur_line[2].split(" ")
    return restaurant_features


def transform_sequences(sequences):
    unique_events = {}
    restaurant_features = load_restaurant_features()
    for seq_id in range(len(sequences)):
        old_sequence = sequences[seq_id]
        new_sequence = [] 
        for time_stamp in range(len(old_sequence)):
            transaction = [seq_id, time_stamp]

            #restaurant id is all but last char
            restaurant_id = old_sequence[time_stamp][0:-1]

            #Since the last sequence has an implied action of the user choosing the given restaurant,
            #we add 'Z' to represent this action
            if time_stamp == len(old_sequence) - 1:
                action = 'Z'
            else:
                #action is last char
                action = old_sequence[time_stamp][-1]

            event_set = restaurant_features[restaurant_id]
            event_set.append(action)
            for event in range(len(event_set)):
                if event not in unique_events:
                    unique_events[event] = len(unique_events)
                transaction.append(unique_events[event])

            new_sequence.append(transaction)
        sequences[seq_id] = new_sequence

    save_unique_events(unique_events)
    return sequences

def save_sequences(sequences):
    with open("transformed_data/transformed_sequences", "w") as out_file:
        for sequence in sequences:
            for transaction in sequence:
                out_file.write("\t".join(cur_line) + "\n")




def main():
    sequences = load_sequences()
    sequences = transform_sequences(sequences)
    save_sequences(sequences)

if __name__ == "__main__":
    main()