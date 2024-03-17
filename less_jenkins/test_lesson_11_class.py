import time

import pytest


@pytest.mark.skip  # вішаємо скіп на клас
class TestSlepp:
    def test_sleep_1(self):
        print("я йду спати на 1 секунду")
        time.sleep(1)

    def test_sleep_2(self):
        print("я йду спати на 1 секунду")
        time.sleep(1)


class TestWait:
    URL = "https://www.ourproduct.ua"

    @pytest.mark.skipif("qa" in URL, reason="повинен працювати тільки для прода")  # скіпаємо при певній умові коли qa в юрлі
    def test_wait_1(self):
        print("я зайнятий чекай 1 секунду")
        time.sleep(1)

    @pytest.mark.skip  # пропустити тест
    def test_wait_2(self):
        print("я зайнятий чекай 1 секунду")
        time.sleep(1)

    @pytest.mark.xfail  # коли падає буде скіп, коли запрацює буде зеленим
    def test_wait_3(self):
        print("я зайнятий чекай 1 секунду")
        time.sleep(1)
        assert True


class TestOther:
    def test_close_value(self):
        assert 3.1 == pytest.approx(3.1000001)

    def test_close_value_2(self):
        assert 0.1 + 0.2 == pytest.approx(0.3)
