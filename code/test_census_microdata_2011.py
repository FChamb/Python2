import unittest
import pandas as pd

import census_microdata_2011 as md
from consistency import colValidity as col_valid

class TestExampleMicroData(unittest.TestCase):

    # Helper functions
    def check_valid(self, values, permitted):
        if permitted is None:
            return True
        s = pd.Series(values)
        if col_valid(s, permitted.keys()):
            return True
        for v in values:
            if not col_valid(pd.Series(v), permitted.keys()):
                self.fail(f"Expected {v} be valid, but it was not (permitted: {permitted.keys()})")

    def check_invalid_single(self, value, permitted):
        s = pd.Series([value])
        self.assertFalse(col_valid(s, permitted.keys()))

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
        self.check_valid(valid_regions, md.RegionOptions)

    def test_invalid_regions(self):
        self.check_invalid_single("S12000001", md.RegionOptions)
        self.check_invalid_single(60, md.RegionOptions)

    # Residence types
    def test_residence_type(self):
        self.check_valid(["H", "C"], md.ResidenceOptions)

    def test_invalid_residence_type(self):
        self.check_invalid_single("O", md.ResidenceOptions)
        self.check_invalid_single(0, md.ResidenceOptions)

    # Family Composition
    def test_family_composition_valid(self):
        self.check_valid([3,2,1,4,5,6,-9], md.FamilyCompositionOptions)

    def test_family_composition_invalid(self):
        self.check_invalid_single(0, md.FamilyCompositionOptions)
        self.check_invalid_single(-1, md.FamilyCompositionOptions)

    # Population base
    def test_population_base_valid(self):
        self.check_valid([1, 2, 3], md.PopulationBaseOptions)

    def test_population_base_invalid(self):
        self.check_invalid_single(0, md.PopulationBaseOptions)
        self.check_invalid_single(-1, md.PopulationBaseOptions)
        self.check_invalid_single(-9, md.PopulationBaseOptions)

    # Sex
    def test_sex_valid(self):
        self.check_valid([1, 2], md.SexOptions)

    def test_sex_invalid_3(self):
        self.check_invalid_single(0, md.SexOptions)
        self.check_invalid_single(3, md.SexOptions)
        self.check_invalid_single(-9, md.SexOptions)

    # Age
    def test_age_valid(self):
        self.check_valid([1, 2, 3, 4, 5, 6, 7, 8], md.AgeOptions)

    def test_age_invalid(self):
        self.check_invalid_single(0, md.AgeOptions)
        self.check_invalid_single(9, md.AgeOptions)
        self.check_invalid_single(-9, md.AgeOptions)

    # Marital Status
    def test_marital_status_valid(self):
        self.check_valid([1,2,3,4,5], md.MaritalStatusOptions)

    def test_marital_status_invalid_zero(self):
        self.check_invalid_single(0, md.MaritalStatusOptions)
        self.check_invalid_single(6, md.MaritalStatusOptions)
        self.check_invalid_single(-9, md.MaritalStatusOptions)

    # Student
    def test_student_valid(self):
        self.check_valid([1, 2], md.StudentOptions)

    def test_student_invalid_zero(self):
        self.check_invalid_single(0, md.StudentOptions)
        self.check_invalid_single(3, md.StudentOptions)
        self.check_invalid_single(-9, md.StudentOptions)

    # Country of birth
    def test_birth_country_valid(self):
        self.check_valid([1, 2, -9], md.CountryOfBirthOptions)

    def test_birth_country_invalid_zero(self):
        self.check_invalid_single(0, md.CountryOfBirthOptions)
        self.check_invalid_single(3, md.CountryOfBirthOptions)

    # Health
    def test_health_valid(self):
        self.check_valid([1, 2, 3, 4, 5, -9], md.HealthOptions)

    def test_health_invalid(self):
        self.check_invalid_single(0, md.HealthOptions)
        self.check_invalid_single(6, md.HealthOptions)

    # Ethnic Group
    def test_ethnicity_valid(self):
        self.check_valid([1,2,3,4,5,-9], md.EthnicityOptions)

    def test_ethnicity_invalid(self):
        self.check_invalid_single(0, md.EthnicityOptions)
        self.check_invalid_single(6, md.EthnicityOptions)

    # Religion
    def test_religion_valid(self):
        self.check_valid([1,2,3,4,5,6,7,8,9,-9], md.ReligionOptions)

    def test_religion_invalid(self):
        self.check_invalid_single(0, md.ReligionOptions)
        self.check_invalid_single(10, md.ReligionOptions)

    # Economic activity
    def test_economic_activity_valid(self):
        self.check_valid([1,2,3,4,5,6,7,8,9,-9], md.EconomicActivityOptions)

    def test_economic_activity_invalid(self):
        self.check_invalid_single(0, md.EconomicActivityOptions)
        self.check_invalid_single(10, md.EconomicActivityOptions)

    # Occupation
    def test_occupation_valid(self):
        self.check_valid([1,2,3,4,5,6,7,8,9,-9], md.OccupationOptions)

    def test_occupation_invalid(self):
        self.check_invalid_single(0, md.OccupationOptions)
        self.check_invalid_single(10, md.OccupationOptions)

    # Industry
    def test_industry_valid(self):
        self.check_valid([1,2,3,4,5,6,7,8,9,10,11,12,-9], md.IndustryOptions)

    def test_industry_invalid(self):
        self.check_invalid_single(0, md.IndustryOptions)
        self.check_invalid_single(13, md.IndustryOptions)

    # Hours worked per week
    def test_hours_valid(self):
        self.check_valid([1,2,3,4,-9], md.HoursWorkedPerWeekOptions)

    def test_hours_invalid(self):
        self.check_invalid_single(0, md.HoursWorkedPerWeekOptions)
        self.check_invalid_single(5, md.HoursWorkedPerWeekOptions)

    # Approximated social grade
    def test_social_grade_valid(self):
        self.check_valid([1,2,3,4,-9], md.SocialGradeOptions)

    def test_social_grade_invalid(self):
        self.check_invalid_single(0, md.SocialGradeOptions)
        self.check_invalid_single(5, md.SocialGradeOptions)
