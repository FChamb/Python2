import sys
import os
import pandas as pd
from os import R_OK


def main(csvPath):
    assert os.path.isfile(csvPath) and os.access(csvPath, R_OK), \
        f"File {csvPath} does not exist or is not readable"

    df = pd.read_csv(csvPath)
    findQueries(df)
    discrepancies = findDiscrepancies(df)
    print("Discrepancies found between student status and economic activity: ")
    print(discrepancies)

    hours = findWorkingHours(df)
    print("Working hours found per week for students: ")
    print(hours)

def findWorkingHours(df):
    hours = df[(df["Economic Activity"].isin([4, 6])) & df["Student"] == 1]["Hours worked per week"].sum()
    return hours

def findQueries(df):
    query1 = find_economically_active_region(df)
    query2 = find_economically_active_region(df)
    print("Number of economically active people by region: ")
    print(query1)
    print("Number of economically active people by age: ")
    print(query2)

def findDiscrepancies(df):
    ret = df[df["Student"] == 1]["Economic Activity"].value_counts()
    return ret

def find_economically_active_region(df):
    df = df[df["Economic Activity"] != -9]
    return df.groupby("Region")["Person ID"].count()


def find_economically_active_age(df):
    df = df[df["Economic Activity"] != -9]
    return df.groupby("Age")["Person ID"].count()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid arguments")
        print("Usage:", sys.argv[0], "<csvPath>")
        exit(1)
    main(sys.argv[1])
