import pandas as pd


def main():
    df = pd.read_csv("../data/census2011-clean.csv")
    query1 = find_economically_active_region(df)
    query2 = find_economically_active_region(df)
    print("Number of economically active people by region: ")
    print(query1)
    print("Number of economically active people by age: ")
    print(query2)


def find_economically_active_region(df):
    df = df[df["Economic Activity"] != -9]
    return df.groupby("Region")["Person ID"].count()


def find_economically_active_age(df):
    df = df[df["Economic Activity"] != -9]
    return df.groupby("Age")["Person ID"].count()


if __name__ == '__main__':
    main()
