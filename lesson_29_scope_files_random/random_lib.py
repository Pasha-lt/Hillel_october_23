import random

random.seed(1)  # що б зберегти рандом

print(random.random()) # [0, 1] float
print(int((random.random()*100))) # [0, 100]
print(int((random.random()*50))) # [0, 50]
print(int(3 + random.random()*(10-3))) # [3, 10]


for i in range(20): # ціле число з діапазона
    print(random.randint(3,7), end="/")
#
print()
#
for i in range(20): # ціле число з діапазона з кроком
    print(random.randrange(1,7, 2), end="/")
print()
lst = ["apple", "banana", "orange", "carrot", "cherry"]
# print(lst)
# random.shuffle(lst) # перемішування списку
# print(lst)

print(random.sample(lst, counts=[1,1,10,1,10], k=3))
print(random.sample(lst, counts=[1,1,10,1,10], k=3))