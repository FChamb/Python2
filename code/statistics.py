import pandas as pd

'''
TO DO: - Implement getNumUniques
       - Implement getNumOccurences
'''

def printSummary(df):
    print("Number of Records: " + str(getNumRecords(df)))
    print("Column types\n-----------")
    print(str(getColTypes(df)))

def getNumRecords(df):
    return len(df.index)

def getColTypes(df):
    return df.dtypes[1:] # [1:] removes header

#def getNumUniques(col):

#def getNumOccurences(col):
    
if __name__ == "__main__":
    printSummary(pd.read_csv("../data/census2011-clean.csv"))