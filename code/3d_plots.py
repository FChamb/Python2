import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

from mpl_toolkits import mplot3d
from stats import getGroupTable
from census_microdata_2011 import dataset

imagesDir = '../images/3d/'

def main():
    df = pd.read_csv("../data/census2011-clean.csv")
    plotScatter(getGroupTable(df, "Region", "Industry"), "Region", "Industry")
    plotScatter(getGroupTable(df, "Occupation", "Approximated Social Grade"), "Occupation", "Approximated Social Grade")
    #plotContour(getGroupTable(df, "Region", "Industry"), "Region", "Industry")
    #plotContour(getGroupTable(df, "Occupation", "Approximated Social Grade"), "Occupation", "Approximated Social Grade")

# https://stackoverflow.com/questions/54113067/3d-scatterplot-with-strings-in-python 
def plotScatter(df, col1, col2):
    fig = plt.figure()
    ax = plt.axes(111, projection='3d')
    # get values
    xs = df[col1]
    xlabels = dataset.get_column(col1).values
    ys = df[col2]
    ylabels = dataset.get_column(col2).values
    zs = df["counts"]
    # plot individual points
    count = 0
    for x in range(len(xlabels)):
        for y in range(len(ylabels)):
            ax.scatter(x, y, zs[count])
            count+=1
    # labelling
    plt.title("Records by "+col1+" and "+ col2)
    ax.set_xlabel(col1)
    ax.set_ylabel(col2)
    ax.set(xticks=range(len(xlabels)), xticklabels = xlabels,
           yticks=range(len(ylabels)), yticklabels = ylabels)
    ax.set_zlabel("Count")
    plt.savefig(imagesDir+'3d-'+(col1 + '-' + col2).replace(' ', '-').lower()+'.png')
    plt.show()

def plotContour(df, col1, col2):
    xlabels = colMap.get(col1).values
    ylabels = colMap.get(col2).values
    xs = np.array(0, len(xlabels))
    x = np.eye(len(xlabels)).reshape(len(xlabels),len(ylabels))
    print("x: ", x)
    y = np.linspace(0, len(ylabels)).reshape(len(xlabels),len(ylabels))
    print("y: ", y)
    z = np.array(df["counts"]).reshape(len(xlabels),len(ylabels))

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(x,y,z)

    ax.set_xlabel(col1)
    ax.set_ylabel(col2)
    ax.set(xticks=range(len(xlabels)), xticklabels = xlabels,
           yticks=range(len(ylabels)), yticklabels = ylabels)
    ax.set_zlabel("Count")

    plt.show()

if __name__ == "__main__":
    os.makedirs(imagesDir, exist_ok = True)
    main()
