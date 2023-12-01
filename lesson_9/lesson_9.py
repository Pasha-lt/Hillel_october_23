# docstring
def foo(number_2:int, number_1: int) -> int:
    """
    add two numbers
    :param number_1 int: first number
    :param number_2 int: second number
    :return int: result add two number
    """
    result = number_1 + number_2
    return result

# use default only when your func need it. Не ставимо дефолт і не використовуємно інпут в оголошені функції.
# ENV and requirements.txt коли беремо новий проект дивимось його релізи на pypi.org
# Exceptions

# try:
#     print(40/0)
# except:
#     print("На нуль у пайтоні ділити не можна")

# try:
#     print(40/0)
# except ZeroDivisionError:
#     print("На нуль у пайтоні ділити не можна")


# try:
#     print(int("fdsfdsc"))
# except (ZeroDivisionError, ValueError): # ловили декілька помилок
#     print("На нуль у пайтоні ділити не можна")

# ми можемо ловити ексепшини вверх по гілці. файл exceptions.txt в цій же папці

# value_1 = "0"  # ZeroDivisionError
# value_1 = "fdsfds"  # ValueError

# try:
#     print(5/int(value_1))
# except ZeroDivisionError:
#     print("на нуль не ділиться в пайтоні")
# except ValueError:
#     print("не можна зробити числом")

# try:
#     print(5/0)
# except ZeroDivisionError as e:
#     print("на нуль не ділиться в пайтоні")
#     print(f"we get error -> {e} <-")


# Pytest parametrize -> подивіться файл test_parametrize.py
def add_two_numbers(number_1:int|float, number_2: int|float) -> int|float:
    result = number_1 + number_2
    return result


# tuple return
# tuple_1 = (1, 2, 3)
# print(type(tuple_1), tuple_1)
#
# tuple_2 = 1, 2, 3
# print(type(tuple_2), tuple_2)


# decorator python

def func_wrapper(func):
    def wrapper(*arg, **kwarg):
        print("before")
        result = func(*arg, **kwarg)
        print("after")
        return result
    return wrapper

def bar(*arg, **kwarg):
    print("hello", arg, kwarg)


# # для розуміння
# wrapped_func = func_wrapper(bar)
# wrapped_func()


# Випадок номер два
@func_wrapper
def bar_1(*arg, **kwarg):
    print("hello bar 1", arg, kwarg)

@func_wrapper
def bar_2(*arg, **kwarg):
    print("hello bar 2", arg, kwarg)

# bar_1(333)
# bar_2(333)

from datetime import datetime

def func_wrapper_time(func):
    def wrapper(*arg, **kwarg):
        start = datetime.now()
        result = func(*arg, **kwarg)
        delta_time = datetime.now() - start
        print("Час виконання функції ось такий: ", delta_time)
        return result
    return wrapper


import time
@func_wrapper_time
def foo_1(*arg, **kwarg):
    print("foo_1")
    time.sleep(1)


@func_wrapper_time
def foo_2(*arg, **kwarg):
    print("foo_2")
    time.sleep(2)

# foo_1()
# foo_2()



# Pytest fixture