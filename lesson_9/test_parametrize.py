import pytest
from lesson_9 import add_two_numbers

# solution 1
def test_1():
    assert add_two_numbers(3, 4) == 7

def test_2():
    assert add_two_numbers(13, 4) == 17

def test_3():
    assert add_two_numbers(1, 4) == 5

# solution 2
@pytest.mark.parametrize("numb_1, numb_2, result", [
    pytest.param(3, 4, 7, id="standard"),
    pytest.param(-3, 3, 0, id="negative and positive" ),
    pytest.param(-3, -1, -4, id="two negative")])
def test_set_1(numb_1, numb_2, result):
    assert add_two_numbers(numb_1, numb_2) == result

# solution 3
list_test = [(3, 4, 7), (-3, 3, 0), (-3, -1, -4)]

@pytest.mark.parametrize("numb_1, numb_2, result", list_test)
def test_set_2(numb_1, numb_2, result):
    assert add_two_numbers(numb_1,numb_2) == result



