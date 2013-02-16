#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir + '/recipes')

import unittest
import random_string


class TestRandomString(unittest.TestCase):
    def test_gen_random_string(self):
        for i in range(32):
            rs = random_string.gen_random_string(i)
            reg = '^[a-zA-z0-9]{{{length:d}}}$'.format(length=i)
            self.assertRegexpMatches(rs, reg)

if __name__ == '__main__':
    unittest.main()
