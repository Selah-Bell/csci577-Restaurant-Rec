import os
import pandas as pd

def open_files():
	os.chdir('..')
	files = os.listdir('session') 
	for file in files:
		if not file.startswith('R'):
			df = pd.read_csv(file, sep='\t')
			print(df[0])
				 
def main():
	open_files()
    

if __name__ == "__main__":
	main()
