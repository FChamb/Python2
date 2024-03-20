import unittest
import sys

import test_census_microdata_2011

def test():
    """Create and run the test suite"""
    testsuite = suite()
    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    result = runner.run(testsuite)

def suite():
    """Create a test suite with all the test classes in"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(test_census_microdata_2011.TestExampleMicroData))
    return suite

if __name__ == "__main__":
    test()
