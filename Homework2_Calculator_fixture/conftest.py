# Hogwarts_Homework
# Jewish
# 2021/4/9 19:45
from typing import List

import pytest

from Calculator import Calculator


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope='class')
def initcalc_class():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")
