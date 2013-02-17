#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Sort import Sort


class TestSort(unittest.TestCase):
    def test_sort_dict_by_value(self):
        source = {'b': 3, 'a': 4, 'c': 2, 'd': 1}
        asc_sorted = [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
        desc_sorted = asc_sorted[::-1]

        self.assertEqual(Sort.sort_dict_by_value(source), asc_sorted)
        self.assertEqual(Sort.sort_dict_by_value(source, False), desc_sorted)

    def test_sort_tuple(self):
        source = [('b', 3), ('a', 4), ('c', 2), ('d', 1)]

        # タプルの1つ目の要素でソート
        asc_1_sorted = [('a', 4), ('b', 3), ('c', 2), ('d', 1)]
        desc_1_sorted = asc_1_sorted[::-1]

        self.assertEqual(Sort.sort_tuple(source, 0), asc_1_sorted)
        self.assertEqual(Sort.sort_tuple(source, 0, False), desc_1_sorted)

        # タプルの2つ目の要素でソート
        # asc_2_sorted = asc_1_sortedよりは新しく書いた方が分かりやすいかなって
        asc_2_sorted = [('d', 1), ('c', 2), ('b', 3), ('a', 4), ]
        desc_2_sorted = asc_2_sorted[::-1]

        self.assertEqual(Sort.sort_tuple(source, 1), asc_2_sorted)
        self.assertEqual(Sort.sort_tuple(source, 1, False), desc_2_sorted)
