import sys
import os
import pandas as pd
from os import R_OK


def main(csvPath):
    assert os.path.isfile(csvPath) and os.access(csvPath, R_OK), \
        f"File {csvPath} does not exist or is not readable"

    df = pd.read_csv(csvPath)
    findQueries(df)


def findWorkingHours(df):
    map_hours = {
        1: 10,
        2: 23,
        3: 40,
        4: 50,
        -9: 0
    }
    hours = df[(df["Economic Activity"].isin([4, 6])) & df["Student"] == 1]["Hours worked per week"].replace(map_hours).sum()
    return hours


def findQueries(df):
    query1 = find_economically_active_region(df)
    query2 = find_economically_active_region(df)
    discrepancies = findDiscrepancies(df)
    hours = findWorkingHours(df)

    print("Number of economically active people by region: ")
    print(query1)
    print()

    print("Number of economically active people by age: ")
    print(query2)
    print()

    print("Discrepancies found between student status and economic activity: ")
    print(discrepancies)
    print()

    print("Working hours found per week for students: ")
    print(hours)
    print()


def findDiscrepancies(df):
    ret = df[df["Student"] == 1]["Economic Activity"].value_counts()
    return ret


def find_economically_active_region(df):
    df = df[df["Economic Activity"] != -9]
    return df.groupby("Region")["Person ID"].count()


def find_economically_active_age(df):
    df = df[df["Economic Activity"] != -9]
    return df.groupby("Age")["Person ID"].count()

# Find the results to query 1
def find_query1(df):
    query1 = find_economically_active_region(df)
    print("Number of economically active people by region: ")
    print(query1)
    print()
    return query1

# Find the results to query 2
def find_query2(df):
    query2 = find_economically_active_region(df)
    print("Number of economically active people by age: ")
    print(query2)
    print()

# Find the results to discrepancies
def find_discrepancies(df):
    discrepancies = findDiscrepancies(df)
    print("Discrepancies found between student status and economic activity: ")
    print(discrepancies)
    print()

# Find the results to hours
def find_hours(df):
    hours = findWorkingHours(df)
    print("Working hours found per week for students: ")
    print(hours)
    print()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid arguments")
        print("Usage:", sys.argv[0], "<csvPath>")
        exit(1)
    main(sys.argv[1])
