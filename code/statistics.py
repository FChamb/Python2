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
    print('-----------')
    t1 = getGroupTable(df, "Region", "Industry")
    print("Head of Region/Industry Table: \n", t1.head())
    t2 = getGroupTable(df, "Occupation", "Approximated Social Grade")
    print('-----------')
    print("Head of Occupation/Social Grade Table: \n", t2.head())

# basic req
def getNumRecords(df):
    return len(df.index)

# basic req
def getColTypes(df):
    return df.dtypes[1:] # [1:] removes header

# basic req
def getUniqueCounts(col):
    return col.value_counts()

# groupby req
def getGroupTable(df, col1, col2):
    df2 = df.groupby(col1)
    return df2[col2].value_counts()

if __name__ == "__main__":
    printSummary(pd.read_csv("../data/census2011-clean.csv"))