'''
See MicroDataTeachingVariables pdf for details
'''
from dataset import DataSet
from dataset import Column
from dataset import OptionEnum

import pandas as pd


NO_CODE_REQ = "No Code required"
NO_CODE_AWAY_STUDENT = "students or schoolchildren living away during term-time"
NO_CODE_SHORT_TERM_RES = "short-term resident"
NO_CODE_UNDER_16 = "people aged under 16"
NO_CODE_NOT_ENG_WALES = "not resident in England or Wales"
NO_CODE_NEVER_WORKED = "people who have never worked"
NO_CODE_NOT_WORKING = "people who are not working"
NO_CODE_COMMUNAL_RES = "people resident in a communal establishment"

# Creates a string combining all possible reasons
# that a particular cell does not have a code into
# a long human-readable string
def no_code_req(*reasons):
    s = "No code required"
    if len(reasons) == 0:
        return s
    reasons = list(reasons)
    reasons[0] = reasons[0].capitalize()
    reasons_str = ", ".join(reasons)
    return s + " (" + reasons_str + ")"



class RegionOptions(OptionEnum):
    NORTH_EAST    = ("E12000001", "North East")
    NORTH_WEST    = ("E12000002", "North West")
    YORKSHIRE     = ("E12000003", "Yorkshire and the Humber")
    EAST_MIDLANDS = ("E12000004", "East Midlands")
    WEST_MIDLANDS = ("E12000005", "West Midlands")
    EAST_ENGLAND  = ("E12000006", "East of England")
    LONDON        = ("E12000007", "London")
    SOUTH_EAST    = ("E12000008", "South East")
    SOUTH_WEST    = ("E12000009", "South West")
    WALES         = ("W92000004", "Wales")


class ResidenceOptions(OptionEnum):
    """What kind of residence they live in """
    COMMUNAL =     ("C", "Resident in a communal establishment")
    NOT_COMMUNAL = ("H", "Not resident in a communal establishment")


class FamilyCompositionOptions(OptionEnum):
    NOT_IN_FAMILY = (1, "Not in a family")
    MARRIED       = (2, "Married/same-sex civil partnership couple family")
    COHABITING    = (3, "Cohabiting couple family")
    LONE_FATHER   = (4, "Lone parent family (male head)")
    LONE_MOTHER   = (5, "Lone parent family (female head)")
    OTHER         = (6, "Other related family")
    NO_CODE       = (-9, no_code_req(NO_CODE_COMMUNAL_RES,
                                     NO_CODE_AWAY_STUDENT,
                                     NO_CODE_SHORT_TERM_RES))


class PopulationBaseOptions(OptionEnum):
    USUAL_RESIDENT      = (1, "Usual resident")
    STUDENT_AWAY        = (2, "Student living away from home during term-time")
    SHORT_TERM_RESIDENT = (3, "Short-term resident")


class SexOptions(OptionEnum):
    MALE   = (1, "Male")
    FEMALE = (2, "Female")


class AgeOptions(OptionEnum):
    UNDER_16      = (1, "0-15")
    FROM_16_TO_24 = (2, "16-24")
    FROM_25_TO_34 = (3, "25-34")
    FROM_35_TO_44 = (4, "35-44")
    FROM_45_TO_54 = (5, "45-54")
    FROM_55_TO_64 = (6, "55-64")
    FROM_65_TO_74 = (7, "65-74")
    OVER_75       = (8, "75+")


class MaritalStatusOptions(OptionEnum):
    SINGLE    = (1, "Single (never married or never registered in a "
                     "same-sex civil partnership)")
    MARRIED   = (2, "Married or in a registered same-sex civil partnership")
    SEPARATED = (3, "Separated but still legally marrried or seperated "
                    "but still legally in a same-sex civil partnership")
    DIVORCED  = (4, "Divorced or formely in a same-sex civil partnership "
                    "which is now legally dissolved")
    WIDOWED   = (5, "Widowed or surviving partner from a same-sex"
                    "civil partnership")


class StudentOptions(OptionEnum):
    YES = (1, "Yes")
    NO  = (2, "No")


class CountryOfBirthOptions(OptionEnum):
    UK      = (1, "UK")
    NON_UK  = (2, "Non UK")
    NO_CODE = (-9, no_code_req(NO_CODE_AWAY_STUDENT))

class HealthOptions(OptionEnum):
    VERY_GOOD = (1, "Very good health")
    GOOD      = (2, "Good health")
    FAIR      = (3, "Fair health")
    BAD       = (4, "Bad health")
    VERY_BAD  = (5, "Very bad health")
    NO_CODE   = (-9, no_code_req(NO_CODE_AWAY_STUDENT))


class EthnicityOptions(OptionEnum):
    WHITE   = (1, "White")
    MIXED   = (2, "Mixed")
    ASIAN   = (3, "Asian or Asian British")
    BLACK   = (4, "Black or Black British")
    OTHER   = (5, "Chinese or Other ethnic group")
    NO_CODE = (-9, no_code_req(NO_CODE_NOT_ENG_WALES, NO_CODE_AWAY_STUDENT))

class ReligionOptions(OptionEnum):
    NONE       = (1, "No religion")
    CHRISTIAN  = (2, "Christian")
    BUDDHIST   = (3, "Buddhist")
    HINDU      = (4, "Hindu")
    JEWISH     = (5, "Jewish")
    MUSLIM     = (6, "Muslim")
    SIKH       = (7, "Sikh")
    OTHER      = (8, "Other religion")
    NOT_STATED = (9, "Not stated")
    NO_CODE    = (-9, no_code_req(NO_CODE_NOT_ENG_WALES, NO_CODE_AWAY_STUDENT))

class EconomicActivityOptions(OptionEnum):
    EMPLOYEE          = (1, "Economically active: Employee")
    SELF_EMPLOYED     = (2, "Economically active: Self-employed")
    UNEMPLOYED        = (3, "Economically active: Unemployed")
    FULL_TIME_STUDENT = (4, "Economically active: Full-time student")
    RETIRED           = (5, "Economically inactive: Retired")
    STUDENT_INACTIVE  = (6, "Economically inactive: Student")
    CARING            = (7, "Economically inactive: Looking after home or family")
    SICK_OR_DISABLED  = (8, "Economically inactive: Long-term sick or disabled")
    OTHER             = (9, "Economically inactive: Other")
    NO_CODE           = (-9, no_code_req(NO_CODE_UNDER_16,
                                         NO_CODE_AWAY_STUDENT))


class OccupationOptions(OptionEnum):
    MANAGER                = (1, "Managers, Directors and Senior Officials")
    PROFESSIONAL           = (2, "Professional Occupations")
    ASSOCIATE_OR_TECHNICAL = (3, "Associate Professional and Technical Occupations")
    ADMINISTRATIVE         = (4, "Administrative and Secretarial Occupations")
    SKILLED_TRADES         = (5, "Skilled Trades Occupations")
    CARING_SERVICE         = (6, "Caring, Leisure and Other Service Occupations")
    SALES_SERVICE          = (7, "Sales and Customer Service Occupations")
    PLANT_OPERATIVE        = (8, "Process, Plant and Machine Operatives")
    ELEMENTARY             = (9, "Elementary Occupations")
    NO_CODE                = (-9, no_code_req(NO_CODE_UNDER_16,
                                              NO_CODE_NEVER_WORKED,
                                              NO_CODE_AWAY_STUDENT))

class IndustryOptions(OptionEnum):
    AGRICULTURE                 = (1, "Agriculture, forestry and fishing")
    ESSENTIALS                  = (2, "Mining and quarrying; Manufacturing; "
                                       "Electricity, gas, steam and air conditioning "
                                       "system; Water supply")
    CONSTRUCTION                = (3, "Construction")
    TRADE_AND_MOTOR             = (4, "Wholesale and retail trade; Repair of motor "
                                       "vehicles and motorcycles")
    ACCOMODATION_AND_FOOD       = (5, "Accomodation and food service activities")
    TRANSPORT_AND_COMMUNICATION = (6, "Transport and storage; "
                                       "Information and communication")
    FINANCIAL                   = (7, "Financial and insurance activities; Intermediation")
    REAL_ESTATE_TECHNICAL_ADMIN = (8, "Real estate activities; Professional, "
                                       "scientific and technical activities; "
                                       "Administrative and "
                                       "support service activities")
    EDUCATION                   = (9, "Education")
    HEALTH_AND_SOCIAL_WORK      = (10,"Human health and social work activities")
    PUBLIC_ADMIN_DEFENSE_SOCIAL = (11,"Public administration and defence; "
                                       "compulsory social security")
    OTHER                       = (12,"Other community, social and personal "
                                       "service activities; Private households "
                                       "employing domestic staff; Extra-territorial "
                                       "organisations and bodies")
    NO_CODE                     = (-9, no_code_req(NO_CODE_UNDER_16,
                                                   NO_CODE_NEVER_WORKED,
                                                   NO_CODE_AWAY_STUDENT))

class HoursWorkedPerWeekOptions(OptionEnum):
    PART_TIME_LOW  = (1, "Part-time: 15 or less hours worked")
    PART_TIME_HIGH = (2, "Part-time: 16 to 30 hours worked")
    FULL_TIME_LOW  = (3, "Full-time: 31 to 48 hours worked")
    FULL_TIME_HIGH = (4, "Full-time: 49 or more hours worked")
    NO_CODE        = (-9, no_code_req(NO_CODE_UNDER_16,
                                      NO_CODE_NOT_WORKING,
                                      NO_CODE_AWAY_STUDENT))

class SocialGradeOptions(OptionEnum):
    AB = (1, "AB")
    C1 = (2, "C1")
    C2 = (3, "C2")
    DE = (4, "DE")
    NO_CODE = (-9, no_code_req(NO_CODE_UNDER_16,
                               NO_CODE_COMMUNAL_RES,
                               NO_CODE_AWAY_STUDENT))


# map header to column values
colMap = {"Person ID" : Column(None, int), # set to None to allow any unique id, CHANGE ?
          "Region" : Column(RegionOptions, object),
          "Residence Type" : Column(ResidenceOptions, pd.StringDtype()),
          "Family Composition" : Column(FamilyCompositionOptions, int),
          "Population Base" : Column(PopulationBaseOptions, int),
          "Sex" : Column(SexOptions, int),
          "Age" : Column(AgeOptions, int),
          "Marital Status" : Column(MaritalStatusOptions, int),
          "Student": Column(StudentOptions, int),
          "Country of Birth" : Column(CountryOfBirthOptions, int),
          "Health" : Column(HealthOptions, int),
          "Ethnic Group" : Column(EthnicityOptions, int),
          "Religion" : Column(ReligionOptions, int),
          "Economic Activity" : Column(EconomicActivityOptions, int),
          "Occupation" : Column(OccupationOptions, int),
          "Industry" : Column(IndustryOptions, int),
          "Hours worked per week" : Column(HoursWorkedPerWeekOptions, int),
          "Approximated Social Grade" : Column(SocialGradeOptions, int)
          }

# contradictions
conts = [
    (AgeOptions.UNDER_16,   [MaritalStatusOptions.SINGLE,
                             SocialGradeOptions.NO_CODE,
                             HoursWorkedPerWeekOptions.NO_CODE,
                             IndustryOptions.NO_CODE,
                             OccupationOptions.NO_CODE,
                             EconomicActivityOptions.NO_CODE]),
    (PopulationBaseOptions.STUDENT_AWAY, [FamilyCompositionOptions.NO_CODE,
                                          CountryOfBirthOptions.NO_CODE,
                                          HealthOptions.NO_CODE,
                                          EthnicityOptions.NO_CODE,
                                          ReligionOptions.NO_CODE,
                                          EconomicActivityOptions.NO_CODE,
                                          OccupationOptions.NO_CODE,
                                          IndustryOptions.NO_CODE,
                                          HoursWorkedPerWeekOptions.NO_CODE,
                                          SocialGradeOptions.NO_CODE]),
    (HealthOptions.VERY_BAD,[EconomicActivityOptions.SICK_OR_DISABLED,
                             EconomicActivityOptions.RETIRED,
                             EconomicActivityOptions.STUDENT_INACTIVE,
                             EconomicActivityOptions.OTHER]),
    (StudentOptions.NO,     [CountryOfBirthOptions.UK,
                             CountryOfBirthOptions.NON_UK]),
    (StudentOptions.YES,    [EconomicActivityOptions.FULL_TIME_STUDENT,
                             EconomicActivityOptions.STUDENT_INACTIVE,
                             EconomicActivityOptions.NO_CODE]),
    (EconomicActivityOptions.RETIRED,    [HoursWorkedPerWeekOptions.NO_CODE]),
    (EconomicActivityOptions.UNEMPLOYED, [HoursWorkedPerWeekOptions.NO_CODE]),
    (ResidenceOptions.COMMUNAL, [FamilyCompositionOptions.NO_CODE,
                                  SocialGradeOptions.NO_CODE])
]

csvPath = "data/census2011.csv"

dataset = DataSet(csvPath, colMap, conts)

# compare economic activity to occupation, student status, etc. to find discrepancies
