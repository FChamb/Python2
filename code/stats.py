#!/usr/bin/env python
import pandas as pd
import sys

def printSummary(df):
    print("Number of Records: " + str(getNumRecords(df)))
    print("Column types-----------")
    print(str(getColTypes(df)))
    for col in df.columns[2:]: # skip indices and Person ID column
        print()
        print(getUniqueCounts(df[col]).transpose().to_string(header=False))
    print()

# basic req
def getNumRecords(df):
    return len(df.index)

# basic req
def getColTypes(df):
    return df.dtypes[1:] # [1:] removes header

# basic req
def getUniqueCounts(col):
    df = col.value_counts().reset_index()
    return df

# groupby req
def getGroupTable(df, col1, col2):
    df_c = df.groupby(col1)[col2].value_counts().reset_index() # group columns, count them
    df_c.columns = [col1, col2, "counts"] # rename columns
    return df_c

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Invalid arguments")
        print("Usage:", sys.argv[0], "<csvfile>")
        exit(1)
    try:
        printSummary(pd.read_csv(sys.argv[1]))
    except:
        print("Execution unsuccessful: error with file")
