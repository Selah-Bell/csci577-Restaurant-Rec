#this program counts the number of total data points, how many missing entry points, end points, and both
import os
import pandas as pd

def open_files():
	os.chdir('original_data')
	files = os.listdir('session')
	total_data_points = 0
	missing_start_point = 0
	missing_end_point = 0 
	missing_both = 0
	for file in files:
		if not file.startswith('R'):
			#print(file)
			#df = pd.read_csv("../originalData/session/"+file, sep='\t')
			#print(df[0])
			with open("../original_data/session/"+file, "r") as f:
				for line in f:
					total_data_points += 1
					line_list = line.split('\t')
					#print(line_list[-1])
					if line_list[2].strip() == '0':
						#print(line_list[2])
						missing_start_point += 1
					if line_list[-1].strip() == '-1':
						missing_end_point += 1
					if  line_list[2].strip() == '0' and line_list[-1].strip() == '-1':
						missing_both += 1

	print("Total Data Points: "+str(total_data_points))
	print("Missing Entry Points: "+str(missing_start_point))
	print("Missing End Points: "+str(missing_end_point))
	print("Missing Both: "+str(missing_both))
def main():
	open_files()
    

if __name__ == "__main__":
	main()
