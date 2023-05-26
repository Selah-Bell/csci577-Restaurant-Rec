#this program takes clean data, removes query start points, separates by city 


#Things to do:
#   -remove entry points w/ 0 value
#   - split data into 8 cities
#   - create sequences for each city

def load_sequences():
    filenames = ["session.1996-Q3", "session.1996-Q4", "session.1997-Q1", "session.1997-Q2", "session.1997-Q3", "session.1997-Q4", "session.1998-Q1", "session.1998-Q2", "session.1998-Q3", "session.1998-Q4", "session.1999-Q1", "session.1999-Q2"]
    city_sequences = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []} 
    city_count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0} 
    for filename in filenames:
        with open("clean_data/" + filename + ".cleaned", "r") as in_file:
            for line in in_file:
                seq = line.split("\t")
                seq[3] = seq[3].strip()
                seq[2] = seq[2].strip()
                seq[-1] = seq[-1].strip("\n")
                #print(seq)
                #only non-zero entry points
                if seq[2] != "0":
                    #remove timestamp, id, 
                    seq = seq[2:]
                    #print(seq)
                    #add to city list of sequences
                    city_sequences[seq[0][-1]].append(seq)
                    city_count[seq[0][-1]] += 1
    print(city_count)
    for city in city_sequences: print(city + ": "+str(len(city_sequences[city])))
    print(city_sequences["A"][0])
    return city_sequences

def get_restaurant_features(city):
    entry_restaurant_features = load_restaurant_features(city)
    if city == "chicago":
         chicago_restaurant_features = entry_restaurant_features
    else:
        chicago_restaurant_features = load_restaurant_features("chicago")
    return entry_restaurant_features, chicago_restaurant_features

def load_restaurant_features(city):
    restaurant_features = {}
    file_path = "original_data/data/"+city+".txt"
    print(file_path)
    with open(file_path, "r") as in_file:
        for line in in_file:
            cur_line = line.split("\t")

            cur_line[-1] = cur_line[-1].strip("\n")
            cur_line[0] = cur_line[0].lstrip("0")
            if cur_line[0] is "":
                cur_line[0] = "0"

            #example element:
            #{"71": ["026", "023", "123"]}
            restaurant_features[cur_line[0]] = cur_line[2].split(" ")
    #print(restaurant_features)
    return restaurant_features


def transform_sequences(entry_city_id, entry_city, sequences, entry_restaurant_features, chicago_restaurant_features):
    unique_events = {}
    features = load_features()
    #chicago_restaurant_features = load_restaurant_features()
    for seq_id in range(len(sequences)):
        old_sequence = sequences[seq_id]
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
            #use entry point events
            if action == entry_city_id:
                event_set = entry_restaurant_features[restaurant_id]

            else:
                event_set = chicago_restaurant_features[restaurant_id]
            print(event_set)
            for event in event_set:
                feature = features[event]
                if feature not in unique_events:
                    unique_events[feature] = str(len(unique_events))
                transaction.append(unique_events[feature])
            #add start transaction event
            if action == entry_city_id:
                features[action] = "start transaction"
            feature = features[action]
            if feature not in unique_events:
                unique_events[feature] = str(len(unique_events))
            transaction.append(unique_events[feature])

            new_sequence.append(transaction)
        sequences[seq_id] = new_sequence

    save_unique_events(entry_city, unique_events)
    return sequences

def save_sequences(entry_city, sequences):
    file_path = "transformed_city_data/"+entry_city+"/transformed_sequences"
    with open(file_path, "w") as out_file:
        count = 0
        for sequence in sequences:
            for transaction in sequence:
                count+=1
                print(count)
                out_file.write("\t".join(transaction) + "\n")



def load_features():
    events = {"L": "browse", "M": "cheaper", "N": "nicer", "O": "closer", "P": "more traditional", "Q": "more creative", "R": "more lively", "S": "quieter", "T": "change cuisine", "Z": "end transaction"}
    #add restaurant features to list of events in format {id, Feature description}
    with open("original_data/data/features.txt", "r") as f:
        for line in f:
            #print(line)
            feature = line.split("\t")
            feature[-1] = feature[-1].strip("\n")
            #print(feature)
            events[str(feature[0])] = str(feature[1])
    print("HERE")
    print(events)
    return events

def save_unique_events(entry_city, event_dict):
    print(event_dict)
    #create kety        
    file_path = "transformed_city_data/"+entry_city+"/event_key"
    with open(file_path, "w") as event_key:
        for event, ID in event_dict.items():
            event_key.write(str(ID))
            event_key.write("\t")
            event_key.write(event)
            event_key.write("\n")


def main():
    entry_dict = {"A": "atlanta", "B": "boston", "C": "chicago", "D": "los_angeles", "E": "new_orleans", "F": "new_york", "G": "san_francisco", "H": "washington_dc"}
    city_sequences = load_sequences()
    for city in city_sequences:
        entry_restaurant_features, chicago_restaurant_features = get_restaurant_features(entry_dict[city])
        sequences = transform_sequences(city, entry_dict[city], city_sequences[city], entry_restaurant_features, chicago_restaurant_features)
        #print(len(sequences))
        save_sequences(entry_dict[city], sequences)

if __name__ == "__main__":
    main()
