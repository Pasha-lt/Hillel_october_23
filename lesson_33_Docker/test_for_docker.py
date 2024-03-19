import time

import pytest

def test_sleep_1():
    print('сплю 1 секунду')
    time.sleep(1)
    assert True


def test_sleep_1a():
    print('сплю 1 секунду')
    time.sleep(1)
    assert True


def test_sleep_1b():
    print('сплю 1 секунду')
    time.sleep(1)
    assert True

def test_close_value():
    assert 3.1 == pytest.approx(3.100000000001)

def test_close_value():
    assert 0.1 + 0.2 == pytest.approx(0.3)