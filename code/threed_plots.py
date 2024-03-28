import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
import os

from stats import getGroupTable
from census_microdata_2011 import dataset
from ipywidgets import interact, Dropdown, IntSlider
from mpl_toolkits.mplot3d import Axes3D

imagesDir = 'images/3d/'

def main():
    df = pd.read_csv("data/census2011-clean.csv")
    print("Generating 3D scatter plots...")
    plotScatter(getGroupTable(df, "Region", "Industry"), "Region", "Industry")
    plotScatter(getGroupTable(df, "Occupation", "Approximated Social Grade"), "Occupation", "Approximated Social Grade")
    print("Done.")
    print("Generating 3D surface plots...")
    plotSurface(getGroupTable(df, "Region", "Industry"), "Region", "Industry")
    plotSurface(getGroupTable(df, "Occupation", "Approximated Social Grade"), "Occupation", "Approximated Social Grade")
    print("Done.")

def plotScatter(df, col1, col2):
    xs = dataset.get_column(col1).values
    ys = dataset.get_column(col2).values
    zs = df["counts"]

    @interact(region=Dropdown(options=xs), occupation=Dropdown(options=ys))
    def updatePlot(region, occupation):
        fig = plt.figure()
        # get values, plot points
        ax = plt.axes(111, projection='3d')
        # ax = Axes3D(fig)
        # plot individual points
        count = 0
        for x in range(len(xs)):
            for y in range(len(ys)):
                if count < len(zs):
                    ax.scatter(x, y, zs[count])
                    count+=1
                else:
                    break
        #ax.scatter(xs.index(region), ys.index(occupation), zs[(xs == region) & (ys == occupation)])
        plt.title("Records by " + col1 + " and " + col2)
        # labelling
        ax.set_xlabel(col1)
        ax.set_ylabel(col2)
        ax.set_zlabel("Count")
        ax.set(xticks=range(len(xs)), xticklabels = xs,
                yticks=range(len(ys)), yticklabels = ys)
        # save and show
        #plt.savefig(imagesDir + '3d-scatter-' + (col1 + '-' + col2).replace(' ', '-').lower() + '.png')
    plt.show()

def plotSurface(df, col1, col2):
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

    @interact(region=Dropdown(options=xlabels), occupation=Dropdown(options=ylabels))
    def update_plot(region, occupation):
        # generate plot
        plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot_trisurf(x, y, list(df["counts"]), cmap=cm.jet)
        # labelling
        ax.set_xlabel(col1)
        ax.set_ylabel(col2)
        ax.set_zlabel("Count")
        ax.set(xticks=range(len(xlabels)), xticklabels = xlabels,
                yticks=range(len(ylabels)), yticklabels = ylabels)
        # save and show
        #plt.savefig(imagesDir + '3d-surface-' + (col1 + '-' + col2).replace(' ', '-').lower() + '.png')
        plt.show()

if __name__ == "__main__":
    os.makedirs(imagesDir, exist_ok = True)
    main()
