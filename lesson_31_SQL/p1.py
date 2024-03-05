import sqlite3

connection = sqlite3.connect("orders.db", isolation_level=None)  # isolation_level=None - потрібен що б відразу комітило
cursor = connection.cursor()



# Варіант виводу результата
# 1 варіант
import pprint
# pprint.pprint(list(result))  # для зручного відображення
#
# for i in result:
#    print(i)

# 2 варіант
# print(result.fetchall()) # витягнути все

# 3 варіант
# print(result.fetchone()) # витягує по одному
# print(result.fetchone())
# print(result.fetchone())

# 4 варіант
# pprint.pprint(result.fetchmany(4)) # витягує по декілька

# cursor.execute("INSERT INTO Vendors(name, item, deal, price) VALUES ('Snigana', 'Car-sedan2', 4, 500);")
# result = cursor.execute("select * from Vendors;")
# pprint.pprint(result.fetchall())

# connection.commit() # додати зміни в бд АЛЕ ДИВИСЬ isolated level бо можна без коміту

# вибірка даних з підставляням даних в наш запит
# Варінат 1 ф стрічка
# deal_id = 3
# price = 10
# result = cursor.execute(f'select * from Vendors where deal={deal_id} and price>{price};')
# pprint.pprint(result.fetchall())

# Варінат 2 tuple
# result = cursor.execute(f'select * from Vendors where deal=(?) and price>(?);', (3,10))
# result = cursor.execute(f'select * from Vendors where deal=(?);', (3,)) # передавти треба кортеж
# pprint.pprint(result.fetchall())

# Варінат 3 dict
# result = cursor.execute(f'select * from Vendors where deal=:deal_id and price> :price;',
#                         {'deal_id':3, 'price':10})

# Різні типи виконання(execute)
# 1 варіант ми розглянули попередньо cursor.execute(f'select * from Vendors where deal=(?) and price>(?);', (3,10))
# 2 варіант executemany
# cursor.executemany("INSERT INTO Vendors(name, item, deal, price) VALUES ((?), (?), (?), (?));",
#                   [('Pavlo21', 'Car-sedan44', 4, 101),
#                    ('Pavlo11', 'Car-sedan56', 4, 102),
#                    ('Pavlo1', 'Car-sedan67', 4, 101)])

# 3 варіант executescript
# with open('script.sql', 'r') as f:
#     cursor.executescript(f.read())




cursor.close()
connection.close()