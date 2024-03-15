import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np

from mpl_toolkits import mplot3d
from statistics import getGroupTable

def main():
    df = pd.read_csv("../data/census2011-clean.csv")
    plotTable(getGroupTable(df, "Occupation", "Approximated Social Grade"))

def plotTable(df):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    for x, z in df.items():
        print("Plotting...", x[0], x[1], z)
        ax.scatter3D(x[0], x[1], z)
    plt.show()

if __name__ == "__main__":
    main()
