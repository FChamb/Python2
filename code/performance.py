import pandas
import timeit
import matplotlib.pyplot as plt

import MicroDataTeachingVars as md
import consistency


def iterate_df_in_values(df):
    invalid_columns = {}
    for column in df:
        invalid_rows = []
        invalid_columns[column] = invalid_rows
        col = md.colMap.get(column)
        if col.options is None:
            continue
        for i, cell in enumerate(df[column]):
            if cell not in col.values:
                invalid_rows.append(i)
    return invalid_columns

def cur_impl(df):
    consistency.findProblemRows(df)

def df_parse_by_iter(df):
    for column in df:
        col = md.colMap.get(column)
        if col.options is None:
            continue
        df[column].apply(col.options.parse)

def df_parse_dict(df):
    for column in df:
        col = md.colMap.get(column)
        if col.options is None:
            continue
        opts = {x.key(): x.desc() for x in col.options}
        df[column].replace(opts)


# https://stackoverflow.com/questions/5086430/how-to-pass-parameters-of-a-function-when-using-timeit-timer
def profileWith(df):
    results = {}
    NUMBER = 3
    print("== Iterate df in values ==")
    results["iterate_df_in_values"] = timeit.timeit(lambda: iterate_df_in_values(df), number=NUMBER)
    print("== Current implementation ==")
    results["current_impl"] = timeit.timeit(lambda: cur_impl(df), number=NUMBER)
    print("== Parse df list ==")
    results["parse_by_iter"] = timeit.timeit(lambda: df_parse_by_iter(df), number=NUMBER)
    print("== Parse df dict ==")
    results["parse_dict"] = timeit.timeit(lambda: df_parse_dict(df), number=NUMBER)
    return results

def profileSize(df, size, cur):
    print(f"-- {size} Rows --")
    result = profileWith(df.head(size))
    for k,v in result.items():
        pair = (size, v)
        if k not in cur:
            cur[k] = [pair]
        else:
            cur[k].append(pair)

def plot_comparison(lines, title, filename):
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel("DataFrame rows")
    ax.set_ylabel("Time taken (seconds)")
    for k, v in lines.items():
        size = [x[0] for x in v]
        times = [x[1] for x in v]
        ax.plot(size, times, label=k)
    ax.legend()
    fig.savefig("images/" + filename)
    print("Saved", filename)

if __name__ == "__main__":
    df = pandas.read_csv(md.csvPath)
    cur = {}
    profileSize(df, 10, cur)
    profileSize(df, 100, cur)
    profileSize(df, 500, cur)
    profileSize(df, 1000, cur)
    profileSize(df, 5000, cur)
    profileSize(df, 10000, cur)
    profileSize(df, 50000, cur)
    profileSize(df, 100000, cur)
    profileSize(df, 400000, cur)
    for k,v in cur.items():
        print(k, "->", v)
    validate = {"Simple iteration": cur["iterate_df_in_values"], "Using panda's isin()": cur["current_impl"]}
    parse = {"Parser by iteration": cur["parse_by_iter"], "Using dictionary and .replace()": cur["parse_dict"]}
    plot_comparison(validate, "Validation algorithm comparison", "validation_performance.png")
    plot_comparison(parse, "Parsing algorithm comparison", "parse_performance.png")

