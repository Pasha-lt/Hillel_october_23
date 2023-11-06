# # Ще раз конкатенація може бути додавання два стр, та може бути множення стр на інт
# variable_1 = "5"
# variable_2 = "12"
#
# print(int(variable_1) * int(variable_2)) # 60
# print(variable_1 * int(variable_2)) # 555555555555
# print(variable_1 + variable_2) # 512
#
# variable_1 = "new"
# variable_2 = "student"
# print(variable_1 + variable_2)  # newstudent
# print(variable_1,                    variable_2)  # new student

# # todo питання півбесіда Які типи данних є в Python.
# variable_1 = 10
# variable_2 = 20
# print(variable_1)
# print(variable_2)
# # синтаксичний цукор
# variable_1, variable_2 = variable_2, variable_1
# print(variable_1)
# print(variable_2)
#
# # множине присвоєння
# a,b,c = 3,4,5
# print(a,b,c)

# # степінь
# print(2**3)
#
# # квадратний корінь
# print(25**0.5)

# зарезервовані слова
# variable_1 = 999
# print = 20  # перевизначаємо функцію print
# print(variable_1 + 20)

# float, коли в числі є крапка то це флоат
# variable_1 = 10000000000000000000.1  # це float
# variable_2 = 0
# print(type(variable_2), variable_2)
# variable_2_float = float(variable_2)
# print(type(variable_2_float), variable_2_float)

# новий тип даних bool. в пайтоні пишеться з великої літери, в інших мовах може бути з малої.
# будьте уважні.
# variable_true_wrong = true # НЕПРАВИЛЬНО БУДЕ ПОМИЛКА
# variable_true = True
# variable_false = False
# # print(int(variable_true))
# print(bool(""))  # False
# print(bool(" "))  # True
# print(bool("0"))  # True
# print(bool(0))  # False
# print(bool(-9))  # True
# print(bool(9))  # True

# тип данних
# var_none = None
# print(type(var_none), var_none)
# print(bool(var_none))  # False

# Математичні порівняння
# var_1 = 5
# var_2 = 2
# var_3 = 5 # дубль

# >, < , >=, <=
# print(var_1 > var_2)  # True
# print(var_1 < var_2)  # False
# print(var_1 >= var_2)  # True
# print(var_1 <= var_2)  # False
# print(var_1 <= var_3)  # True
# print(var_1 >= var_3)  # True

# == , !=  , == - порівняння по значенню
# print(var_1 == var_3)
# print(5 == 5.0)  # True
# print(var_1 != var_3)

# is, not - порівняння по айді
# var_1 = 5
# var_1_float = 5.0
# var_2 = 2
# var_3 = 5 # дубль
# print(id(var_1))
# print(id(var_1_float))
# print(id(var_2))
# print(id(var_3))
#
#
# print(True)
# print(not True)
# print(True is True)
# print(not(True is True))
# print(var_1 is not var_2)

# оптимізує в проміжку # interned integers from “-5” to “256” - числа які мають одне айді
# variable_1 = 200
# variable_2 = 199 + 1
# print(id(variable_1))
# print(id(variable_2))
# print(hex(id(variable_1)))
# print(hex(id(variable_2)))
# # variable_1 == variable_2
# # Out[3]: True
# # variable_1 is variable_2
# # Out[4]: True
#
# variable_1 = 2000
# variable_2 = 1999 + 1
# print(id(variable_1))
# print(id(variable_2))
# # variable_1 == variable_2
# # Out[4]: True
# # variable_1 is variable_2
# # Out[5]: False


# IF
# var_1 = 5
# var_1_float = 5.0
# var_2 = 2
# var_3 = 5 # дубль

# if var_1 > var_2:
#     print("привіт це гілка іф")  # виконається коли умова буде Тру.
# else:
#     print("блок іф виявися фолс тому ми в цьому блоці кода")
#
# print("text after if block")


# Вкладений if
# age = int(input("how old are you"))
# if age < 18:
#     print("вибачте вхід в клуб з 18 років")  # виконається коли умова буде Тру.
# else:
#     if age >= 21:
#         print("ви можете купувати алкоголь")
#     else:
#         print("Ви можете знаходить в клубі та їсти морозиво")

# elif
# if age < 18:
#     print("вибачте вхід в клуб з 18 років")  # виконається коли умова буде Тру.
# elif age >= 21:
#     print("ви можете купувати алкоголь")
# else:
#     print("Ви можете знаходить в клубі та їсти морозиво")

# string_var = "iGor"
# print(type(string_var))
#
# print(string_var.upper())  # IGOR
# print(string_var.lower())  # igor
# print(string_var.title())  # Igor
# string_var = string_var.title()  # стр зміний тип даних для збреження треба зберігати.
# print(string_var)

url = "https://product_ur_prod.com"
print(url)
url = url.replace("_prod", "_qa")  # заміна
print(url)
url = url.replace("_qa", "")  # видалення
print(url)

# password = input("please, type your name: ")
# if password.title() == "Igor":
#     print("welcome")
# else:
#     print("sorry, access deny")


