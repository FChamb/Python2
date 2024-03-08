import unittest
import pandas as pd

import MicroDataTeachingVars as md
from consistency import colValidity as col_valid

class TestExampleMicroData(unittest.TestCase):

    # Helper functions
    def check_valid(self, values, permitted):
        s = pd.Series(values)
        self.assertTrue(col_valid(s, permitted))

    def check_invalid_single(self, value, permitted):
        s = pd.Series([value])
        self.assertFalse(col_valid(s, permitted))

    # Student ID
    def test_valid_student_id(self):
        # No restrictions on Student ID
        self.check_valid([0, 10, 23132], None)
        self.check_valid(["awdawd", 2013, -100], None)

    # Regions
    def test_valid_regions(self):
        valid_regions =[
            "E12000001",
            "E12000002",
            "E12000003",
            "E12000004",
            "E12000005",
            "E12000006",
            "E12000007",
            "E12000008",
            "E12000009",
            "W92000004"
        ]
        self.check_valid(valid_regions, md.regions)

    def test_invalid_regions(self):
        self.check_invalid_single("S12000001", md.regions)
        self.check_invalid_single(60, md.regions)

    # Residence types
    def test_residence_type(self):
        self.check_valid(["H", "C"], md.residences)

    def test_invalid_residence_type(self):
        self.check_invalid_single("O", md.residences)
        self.check_invalid_single(0, md.residences)

    # Family Composition
    def test_family_composition_valid(self):
        self.check_valid([3,2,1,4,5,6,-9], md.familyComp)

    def test_family_composition_invalid(self):
        self.check_invalid_single(0, md.familyComp)
        self.check_invalid_single(-1, md.familyComp)

    # Population base
    def test_population_base_valid(self):
        s = pd.Series([1, 2, 3])
        self.assertTrue(col_valid(s, md.popBase))

    def test_population_base_invalid(self):
        self.check_invalid_single(0, md.popBase)
        self.check_invalid_single(-1, md.popBase)
        self.check_invalid_single(-9, md.popBase)

    # Sex
    def test_sex_valid(self):
        self.check_valid([1, 2], md.sexes)

    def test_sex_invalid_3(self):
        self.check_invalid_single(0, md.sexes)
        self.check_invalid_single(3, md.sexes)
        self.check_invalid_single(-9, md.sexes)

    # Age
    def test_age_valid(self):
        self.check_valid([1, 2, 3, 4, 5, 6, 7, 8], md.ages)

    def test_age_invalid(self):
        self.check_invalid_single(0, md.ages)
        self.check_invalid_single(9, md.ages)
        self.check_invalid_single(-9, md.ages)

    # Marital Status
    def test_marital_status_valid(self):
        self.check_valid([1,2,3,4,5], md.maritalStat)

    def test_marital_status_invalid_zero(self):
        self.check_invalid_single(0, md.maritalStat)
        self.check_invalid_single(6, md.maritalStat)
        self.check_invalid_single(-9, md.maritalStat)

    # Student
    def test_student_valid(self):
        self.check_valid([1, 2], md.studying)

    def test_student_invalid_zero(self):
        self.check_invalid_single(0, md.studying)
        self.check_invalid_single(3, md.studying)
        self.check_invalid_single(-9, md.studying)

    # Country of birth
    def test_birth_country_valid(self):
        self.check_valid([1, 2, -9], md.birthCountry)

    def test_birth_country_invalid_zero(self):
        self.check_invalid_single(0, md.birthCountry)
        self.check_invalid_single(3, md.birthCountry)

    # Health
    def test_health_valid(self):
        self.check_valid([1, 2, 3, 4, 5, -9], md.healthStat)

    def test_health_invalid(self):
        self.check_invalid_single(0, md.healthStat)
        self.check_invalid_single(6, md.healthStat)

    # Ethnic Group
    def test_ethnicity_valid(self):
        self.check_valid([1,2,3,4,5,-9], md.ethnicity)

    def test_ethnicity_invalid(self):
        self.check_invalid_single(0, md.ethnicity)
        self.check_invalid_single(6, md.ethnicity)

    # Religion
    def test_religion_valid(self):
        self.check_valid([1,2,3,4,5,6,7,8,9,-9], md.religion)

    def test_religion_invalid(self):
        self.check_invalid_single(0, md.religion)
        self.check_invalid_single(10, md.religion)

    # Economic activity
    def test_economic_activity_valid(self):
        self.check_valid([1,2,3,4,5,6,7,8,9,-9], md.econAct)

    def test_economic_activity_invalid(self):
        self.check_invalid_single(0, md.econAct)
        self.check_invalid_single(10, md.econAct)

    # Occupation
    def test_occupation_valid(self):
        self.check_valid([1,2,3,4,5,6,7,8,9,-9], md.job)

    def test_occupation_invalid(self):
        self.check_invalid_single(0, md.job)
        self.check_invalid_single(10, md.job)

    # Industry
    def test_industry_valid(self):
        self.check_valid([1,2,3,4,5,6,7,8,9,10,11,12,-9], md.industry)

    def test_industry_invalid(self):
        self.check_invalid_single(0, md.industry)
        self.check_invalid_single(13, md.industry)

    # Hours worked per week
    def test_hours_valid(self):
        self.check_valid([1,2,3,4,-9], md.hrs)

    def test_hours_invalid(self):
        self.check_invalid_single(0, md.hrs)
        self.check_invalid_single(5, md.hrs)

    # Approximated social grade
    def test_social_grade_valid(self):
        self.check_valid([1,2,3,4,-9], md.socialGr)

    def test_social_grade_invalid(self):
        self.check_invalid_single(0, md.socialGr)
        self.check_invalid_single(5, md.socialGr)
