#This program goes through the entree dataset and removes undesired entries.

#An undesired entry is one that has a -1 for the end point

def main():
    filenames = ["session.1996-Q3", "session.1996-Q4", "session.1997-Q1", "session.1997-Q2", "session.1997-Q3", "session.1997-Q4", "session.1998-Q1", "session.1998-Q2", "session.1998-Q3", "session.1998-Q4", "session.1999-Q1", "session.1999-Q2"]
    for filename in filenames:
        with open("original_data/session/" + filename, "r") as in_file, open("clean_data/" + filename + ".cleaned", "w") as out_file:
            for line in in_file:
                cur_line = line.split("\t")
                cur_line[-1] = cur_line[-1].strip("\n")

                if cur_line[-1] != "-1":
                    out_file.write(line)

if __name__ == "__main__":
    main()