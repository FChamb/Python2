import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np

from mpl_toolkits import mplot3d
from statistics import getGroupTable
from MicroDataTeachingVars import colMap

def main():
    df = pd.read_csv("../data/census2011-clean.csv")
    #plotTable(df, "Region", "Industry")
    plotTable(df, "Occupation", "Approximated Social Grade")

def plotTable(df, col1, col2):
    data = getGroupTable(df, col1, col2)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    for x, z in data.items():
        print("Plotting...", x[0], x[1], z)
        ax.scatter3D(x[0], x[1], z)
    plt.title("Records by "+col1+" and "+ col2)
    ax.set_xlabel(col1)
    ax.set_xticks(colMap.get(col1).values)
    ax.set_ylabel(col2)
    ax.set_yticks(colMap.get(col2).values)
    ax.set_zlabel("Count")
    plt.show()

if __name__ == "__main__":
    main()
