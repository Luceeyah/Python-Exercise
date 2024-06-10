import pandas as pd

# # Read the .dat file into a DataFrame
# df = pd.read_csv('chf01.dat', sep='\s+', encoding='latin-1')  # Assuming tab-separated values

# # Write the DataFrame to a .csv file
# df.to_csv('chf01.csv', index=False)


import pickle

import textfile as textfile

# textfile = open("file.txt" , "w")
binary_file = open("chf01.dat" ,  "rb")

while  not (binary_file.eof()):
   textfile.write(str(pickle.load(binary_file) + "/n"))


textfile.close()
binary_file.close()