import unittest
import sys

import MicroDataTeachingVarsTest

def test():
    """Create and run the test suite"""
    testsuite = suite()
    runner = unittest.TextTestRunner(sys.stdout, verbosity=2)
    result = runner.run(testsuite)

def suite():
    """Create a test suite with all the test classes in"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(MicroDataTeachingVarsTest.TestExampleMicroData))
    return suite

if __name__ == "__main__":
    test()
