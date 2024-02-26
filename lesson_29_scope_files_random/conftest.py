import pytest

@pytest.fixture
def conf_1():
    print("->func")
    data = "func"
    yield data
    print("\n", "func<-")

@pytest.fixture(scope="class")
def conf_2():
    print("->class")
    data = "class"
    yield data
    print("class<-")

@pytest.fixture(scope="module")
def conf_3():
    print("->module")
    data = "module"
    yield data
    print("module<-")

@pytest.fixture(scope="session")
def conf_4():
    print("\n","->session")
    data = "session"
    yield data
    print("session<-")
