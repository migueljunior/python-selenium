from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions_test import AssertionTest
from search_test import SearchTest

assertions_testing = TestLoader().loadTestsFromTestCase(AssertionTest)
search_testing = TestLoader().loadTestsFromTestCase(SearchTest)

tests = TestSuite([assertions_testing, search_testing])

kwargs = {
    'output': 'test_suite_folder',
    'report_name': 'report_test_suite'
}

runner = HTMLTestRunner(**kwargs)
runner.run(tests)