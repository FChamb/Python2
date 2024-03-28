#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys

from census_microdata_2011 import dataset
from cycler import cycler
from ipywidgets import interact, Dropdown, IntSlider, fixed

imagesDir = 'images/basics/'

def main(csvPath):
    df = pd.read_csv(csvPath)
    os.makedirs(imagesDir, exist_ok=True)
    print("Generating basic requirement plots...")
    interact(genRecordBarPlot(df, 'Region', True), df=fixed(df), colName=Dropdown(options=df.columns))
    interact(genRecordBarPlot(df, 'Occupation', True), df=fixed(df), colName=Dropdown(options=df.columns))
    interact(genDistPieChart(df, 'Age', True), df=fixed(df), colName=Dropdown(options=df.columns))
    interact(genDistPieChart(df, 'Economic Activity', True), df=fixed(df), colName=Dropdown(options=df.columns))
    print("Done.")

def genRecordBarPlot(df, colName, save):
    if dataset.get_column(colName) is not None:
        # gets options as strings
        values = [str(x) for x in dataset.get_column(colName).values]
        # plot options w/ their frequencies
        f, ax = plt.subplots()
        bars = ax.bar(values, df[colName].value_counts(),label=values)
        # title + y axis
        plt.title("Number of records for each " + colName.lower())
        plt.ylabel("Number of Records")
        # x axis
        plt.xlabel(colName)
        plt.xticks(values)
        if len(values[0]) > 1: # if vals too long, tilt
            plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
        # create legend w/ keys and descriptions
        plt.legend(labels=getLegend(colName),loc='upper right')
        # save and close
        if save:
            plt.savefig(imagesDir+'barchart-'+colName.replace(' ', '-').lower()+'.png', bbox_inches="tight")
        else:
            plt.show()
        #plt.close()
    else:
        raise ValueError(colName+" is an invalid column")

def genDistPieChart(df, colName, save):
    if dataset.get_column(colName) is not None:
        plt.pie(df[colName].value_counts(), labels = dataset.get_column(colName).options) # plot w labels
        plt.title("Distribution of sample by " + colName.lower()) # name
        # save and close
        if save:
            plt.savefig(imagesDir+'piechart-'+colName.replace(' ', '-').lower()+'.png', bbox_inches="tight")
        else:
            plt.show()
        #plt.close()
    else:
        raise ValueError(colName+" is an invalid column")

def getLegend(colName):
    return [f'{x.key()} - {x.desc().split("(")[0]}' for x in dataset.get_column(colName).options]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments")
        print("Usage:", sys.argv[0], "<csvPath>")
        exit(1)
    main(sys.argv[1])
