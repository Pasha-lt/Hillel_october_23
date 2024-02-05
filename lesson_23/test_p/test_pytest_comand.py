import time

def test_1():
    assert True

def test_2():
    time.sleep(1)
    assert False

def test_3():
    assert True

def test_4():
    time.sleep(2)
    assert True

def test_5():
    assert True

def test_6():
    assert False