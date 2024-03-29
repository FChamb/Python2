import pandas
import timeit
import matplotlib.pyplot as plt

import census_microdata_2011 as md
import consistency


# WAYS OF VALIDATING
def iterate_df_in_values(df):
    """Naive way of validating through iteration"""
    invalid_columns = {}
    for column in df:
        invalid_rows = []
        invalid_columns[column] = invalid_rows
        col = md.colMap[column]
        if col.options is None:
            continue
        for i, cell in enumerate(df[column]):
            if cell not in col.values:
                invalid_rows.append(i)
    return invalid_columns

def cur_impl(df):
    """Our implementation: uses DataFrame.isin()"""
    consistency.findProblemRows(df)

# WAYS OF PARSING
def df_parse_by_apply(df):
    """Parse using DataFrame.apply()"""
    for column in df:
        col = md.colMap[column]
        if col.options is None:
            continue
        df[column].apply(col.options.parse)

def df_parse_dict(df):
    """Parse using DataFrame.replace()"""
    for column in df:
        col = md.colMap[column]
        if col.options is None:
            continue
        opts = {x.key(): x.desc() for x in col.options}
        df[column].replace(opts)

def profileWith(df):
    """Profile all methods with a given data frame"""
    results = {}
    print("Simple Iteration... ", flush=True, end="")
    results["iterate_df_in_values"] = profileMethod(lambda: iterate_df_in_values(df), 3)
    print("Current implementation... ", flush=True, end="")
    results["current_impl"] = profileMethod(lambda: cur_impl(df), 10)
    print("Parse df list... ", flush=True, end="")
    results["parse_by_apply"] = profileMethod(lambda: df_parse_by_apply(df), 3)
    print("Parse df dict... ", flush=True, end="")
    results["parse_dict"] = profileMethod(lambda: df_parse_dict(df), 10)
    print()
    return results

def profileMethod(f, number):
    """Profile a method, getting the average time taken to run each iteration"""
    return timeit.timeit(f, number=number) / number

def profileSize(df, size, cur):
    """Profile a given size dataframe"""
    print(f"{size} Rows: ", flush=True, end="")
    result = profileWith(df.head(size))
    for k,v in result.items():
        pair = (size, v)
        if k not in cur:
            cur[k] = [pair]
        else:
            cur[k].append(pair)

def plot_comparison(lines, title, filename, save):
    """Plot a line graph comparing the different methods"""
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel("DataFrame rows")
    ax.set_ylabel("Time taken (seconds)")
    for k, v in lines.items():
        size = [x[0] for x in v]
        times = [x[1] for x in v]
        ax.plot(size, times, label=k)
    ax.legend()
    if save:
        fig.savefig("images/performance/" + filename)
    print("Saved", filename)

def profile_and_plot(df, save=False):
    """Profile the various methods for a range of dataframe sizes"""

    if len(df) < 400000:
        print("Data set is not atleast 400000, this will mean graphs are incorrect")
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

    validate = {"Simple iteration": cur["iterate_df_in_values"], "Using panda's isin()": cur["current_impl"]}
    parse = {"Parse by .apply()": cur["parse_by_apply"],
             "Using dictionary and .replace()": cur["parse_dict"]}
    plot_comparison(validate, "Validation algorithm comparison", "validation.png", save)
    plot_comparison(parse, "Parsing algorithm comparison", "parse.png", save)
    print("== Validation Results ==")
    print_results(validate)
    print("== Parsing Results ==")
    print_results(parse)

def print_results(results):
    """Prin the benchmark results in a human readable format"""
    for k,v in results.items():
        print(f"{k}: ", end="")
        # Format to 5 significant digits
        line = ["({}: {:.5g})".format(x[0], x[1]) for x in v]
        print(", ".join(line))

if __name__ == "__main__":
    df = pandas.read_csv(md.csvPath)
    profile_and_plot(df, save=True)
