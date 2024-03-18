import matplotlib.pyplot as plt
import pandas as pd
import os

from mpl_toolkits import mplot3d
from stats import getGroupTable
from MicroDataTeachingVars import colMap

imagesDir = '../images/3d/'

def main():
    df = pd.read_csv("../data/census2011-clean.csv")
    plotTable(getGroupTable(df, "Region", "Industry"), "Region", "Industry")
    plotTable(getGroupTable(df, "Occupation", "Approximated Social Grade"), "Occupation", "Approximated Social Grade")

def plotTable(df, col1, col2):
    data = getGroupTable(df, col1, col2)
    fig = plt.figure()
    ax = plt.axes(111, projection='3d')
    xs = df[col1]
    xlabels = colMap.get(col1).values
    ys = df[col2]
    ylabels = colMap.get(col2).values
    zs = df["counts"]
    # https://stackoverflow.com/questions/54113067/3d-scatterplot-with-strings-in-python 
    count = 0
    for x in range(len(xlabels)):
        for y in range(len(ylabels)):
            ax.scatter(x, y, zs[count])
            count+=1
    plt.title("Records by "+col1+" and "+ col2)
    ax.set_ylabel(col2)
    ax.set(xticks=range(len(xlabels)), xticklabels = xlabels,
           yticks=range(len(ylabels)), yticklabels = ylabels)
    ax.set_zlabel("Count")
    plt.savefig(imagesDir+'3d-'+(col1 + '-' + col2).replace(' ', '-').lower()+'.png')
    plt.show()

if __name__ == "__main__":
    os.makedirs(imagesDir, exist_ok = True)
    main()
