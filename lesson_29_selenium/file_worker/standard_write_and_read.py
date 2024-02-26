text = "hello"

# with open("file_1.txt", "w") as file:
#     file.write(text)

with open("file_1.txt", "r") as file:
    file_data = file.read()

print(file_data)