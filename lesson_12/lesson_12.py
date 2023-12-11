# API
# https://api.chucknorris.io/#!
# OOP

class NameClass:
    name: str = "Taras"
    age = 21

    def say_hello(self):
        self.age_name = f"{self.age}-річний {self.name}"
        self.hello_string = f"привіт {self.age_name}, як справи?"
        print(self.hello_string)

    def say_goodbay(self):
        print(f"гарного дня {self.age_name}")


# obj_1 = NameClass()
# obj_1.name = {"name": ["Pasha", "Sasha", "Natasha"]}
# obj_1.say_hello()
# obj_1.address = "Грушевського 34в"  # додавання до обьєкту атрибута якого не було
# print(obj_1.address)
# # Міксуємо навчання чи вчимо одне за другим?
# obj_2 = NameClass()
# print(hasattr(obj_1, "address"))  # перевіряє чи в класі атрибут
# print(hasattr(obj_2, "address"))
#
# print(getattr(obj_1, "address"))  # прочитати зміну
# print(setattr(obj_1, "address", "Гришка 32"))  # змінити зміну
#
# # delattr(obj_1, "address")  # видалення обьєкта
# print(obj_1.address)

# class User:
#     name = "Taras"
#     _phone = "0931234567"  # protected
#
#     def say_hello(self):
#         return f"імя {self.name} телефон - {self._phone}"
#
# taras = User()
# result = taras.say_hello()
# print(result)
# print(setattr(taras, "_phone", "1111"))  # змінити зміну
# print(taras.say_hello())

# todo Інкапсуляція = protected + secret, Інкапсуляція це включання всього необхідно в клас.
class User:
    name = "Taras"
    _phone = "0931234567"  # protected
    __address = "Лютеранська 14"  # secret
    def say_hello(self):
        return f"імя {self.name} телефон - {self._phone}, адреса - {self.__address}"

taras = User()
print(taras.say_hello())
taras.__address = "Саксаганського 52"
print(dir(taras))
taras._User__address = "Саксаганського 52"
print(taras.say_hello())
