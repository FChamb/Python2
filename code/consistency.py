#!/usr/bin/env python
'''
TO DO:
    - make shell script to run executable
    - remove contradictions
    - produce new file with refined data if any duplicates or contradictions are removed
'''
import os
import sys
from os import R_OK
import pandas as pd

from MicroDataTeachingVars import *

def main(csvPath):
    # https://stackoverflow.com/questions/32073498/check-if-file-is-readable-with-python-try-or-if-else
    # Might want to separate each error
    assert os.path.isfile(csvPath) and os.access(csvPath, R_OK), \
       f"File {csvPath} doesn't exist or isn't readable"

    df = pd.read_csv(csvPath)
    cleanDataFrame(df)

def cleanDataFrame(df):    
    # appropriate values
    if hasProblemValue(df):
        dropRows(df, findProblemRows(df))
    # appropriate types
    problemColumns = checkTypes(df)
    reTypeCols(df, problemColumns)

    # remove all the rows with duplicate ID values
    removeDupId(df)
    
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
    for col_name in df:
        print("Column:", col_name)
        col = colMap[col_name]
        if col.values is None:
            continue
        values_good = df[col_name].isin(col.values)
        bad_values = values_good[~values_good].index
        if len(bad_values) != 0:
            print("Discrepancies in column ", col_name, "-", bad_values)
            return list(bad_values)
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

# returns rows containing any duplicate ID's
def removeDupId(df):
    df["Person ID"].duplicated(keep=False)

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        main(sys.argv[1])
