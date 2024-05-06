import unittest

def select_test_cases(case_pattern):
    test_dir = 'C:\\Users\\xxzhen\\Desktop\\bnc\\case\\'
    return unittest.defaultTestLoader.discover(test_dir, pattern=case_pattern)
