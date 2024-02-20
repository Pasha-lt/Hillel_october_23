# не правильний запис в цьому варіанті ви відкриваєте і закриваєте файл на запис ВІСІМ РАЗІВ!!!
with open("1.txt", "w") as file:
    for i in range(9):
        file.write(i)

#правильний запис в цьому варіанті ви відкриваєте і закриваєте файл на запис один раз
with open("2.txt", "w") as file:
    text = ""
    for i in range(9):
        text += str(i)
    file.write(text)