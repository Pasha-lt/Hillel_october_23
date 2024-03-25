import requests
from faker import Faker



fake = Faker()

body = {
    'userId': 1,
    'title': fake.name(),
    'body': fake.sentence()

}

response = requests.post('https://jsonplaceholder.typicode.com/users/1/posts', json=body)
print(response)

post_id = response.json().get('userId')

response_get = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
print(response_get)

response_del = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
print(response_del)
