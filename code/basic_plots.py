import matplotlib as plt
import pandas as pd

from MicroDataTeachingVars import *

csvPath = 'data/census2011-clean.csv' #placeholder

''' TO DO:
        - implement plot functions
        - make executable to gen images in images subdir
'''

def main():
    df = pd.read_csv(csvPath)
    genRecordBarPlot(df, 'Region')
    genRecordBarPlot(df, 'Occupation')
    genDistPieChart(df, 'Age')
    genDistPieChart(df, 'Economic Activity')

def genRecordBarPlot(df, colName):

def genDistPieChart(df, colName):
