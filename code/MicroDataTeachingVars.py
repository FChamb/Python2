'''
See MicroDataTeachingVariables pdf for details

TO DO:
Map values to descriptions/documentation of meanings
'''
csvPath = "../data/census2011.csv/census2011.csv"

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
familyComp = [range(1,7), -9]
popBase = range(1,4)
sexes = range(1,3)
ages = range(1,9)
maritalStat = range(1,6)
studying = range(1,3) # Boolean ?
birthCountry = [range(1,3), -9]
healthStat = [range(1,6), -9]
ethnicity = [range(1,6), -9]
religion = [range(1,10), -9]
econAct = [range(1,10), -9]
job = [range[1,10], -9]
industry = [range(1,13), -9]
hrs = [range(1,5), -9]
socialGr = [range(1,5), -9]
