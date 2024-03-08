import unittest
import pandas as pd

import MicroDataTeachingVars as md
import consistency

class TestExampleMicroData(unittest.TestCase):
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
        s = pd.Series(valid_regions)
        self.assertTrue(consistency.colValidity(s, md.regions))

    def test_invalid_regions(self):
        s = pd.Series(["S12000001"])
        self.assertFalse(consistency.colValidity(s, md.regions))

    def test_invalid_regions_num(self):
        s = pd.Series([60])
        self.assertFalse(consistency.colValidity(s, md.regions))
