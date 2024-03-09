'''
See MicroDataTeachingVariables pdf for details

TO DO:
Map values to descriptions/documentation of meanings
'''
import pandas as pd

csvPath = "data/census2011.csv"

# value options from pdf
regions = { "E12000001" : "North East",
            "E12000002" : "North West",
            "E12000003" : "Yorkshire and the Humber",
            "E12000004" : "East Midlands",
            "E12000005" : "West Midlands",
            "E12000006" : "East of England",
            "E12000007" : "London",
            "E12000008" : "South East",
            "E12000009" : "South West",
            "W92000004" : "Wales"}
residences = ["H","C"]
familyComp = [*range(1,7), -9]
popBase = [*range(1,4)]
sexes = [*range(1,3)]
ages = [*range(1,9)]
maritalStat = [*range(1,6)]
studying = [*range(1,3)] # Boolean ?
birthCountry = [*range(1,3), -9]
healthStat = [*range(1,6), -9]
ethnicity = [*range(1,6), -9]
religion = [*range(1,10), -9]
econAct = [*range(1,10), -9]
job = [*range(1,10), -9]
industry = [*range(1,13), -9]
hrs = [*range(1,5), -9]
socialGr = [*range(1,5), -9]

# class to represent column
class Column:
    def __init__(self, values, type):
        self.values = values
        self.type = type

# map header to column values
colMap = {"Person ID" : Column(None, int), # set to None to allow any unique id, CHANGE ?
          "Region" : Column(regions, object),
          "Residence Type" : Column(residences, pd.StringDtype()),
          "Family Composition" : Column(familyComp, int),
          "Population Base" : Column(popBase, int),
          "Sex" : Column(sexes, int),
          "Age" : Column(ages, int),
          "Marital Status" : Column(maritalStat, int),
          "Student": Column(studying, int),
          "Country of Birth" : Column(birthCountry, int),
          "Health" : Column(healthStat, int),
          "Ethnic Group" : Column(ethnicity, int),
          "Religion" : Column(religion, int),
          "Economic Activity" : Column(econAct, int),
          "Occupation" : Column(job, int),
          "Industry" : Column(industry, int),
          "Hours worked per week" : Column(hrs, int),
          "Approximated Social Grade" : Column(socialGr, int)
          }

# compare economic activity to occupation, student status, etc. to find discrepancies
