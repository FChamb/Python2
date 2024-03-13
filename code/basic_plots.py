import matplotlib.pyplot as plt
import pandas as pd

from MicroDataTeachingVars import *

csvPath = '../data/census2011-clean.csv' #placeholder

''' TO DO:
        - add legend to bar plot
        - make executable to gen images in images subdir
        - executable should take filepath or dataframe AND some value for colMap
'''

def main():
    df = pd.read_csv(csvPath)
    #genRecordBarPlot(df, 't')
    #genRecordBarPlot(df, 'Occupation')
    genDistPieChart(df, 'Age')
    genDistPieChart(df, 'Economic Activity')

def genRecordBarPlot(df, colName):
    if colMap.get(colName) is not None:
        values = [str(x) for x in colMap.get(colName).values] # gets options as strings
        # refer to for legend stuff
        # https://stackoverflow.com/questions/62941033/how-to-turn-x-axis-values-into-a-legend-for-matplotlib-bar-graph 
        f, ax = plt.subplots()
        ax.bar(values, df[colName].value_counts()) # plot options w/ their frequencies
        
        plt.title("Number of records for each " + colName.lower())
        plt.xlabel(colName)
        plt.xticks(values)
        plt.ylabel("Number of Records")
        # create legend w/ keys and descriptions
        legend = '\n'.join(f'{x.key()} - {x.desc()}' for x in colMap.get(colName).options)
        # TO DO: ADD LEGEND SOMEHOW
        plt.show()
    else:
        raise ValueError(colName+" is an invalid column")

def genDistPieChart(df, colName):
    if colMap.get(colName) is not None:
        plt.pie(df[colName].value_counts(), labels = colMap.get(colName).options)
        plt.title("Distribution of sample by " + colName.lower())
        plt.show()
    else:
        raise ValueError(colName+" is an invalid column")

if __name__ == "__main__":
    main()