import pandas as pd
import numpy as np



# loop through all csv files and incrementally add to the df
# input the inital month and year for csv file and input the name of the final file
yr = "2016"
mo = "04"
end_file = "201702.csv"

# initialize the first df file
file = yr + mo +".csv"
df = pd.read_csv(file)

while(True):
	# increment the month count	
	mo +=

	# break if file is end file
	if file == end_file:
		break

	# loop month back to 1 and year to next year if month count is 13
	if mo == 13:
		yr += 
		mo = 01

	# read csv into temporary df
	file = yr + mo +".csv"
	df_init = pd.read_csv(file)

	# add the temporary df to the key df
	df = pd.concat([df, df_init])

df.to_csv('Until%s_merged.csv' %end_file)
