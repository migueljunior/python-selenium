from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions_test import AssertionTest
from search_test import SearchTest

assertions_test = TestLoader().loadTestsFromTestCase(AssertionTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

tests = TestSuite([assertions_test, search_test])

kwargs = {
    'output': 'test_suite_folder',
    'report_name': 'report_test_suite'
}

runner = HTMLTestRunner(**kwargs).run(tests)