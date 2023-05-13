#this program takes claean data and simplifies it to make it less cumbersome to process


#Things to do:
#   -convert timestamps into compact ordinal values (1-n where n is the number of visits by a user)
#       -we assume that the data is in order which should be true
#   -convert unique client addresses to compact nominal values (1-n where n is the number of unique client addresses)

def load_sequences():
    filenames = ["session.1996-Q3", "session.1996-Q4", "session.1997-Q1", "session.1997-Q2", "session.1997-Q3", "session.1997-Q4", "session.1998-Q1", "session.1998-Q2", "session.1998-Q3", "session.1998-Q4", "session.1999-Q1", "session.1999-Q2"]
    sequences = []
    for filename in filenames:
        with open("clean_data/" + filename + ".cleaned", "r") as in_file:
            for line in in_file:
                seq = line.split("\t")
                seq[3] = seq[3].strip()
                seq[-1] = seq[-1].strip("\n")
                #print(seq)
                #remove timestamp, id, entry pt
                seq = seq[3:]
                #print(seq)
                sequences.append(seq)
    #print(sequences)
    return sequences

def load_restaurant_features():
    restaurant_features = {}
    with open("original_data/data/chicago.txt", "r") as in_file:
        for line in in_file:
            cur_line = line.split("\t")

            cur_line[-1] = cur_line[-1].strip("\n")
            cur_line[0] = cur_line[0].lstrip("0")
            if cur_line[0] is "":
                cur_line[0] = "0"

            #example element:
            #{"71": ["026", "023", "123"]}
            restaurant_features[cur_line[0]] = cur_line[2].split(" ")
    return restaurant_features


def transform_sequences(sequences):
    unique_events = {}
    restaurant_features = load_restaurant_features()
    for seq_id in range(len(sequences)):
        old_sequence = sequences[seq_id]
        print(old_sequence)
        new_sequence = [] 
        for time_stamp in range(len(old_sequence)):
            transaction = [str(seq_id), str(time_stamp)]


            #Since the last sequence has an implied action of the user choosing the given restaurant,
            #we add 'Z' to represent this action
            if time_stamp == len(old_sequence) - 1:
                restaurant_id = old_sequence[time_stamp]
                action = 'Z'
            else:
                #action is last char
                #restaurant id is all but last char
                restaurant_id = old_sequence[time_stamp][0:-1]
                action = old_sequence[time_stamp][-1]

            event_set = restaurant_features[restaurant_id]
            event_set.append(action)
            for event in event_set:
                if event not in unique_events:
                    unique_events[event] = str(len(unique_events))
                transaction.append(unique_events[event])

            new_sequence.append(transaction)
        sequences[seq_id] = new_sequence

    save_unique_events(unique_events)
    return sequences

def save_sequences(sequences):
    with open("transformed_data/transformed_sequences", "w") as out_file:
        count = 0
        for sequence in sequences:
            for transaction in sequence:
                print(count+=1)
                out_file.write("\t".join(transaction) + "\n")

def save_unique_events(event_dict):
    print(event_dict)
    events = {"L": "browse", "M": "cheaper", "N": "nicer", "O": "closer", "P": "more traditional", "Q": "more creative", "R": "more lively", "S": "quieter", "T": "change cuisine", "Z": "end transaction"}
    #add restaurant features to list of events in format {id, Feature description}
    with open("original_data/data/features.txt", "r") as f:
        for line in f:
            #print(line)
            feature = line.split("\t")
            feature[-1] = feature[-1].strip("\n")
            #print(feature)
            events[str(feature[0])] = str(feature[1])
    #print(events)
    #create kety        
    with open("transformed_data/event_key", "w") as event_key:
        for event, ID in event_dict.items():
            event_key.write(str(ID))
            event_key.write("\t")
            event_key.write(events[event])
            event_key.write("\n")


def main():
    sequences = load_sequences()
    sequences = transform_sequences(sequences)
    print(len(sequences))
    save_sequences(sequences)

if __name__ == "__main__":
    main()
