import pytest

@pytest.mark.smoke
def test_1():
    assert True

def test_2():
    assert True

@pytest.mark.regression
def test_3():
    assert True

@pytest.mark.smoke
def test_4():
    assert True

def test_5():
    assert True

@pytest.mark.regression
@pytest.mark.smoke
def test_6():
    assert True

def test_7():
    assert True

@pytest.mark.smoke
def test_8():
    assert True

@pytest.mark.regression
def test_9():
    assert True

def test_10():
    assert True

@pytest.mark.regression
def test_11():
    assert True

def test_12():
    assert True


#  pytest -m "smoke or regression" -v     ранить і то і то
#  pytest -m "smoke and regression" -v    ранить коли збігається обидва
#  pytest -m "not smoke" -v               ранить всі окрім smoke