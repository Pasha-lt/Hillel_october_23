# приклад псевдокоду: якщо буде зміна var_а більше ніж 10 зроби цей код.

# для того що б поставити курсор в декількох місцях(в групі) затискаємо option або alt
# для коментування декількох стрічок або розкоментувати виділяємо command+? або cntr+?

# # НЕ ПИШІТЬ ЗМІНІ УКРАЇНСЬКОЮ МОВОЮ. !!!НЕ ВІРНИЙ СИНТАКСИС
# зміна_1 = 20
# print(зміна_1)
#
# # НЕ ПИШІТЬ УКРАЇНСЬКІ ЗМІНІ АНГЛІЙСЬКИМИ ЛІТЕРАМИ !!!НЕ ВІРНИЙ СИНТАКСИС
# zmina_1 = 20
# print(zmina_1)

# ПРАВИЛЬНИЙ ВАРІАНТ
variable_1 = 20
variable_2 = 5
variable_3 = 3

# hotkey дублювання command+d або cntrl+d
#
# print(variable_1 * variable_2) # без збереження в змінну
#
# result = variable_2 - variable_1  # більш вірний в написанні
# print(result)

# # залишок від ділення %
# result = variable_1 % variable_3  # 2
# print(result)

# # скільки разів ми змогли поділити на ціло //
# result = variable_1 // variable_3  # 6
# print(result)
#todo питання півбесіда Які типи данних є в Python.

# # snake_case
# the_amount_of_students  = 10
# variable_4 = 10

# Змінні не починаються з цифри, це забороненно
# 2variable = 10
# print(2variable)

# STR
# sample_text = "привіт, мене звуть Павло"
# print(sample_text)
# print(type(sample_text))

# sample_text_1 = "999"
# sample_text_2 = "1"
# print(sample_text_1)
# print(type(sample_text_1))
# print(sample_text_1 + sample_text_2) # плюс з стрічками це конкатенація
#
# sample_text_1_int = int(sample_text_1)  # трансформування типу данних
# sample_text_2_int = int(sample_text_2)  # трансформування типу данних
# result  = (sample_text_2_int + sample_text_1_int)
# result = 2
# print(result)


age = int(input("скільки вам років"))  # default повертає str тип данних
print(age)
print(type(age))
