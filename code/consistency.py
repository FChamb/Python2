#!/usr/bin/env python
import os
import sys
from os import R_OK
import pandas as pd

import census_microdata_2011 as md

def main(csvPath):
    assert os.path.isfile(csvPath) and os.access(csvPath, R_OK), \
       f"File {csvPath} doesn't exist or isn't readable"

    cleanPath = "data/census2011-clean.csv"
    df = pd.read_csv(csvPath)
    df = cleanDataFrame(df)
    df.to_csv(cleanPath, index=False)

def cleanDataFrame(df):    
    # appropriate values
    if hasProblemValue(df):
        print("Finding rows with problem values...")
        problemRows = findProblemRows(df)
        print("Problem finding finished.")
        dropRows(df, findProblemRows(df))
    # appropriate types
    problemColumns = checkTypes(df)
    reTypeCols(df, problemColumns)

    removeDupId(df)
    findContradictions(df)

    return df

def findContradictions(df):
    bad_rows = []
    for (req, thens) in md.dataset.get_contradictions():
        colName = md.dataset.get_column_name(req.__class__)
        print(f">> Checking {colName} == {req}")
        candidates = df.loc[df[colName] == req.key()]
        # Transform array into dictionary of column name to permitted values
        contDict = {}
        for t in thens:
            tColName = md.dataset.get_column_name(t.__class__)
            if tColName not in contDict:
                contDict[tColName] = []
            contDict[tColName].append(t)
        #print("Dict: " + str(contDict))
        for targetColName, permitted in contDict.items():
            print(f"Requirement:", permitted, "- ", end="")
            permitted_values = [x.key() for x in permitted]
            values_good = candidates[targetColName].isin(permitted_values)
            #print(values_good)
            values_bad = values_good[~values_good]
            if len(values_bad) != 0:
                print("CONTRADICTION")
                #print(values_bad)
                bad_df = candidates.loc[~values_good].copy()
                colNameDesc = colName + " DESC"
                targetColNameDesc = targetColName + " DESC"
                show_columns = [colName, colNameDesc, targetColName, targetColNameDesc]
                bad_df[colNameDesc] = bad_df[colName].replace(req.mappings)
                bad_df[targetColNameDesc] = bad_df[targetColName].replace(permitted[0].mappings)
                print(bad_df[show_columns])
                bad_rows = bad_rows + list(values_bad)
            else:
                print("HOLDS")
    return bad_rows

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
        print("Retyping",col,"from",type(col), "to", md.dataset.get_column(col).type)
        df[col] = df[col].astype(md.dataset.get_column(col).type)
    print("Retyping finished")

# returns a list of columns that are incorrectly typed
def checkTypes(df):
    print("Checking types...")
    problems = []
    for column in df:
        if not df[column].dtype == md.dataset.get_column(column).type:
            print("Discrepancy of type in column ", column, "expected", md.dataset.get_column(column).type, "found", df[column].dtype)
            problems.append(column)
    print("Type checking finished.")
    return problems

# returns a list of indices of rows where there is an invalid value
def findProblemRows(df):
    problems = []
    for col_name in df:
        col = md.dataset.get_column(col_name)
        if col.values is None:
            continue
        values_good = df[col_name].isin(col.values)
        bad_values = values_good[~values_good].index
        if len(bad_values) != 0:
            print("Discrepancies in column ", col_name, "-", bad_values)
            return list(bad_values)
    return problems

# returns true if an invalid value is found in a given dataframe
def hasProblemValue(df):
    print("Checking for problem values...")
    isValid = False
    for column in df:
        if not colValidity(df[column], md.dataset.get_column(column).values):
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
    if (len(sys.argv) != 2):
        print("Invalid arguments")
        print("Usage:", sys.argv[0], "<csvfile>")
        exit(1)
    main(sys.argv[1])
