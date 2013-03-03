#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import random_date
import datetime
import time


class TestRandomString(unittest.TestCase):
    def test_gen_random_date(self):
        ts = time.mktime(datetime.datetime.now().timetuple())
        now = datetime.datetime.fromtimestamp(ts)
        random = random_date.gen_random_date(now)
        # TODO: タイミング次第で失敗する気がするので改善したい
        self.assertEqual(random, now)

        now = datetime.datetime.fromtimestamp(ts)
        random = random_date.gen_random_date(now, now)
        self.assertEqual(random, now)

        past = now - datetime.timedelta(days=30)
        for i in range(10):
            random = random_date.gen_random_date(past)
            self.assertLessEqual(random, now)
            self.assertGreaterEqual(random, past)
