from lesson_7 import calc_dict
from lesson_7 import concatenate


# pytest
def test_calc_addition():
    assert calc_dict["+"](3,7) == 10, "Повинно бути 10 "

def test_calc_subs():
    assert calc_dict["-"](13,7) == 6

def test_concatenate():
    assert concatenate("a", "b") == "ab"