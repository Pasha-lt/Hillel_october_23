# pip install pytest_mock

from pytest_mock import MockerFixture

from Hillel_october_23.lesson_33_mock.mocking_module import MockingClass


def test_mock_cls(mocker: MockerFixture):
    mocker.patch.object(MockingClass, 'mock_filed', 'mock_version')
    cls = MockingClass
    # assert cls.mock_filed == 'default field mock class'
    assert cls.mock_filed == 'mock_version'


def test_mock_func(mocker: MockerFixture):
    print(MockingClass().my_func())
    mocker.patch(target='Hillel_october_23.lesson_33_mock.mocking_module.MockingClass.my_func', return_value='my_func_text_update')
    # a = 'my_func_text_update'
    print(MockingClass().my_func())
