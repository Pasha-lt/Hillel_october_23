import time

import pytest


def test_sleep_1():
    print("я йду спати на 1 секунду")
    time.sleep(1)


def test_wait_1():
    print("я зайнятий чекай 1 секунду")
    time.sleep(1)


def test_sleep_2():
    print("я йду спати на 1 секунду")
    time.sleep(1)


def test_wait_2():
    print("я зайнятий чекай 1 секунду")
    time.sleep(1)


def test_wait_3():
    print("я зайнятий чекай 1 секунду")
    time.sleep(1)


def test_close_value():
    assert 3.1 == pytest.approx(3.1000001)


def test_close_value_2():
    assert 0.1 + 0.2 == pytest.approx(0.3)

#  pytest -m "smoke or regression" -v     ранить і то і то
#  pytest -m "smoke and regression" -v    ранить коли збігається обидва
#  pytest -m "not smoke" -v               ранить всі окрім smoke
#  pytest -k "wait" lesson_11/test_lesson_11.py  ранимо по ключовому слову
# pytest -s lesson_11/test_lesson_11.py режим з прінтами

# pytest lesson_11/test_lesson_11.py -v -n=auto запуск в кілька потоків з прорахуванням кількості потоків.
# pytest lesson_11/test_lesson_11.py -v -n=4   конкретна кількість потоків.
# python3 -m pytest lesson_11/test_lesson_11.py -n=4 - Ще один варіант запису який більш універсальний,
# використовуйте коли попередній не працює.

# pytest -k "wait" lesson_11/test_lesson_11.py -v -n=3  - обьєднання

# flake8
# flake8 lesson_11/test_lesson_11.py ранимо тест на перевірку
# flake8 --ignore=E501 lesson_11/test_lesson_11.py - ігноримо помилку --ignore=E501

