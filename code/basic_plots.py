#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys

from IPython.core.display_functions import display

from census_microdata_2011 import dataset
from cycler import cycler
from ipywidgets import interact, Dropdown, IntSlider, fixed, widgets, Output

imagesDir = 'images/basics/'

def main(csvPath):
    df = pd.read_csv(csvPath)
    os.makedirs(imagesDir, exist_ok=True)
    print("Generating basic requirement plots...")
    out1 = Output()
    out2 = Output()
    out3 = Output()
    out4 = Output()

    interact(genRecordBarPlot, df=fixed(df), colName=Dropdown(options=df.columns, value='Region'), save=fixed(True), _output=out1)
    interact(genRecordBarPlot, df=fixed(df), colName=Dropdown(options=df.columns, value='Occupation'), save=fixed(True), _output=out2)
    interact(genDistPieChart, df=fixed(df), colName=Dropdown(options=df.columns, value='Age'), save=fixed(True), _output=out3)
    interact(genDistPieChart, df=fixed(df), colName=Dropdown(options=df.columns, value='Economic Activity'), save=fixed(True), _output=out4)

    display(out1)
    display(out2)
    display(out3)
    display(out4)
    print("Done.")

def genRecordBarPlot(df, colName, save):
    if dataset.get_column(colName) is not None:
        # gets options as strings
        values = [str(x) for x in dataset.get_column(colName).values]
        # plot options w/ their frequencies
        plt.figure()
        # f, ax = plt.subplots()
        bars = plt.bar(values, df[colName].value_counts(), label=values)
        # title + y axis
        plt.title("Number of records for each " + colName.lower())
        plt.ylabel("Number of Records")
        # x axis
        plt.xlabel(colName)
        plt.xticks(values)
        if len(values[0]) > 1: # if vals too long, tilt
            plt.setp(plt.gca().get_xticklabels(), rotation=30, horizontalalignment='right')
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
        plt.figure()
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
