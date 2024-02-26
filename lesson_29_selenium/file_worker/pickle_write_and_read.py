import pickle

data = {"key_1":"value_1", "key_2":"value_2"}
with open('data.pickle', "wb") as file:
    pickle.dump(data, file)


with open('data.pickle', "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)