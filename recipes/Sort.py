#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Sort(object):
    @classmethod
    def sort_dict_by_value(cls, source, asc=True):
        u'''Dictをバリューの値でソートする'''
        # Dictでは順番を保持出来ないのでタプルをリストに入れる
        # これを使えばDictのまま実現できるみたい
        # http://pypi.python.org/pypi/ordereddict/
        result = []
        for i in sorted(source.items(), key=lambda v: v[1], reverse=not asc):
            result.append(i)

        return result

    @classmethod
    def sort_tuple(cls, source, index=0, asc=True):
        u'''タプルのリストをソートする'''
        result = []
        for i in sorted(source, key=lambda v: v[index], reverse=not asc):
            result.append(i)

        return result
