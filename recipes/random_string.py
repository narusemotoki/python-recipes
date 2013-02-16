#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import random


def gen_random_string(length):
    u"""引数で与えた長さのランダムな文字列を返します。"""

    # 英字小文字 + 英字大文字 + 数字
    # 記号その他の文字が必要ならここに加えればOK
    chars = string.ascii_letters + string.digits
    return ''.join([random.choice(chars) for i in range(length)])
