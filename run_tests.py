#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import imp
import os
import sys
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir + '/recipes')


if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests_dir = project_dir + '/tests'

    for file in os.listdir(tests_dir):
        path = tests_dir + '/' + file
        if os.path.isfile(path) and path.endswith('.py'):
            mod = imp.load_source(os.path.splitext(path)[0], path)
            suite.addTest(loader.loadTestsFromModule(mod))

    unittest.TextTestRunner(verbosity=1).run(suite)
