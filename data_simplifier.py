#this program takes claean data and simplifies it to make it less cumbersome to process

#Things to do:
#   -convert timestamps into compact ordinal values (1-n where n is the number of visits by a user)
#       -we assume that the data is in order which should be true
#   -convert unique client addresses to compact nominal values (1-n where n is the number of unique client addresses)

def main():
    filenames = ["session.1996-Q3", "session.1996-Q4", "session.1997-Q1", "session.1997-Q2", "session.1997-Q3", "session.1997-Q4", "session.1998-Q1", "session.1998-Q2", "session.1998-Q3", "session.1998-Q4", "session.1999-Q1", "session.1999-Q2"]
    unique_users = {}
    unique_events = {}
    for filename in filenames:
        with open("clean_data/" + filename + ".cleaned", "r") as in_file, open("simple_data/" + filename + ".simple", "w") as out_file:
            for line in in_file:
                cur_line = line.split("\t")
                cur_line[-1] = cur_line[-1].strip("\n")
                #print(cur_line)
                user = cur_line[1]
                #have we seen this user before
                if user in unique_users:
                    #increase the num_interactions counter
                    unique_users[user][1] += 1
                else:
                    #create new user entry:
                    #   first element corresponds to the user_id
                    #   second element corresponds to the num_interactions
                    unique_users[user] = [len(unique_users), 0]

                #notice time and user are swapped to resemble the desired format for mining
                cur_line[0] = str(unique_users[user][0])
                cur_line[1] = str(unique_users[user][1])

                for i in range(2, len(cur_line)):
                    event = cur_line[i]
                    if event not in unique_events:
                        unique_events[event] = len(unique_events)
                    cur_line[i] = str(unique_events[event])

                out_file.write("\t".join(cur_line) + "\n")
                #print(cur_line)
                #input()
    #save the unique user info so we can translate back after mining
    with open("simple_data/user_data_key", "w") as data_key:
        for user in unique_users:
            data_key.write(user)
            data_key.write("\t")
            data_key.write(str(unique_users[user][0]))
            data_key.write("\t")
            data_key.write(str(unique_users[user][1]))
            data_key.write("\n")
    with open("simple_data/event_data_key", "w") as data_key:
        for event in unique_events:
            data_key.write(event)
            data_key.write("\t")
            data_key.write(str(unique_events[event]))
            data_key.write("\n")




if __name__ == "__main__":
    main()