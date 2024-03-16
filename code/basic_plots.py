#!/usr/bin/env python
import matplotlib.pyplot as plt
import pandas as pd

from MicroDataTeachingVars import colMap

from cycler import cycler

csvPath = '../data/census2011-clean.csv' #placeholder
imagesDir = '../images/'

def main():
    df = pd.read_csv(csvPath)
    print("Generating basic requirement plots...")
    genRecordBarPlot(df, 'Region')
    genRecordBarPlot(df, 'Occupation')
    genDistPieChart(df, 'Age')
    genDistPieChart(df, 'Economic Activity')
    print("Done.")

def genRecordBarPlot(df, colName):
    if colMap.get(colName) is not None:
        # gets options as strings
        values = [str(x) for x in colMap.get(colName).values]
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
        legend = [f'{x.key()} - {x.desc().split("(")[0]}' for x in colMap.get(colName).options]
        plt.legend(labels=legend,loc='upper right')
        # save and close
        plt.savefig(imagesDir+'barchart-'+colName.replace(' ', '-').lower()+'.png', bbox_inches="tight")
        plt.close()
    else:
        raise ValueError(colName+" is an invalid column")

def genDistPieChart(df, colName):
    if colMap.get(colName) is not None:
        plt.pie(df[colName].value_counts(), labels = colMap.get(colName).options) # plot w labels
        plt.title("Distribution of sample by " + colName.lower()) # name
        # save and close
        plt.savefig(imagesDir+'piechart-'+colName.replace(' ', '-').lower()+'.png', bbox_inches="tight") 
        plt.close()
    else:
        raise ValueError(colName+" is an invalid column")

if __name__ == "__main__":
    main()
