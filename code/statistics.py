import pandas as pd

'''
TO DO: - Implement getNumUniques
       - Implement getNumOccurences
'''

def printSummary(df):
    print("Number of Records: " + str(getNumRecords(df)))
    print("Column types-----------")
    print(str(getColTypes(df)))
    for col in df.columns[2:]: # skip indices and Person ID column
        print('-----------')
        print(str(getUniqueCounts(df[col])))

def getNumRecords(df):
    return len(df.index)

def getColTypes(df):
    return df.dtypes[1:] # [1:] removes header

def getUniqueCounts(col):
    return col.value_counts()

if __name__ == "__main__":
    printSummary(pd.read_csv("../data/census2011-clean.csv"))