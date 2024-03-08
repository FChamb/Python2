'''
First 3 basic requirements
1. Check the consistency of the initial (raw) data.
2. Output refined data for further analysis, fixing any encountered inconsistencies.
3. Provide an executable Python script to automate the two steps above.

– develop a procedure to check that the data match expected format, remove duplicates, and
perform further refinement. This procedure should check that:
    1. the file exists and is readable as expected;
    2. the values of variables are of the expected format (numbers, strings, etc.);
    3. the values of variables are admissible (e.g. are within a given range or are from the list
    of admissible values);
    4. there are no logical contradictions in the data.
– in case of any inconsistencies and/or duplicates found, produce new file with refined data
to be used in the subsequent analysis (doing the checks is important, event if the data will
not have instances of all problems you might anticipate)
– this step must be automated to the point when it can be run with a single shell command to
call an executable Python script specifying necessary arguments
'''
import os
from os import R_OK
import pandas as pd

from MicroDataTeachingVars import *

def main():
    # https://stackoverflow.com/questions/32073498/check-if-file-is-readable-with-python-try-or-if-else
    # Might want to separate each error
    assert os.path.isfile(csvPath) and os.access(csvPath, R_OK), \
       f"File {csvPath} doesn't exist or isn't readable"

    df = pd.read_csv(csvPath)
    cleanDataFrame(df)

def cleanDataFrame(df):    
    # appropriate values
    if hasProblemValue(df):
        dropRows(findProblemRows(df))
    # appropriate types
    problemColumns = checkTypes(df)
    reTypeCols(df, problemColumns)

    # TO DO: check for duplicate IDs
    
    # TO DO: find contradictions ?
    return df

# given a list of indices, deletes the rows at those indices in the dataframe
def dropRows(df, rows):
    print("Dropping rows", rows, "...")
    for index in rows:
        print("Dropping row at",index)
        df.drop(index)
    print("Row removal finished.")

# retypes the given columns in the given dataframe with their expected type
def reTypeCols(df, cols):
    print("Retyping columns", cols, "...")
    for col in cols:
        print("Retyping",col,"from",type(col), "to", colMap.get(col).type)
        df[col] = df[col].astype(colMap.get(col).type)
    print("Retyping finished")

# returns a list of columns that are incorrectly typed
def checkTypes(df):
    print("Checking types...")
    problems = []
    for column in df:
        if not df[column].dtype == colMap.get(column).type:
            print("Discrepancy of type in column ", column, "expected", colMap.get(column).type, "found", df[column].dtype)
            problems.append(column)
    print("Type checking finished.")
    return problems

# returns a list of indices of rows where there is an invalid value
def findProblemRows(df):
    print("Finding rows with problem values...")
    problems = []
    for index, row, in df.iterrows():
        for col in df:
            if colMap.get(col).values is not None and not df[col][index] in colMap.get(col).values:
                #colValidity(df[col][index], colMap.get(col).values):
                print("Discrepancy of value in row ", index, "column", col)
                problems.append(index)
    print("Problem finding finished.")
    return problems

# returns true if an invalid value is found in a given dataframe
def hasProblemValue(df):
    print("Checking for problem values...")
    isValid = False
    for column in df:
        if not colValidity(df[column], colMap.get(column).values):
            print("Discrepancy of value in column ", column)
            isValid = True
    print("Value checking finished.")
    return isValid

# returns true if given column only contains values in given value set
def colValidity(column, values):
    return values == None or column.isin(values).all()

if __name__ == "__main__":
    main()
