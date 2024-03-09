'''
See MicroDataTeachingVariables pdf for details

TO DO:
Map values to descriptions/documentation of meanings
'''
import pandas as pd
from enum import Enum
from enum import IntEnum

csvPath = "data/census2011.csv"

class OptionEnum(Enum):
    @classmethod
    def parse(cls, encoded):
        """Parses the encoded key into a enum variant"""
        for m in cls:
            if encoded == m.value[0]:
                return m
        raise KeyError(str(encoded) + " is not a valid key for " + str(cls))

    @classmethod
    def keys(cls):
        """Returns a list of the valid keys for this option"""
        return [m.value[0] for m in cls]

    def __str__(self):
        """Returns a human readable description of what this enum signified"""
        return self.value[1]

    def __repr__(self):
        """Returns a representation of this enum with both value and type information"""
        return f"<{self.__class__.__name__}: {self.value[1]}>" 


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
    NO_CODE       = (-9,"No code required (Resident of communal establishment, \
                         students or schoolchildren living away during \
                         term-time, or a short-term resident")


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
    SINGLE    = (1, "Single (never married or never registered in a \
                     same-sex civil partnership)")
    MARRIED   = (2, "Married or in a registered same-sex civil partnership")
    SEPARATED = (3, "Separated but still legally marrried or seperated \
                     but still legally in a same-sex civil partnership")
    DIVORCED  = (4, "Divorced or formely in a same-sex civil partnership \
                     which is now legally dissolved")
    WIDOWED   = (5, "Widowed or surviving partner from a same-sex \
                     civil partnership")


class StudentOptions(OptionEnum):
    YES = (1, "Yes")
    NO  = (2, "No")


class CountryOfBirthOptions(OptionEnum):
    UK      = (1, "UK")
    NON_UK  = (2, "Non UK")
    NO_CODE = (-9,"No Code required (Students or schoolchildren living away \
                   during term-time") 


class HealthOptions(OptionEnum):
    VERY_GOOD = (1, "Very good health")
    GOOD      = (2, "Good health")
    FAIR      = (3, "Fair health")
    BAD       = (4, "Bad health")
    VERY_BAD  = (5, "Very bad health")
    NO_CODE   = (-9,"No code required (Students or schoolchildren living away \
                     during term-time")


class EthnicityOptions(OptionEnum):
    WHITE   = (1, "White")
    MIXED   = (2, "Mixed")
    ASIAN   = (3, "Asian or Asian British")
    BLACK   = (4, "Black or Black British")
    OTHER   = (5, "Chinese or Other ethnic group")
    NO_CODE = (-9,"No code required (Not resident in England or Wales, \
                   students or schoolchildren living away during term time")

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
    NO_CODE    = (-9,"No code required (Not resident in England or \
                      Wales, students or schoolchildren living away \
                      during term-time)")


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
    NO_CODE           = (-9,"No code required (Aged under 16 or students \
                             or schoolchildren living away during term-time)")


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
    NO_CODE                = (-9,"No code required (People aged under 16, \
                                  people who have never worked and students or \
                                  schoolchildren living away during term-time)")


class IndustryOptions(OptionEnum):
    AGRICULTURE                 = (1, "Agriculture, forestry and fishing")
    ESSENTIALS                  = (2, "Mining and quarrying; Manufacturing; \
                                       Electricity, gas, steam and air conditioning \
                                       system; Water supply")
    CONSTRUCTION                = (3, "Construction")
    TRADE_AND_MOTOR             = (4, "Wholesale and retail trade; Repair of motor \
                                       vehicles and motorcycles")
    ACCOMODATION_AND_FOOD       = (5, "Accomodation and food service activities")
    TRANSPORT_AND_COMMUNICATION = (6, "Transport and storage; \
                                       Information and communication")
    FINANCIAL                   = (7, "Financial and insurance activities; Intermediation")
    REAL_ESTATE_TECHNICAL_ADMIN = (8, "Real estate activities; Professional, \
                                       scientific and technical activities; \
                                       Administrative and \
                                       support service activities")
    EDUCATION                   = (9, "Education")
    HEALTH_AND_SOCIAL_WORK      = (10,"Human health and social work activities")
    PUBLIC_ADMIN_DEFENSE_SOCIAL = (11,"Public administration and defence; \
                                       compulsory social security")
    OTHER                       = (12,"Other community, social and personal \
                                       service activities; Private households \
                                       employing domestic staff; Extra-territorial \
                                       organisations and bodies")
    NO_CODE                     = (-9,"No code required (People aged under 16, \
                                       people who have never worked, and students or \
                                       schoolchildren living away during term-time)")

class HoursWorkedPerWeekOptions(OptionEnum):
    PART_TIME_LOW  = (1, "Part-time: 15 or less hours worked")
    PART_TIME_HIGH = (2, "Part-time: 16 to 30 hours worked")
    FULL_TIME_LOW  = (3, "Full-time: 31 to 48 hours worked")
    FULL_TIME_HIGH = (4, "Full-time: 49 or more hours worked")
    NO_CODE        = (-9,"No code required (People aged under 16, \
                          people not working, and students or schoolchildren \
                          living away during term-time)")

class SocialGradeOptions(OptionEnum):
    AB = (1, "AB")
    C1 = (2, "C1")
    C2 = (3, "C2")
    DE = (4, "DE")
    NO_CODE = (-9, "No code required (People aged under 16, \
                    people resident in communal establishments, and \
                    students or schoolchildren living away during term- \
                    time)")


# class to represent column
class Column:
    def __init__(self, values, type):
        self.values = values
        self.type = type

# map header to column values
colMap = {"Person ID" : Column(None, int), # set to None to allow any unique id, CHANGE ?
          "Region" : Column(RegionOptions.keys(), object),
          "Residence Type" : Column(ResidenceOptions.keys(), pd.StringDtype()),
          "Family Composition" : Column(FamilyCompositionOptions.keys(), int),
          "Population Base" : Column(PopulationBaseOptions.keys(), int),
          "Sex" : Column(SexOptions.keys(), int),
          "Age" : Column(AgeOptions.keys(), int),
          "Marital Status" : Column(MaritalStatusOptions.keys(), int),
          "Student": Column(StudentOptions.keys(), int),
          "Country of Birth" : Column(CountryOfBirthOptions.keys(), int),
          "Health" : Column(HealthOptions.keys(), int),
          "Ethnic Group" : Column(EthnicityOptions.keys(), int),
          "Religion" : Column(ReligionOptions.keys(), int),
          "Economic Activity" : Column(EconomicActivityOptions.keys(), int),
          "Occupation" : Column(OccupationOptions.keys(), int),
          "Industry" : Column(IndustryOptions.keys(), int),
          "Hours worked per week" : Column(HoursWorkedPerWeekOptions.keys(), int),
          "Approximated Social Grade" : Column(SocialGradeOptions.keys(), int)
          }

# compare economic activity to occupation, student status, etc. to find discrepancies
