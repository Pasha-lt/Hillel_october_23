
class MyMock:
    print('-->mock_class<--')
    mock_filed = 'default field mock class'

class MockingClass(MyMock):

    def my_func(self) -> str:
        print('-->my_func<--')
        return 'my_func_text'