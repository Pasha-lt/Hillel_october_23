import csv
#
# data = [
#     ['name', 'age', 'city'],
#     ['Alice', '24', 'New York'],
#     ['Bob', '27', 'Los Angeles'],
#     ['Charlie', '22', 'Chicago']
# ]
#
# with open("people.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

with open("people.csv", "r") as file:
    reader = csv.reader(file)
    print(reader)
    print()
    for row in reader:
        print(row)