#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time
import datetime


def gen_random_date(lower_limit, limit=datetime.datetime.now()):
    u"""引数で与えられた日付の間の日付をランダムに返します。"""

    lower_limit_ts = time.mktime(lower_limit.timetuple())
    limit_ts = time.mktime(limit.timetuple())
    random_ts = random.randint(lower_limit_ts, limit_ts)
    return datetime.datetime.fromtimestamp(random_ts)
