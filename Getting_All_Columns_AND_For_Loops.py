# -*- coding: utf-8 -*-
"""
Gathers all columns in a data set. Not generic or a function yet. Will update in the future

By Jomel Manzano

"""

import pandas 

df = pandas.read_csv("COVID-19_Case_Surveillance_Public_Use_Data.csv")

f = open("data_summary_columns.txt", "w")

all_col = list(df)

length_col = len(all_col)

for x in range(length_col): # ALWAYS END FOR LOOPS WITH COLON
	print( all_col[x] )

###
#column_name = "race_ethnicity_combined"
f.write(all_col + '\n')     # header line for the name of the column 

for name,_ in df.groupby(all_col):  # use groupby to get the possible column values.
    print(name)
    f.write('\t' + name + "\n") # write the column value *indented* using \t, on its own line.
    
###

f.close()


####################

# For Loop Practice: Basic level

all_columns = ["qwerty", "asdf", "hello", "goodbye"]

for x in range(4):
	print( all_columns[x] )
###
