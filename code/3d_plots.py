import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
import numpy as np
import os

from stats import getGroupTable
from census_microdata_2011 import dataset

imagesDir = 'images/3d/'

def main():
    df = pd.read_csv("data/census2011-clean.csv")
    plotScatter(getGroupTable(df, "Region", "Industry"), "Region", "Industry")
    plotScatter(getGroupTable(df, "Occupation", "Approximated Social Grade"), "Occupation", "Approximated Social Grade")
    plotContour(getGroupTable(df, "Region", "Industry"), "Region", "Industry")
    plotContour(getGroupTable(df, "Occupation", "Approximated Social Grade"), "Occupation", "Approximated Social Grade")

# https://stackoverflow.com/questions/54113067/3d-scatterplot-with-strings-in-python 
def plotScatter(df, col1, col2):
    plt.figure()
    ax = plt.axes(111, projection='3d')
    # get values
    xs = dataset.get_column(col1).values
    ys = dataset.get_column(col2).values
    zs = df["counts"]
    # plot individual points
    count = 0
    for x in range(len(xs)):
        for y in range(len(ys)):
            ax.scatter(x, y, zs[count])
            count+=1
    # labelling
    plt.title("Records by "+col1+" and "+ col2)
    ax.set_xlabel(col1)
    ax.set_ylabel(col2)
    ax.set(xticks=range(len(xs)), xticklabels = xs,
           yticks=range(len(ys)), yticklabels = ys)
    ax.set_zlabel("Count")
    # save and show
    plt.savefig(imagesDir+'3d-scatter-'+(col1 + '-' + col2).replace(' ', '-').lower()+'.png')
    plt.show()

#https://stackoverflow.com/questions/9170838/surface-plots-in-matplotlib
def plotContour(df, col1, col2):
    # get values
    xlabels = dataset.get_column(col1).values
    ylabels = dataset.get_column(col2).values
    area = len(xlabels) * len(ylabels)
    x = [None] * area
    y = [None] * area
    index = 0
    # assign x values
    for i in range(len(ylabels)):
        for val in range(len(xlabels)):
            x[index] = val
            index += 1
    # assign y values
    index = 0
    for i in range(len(xlabels)):
        for val in range(len(ylabels)):
            y[index] = val
            index += 1
    # generate plot
    plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_trisurf(x, y, list(df["counts"]),cmap =cm.viridis)
    # labelling
    ax.set_xlabel(col1)
    ax.set_ylabel(col2)
    ax.set(xticks=range(len(xlabels)), xticklabels = xlabels,
           yticks=range(len(ylabels)), yticklabels = ylabels)
    ax.set_zlabel("Count") 
    # save and show
    plt.savefig(imagesDir+'3d-surface-'+(col1 + '-' + col2).replace(' ', '-').lower()+'.png')
    plt.show()

if __name__ == "__main__":
    os.makedirs(imagesDir, exist_ok = True)
    main()
