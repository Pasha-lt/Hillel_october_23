from locust import HttpUser, task, between, tag
from faker import Faker

import random

# https://jsonplaceholder.typicode.com/
class MyException(Exception):
    pass

class MySecondTest(HttpUser):

    wait_time = between(2, 5)  # коли хочемо зробити рандомний час запити час на запит

    @tag('simple')
    @task
    def get_all_posts(self):
        self.client.get('posts')

    @task
    def crud(self):
        fake = Faker()

        payload = {
            'userId': 1,
            'title': fake.name(),
            'body': fake.sentence()}

        response_create = self.client.post('posts', data=payload)

        print(response_create.status_code)
        if response_create.status_code != 201:
            raise MyException("We can't create post")

        post_id = response_create.json().get('userId')

        # Get post from user
        self.client.get(f'posts/{post_id}')

        # Delete user
        self.client.delete(f'posts/{post_id}')

    @tag('locust_with')
    @task
    def locust_with(self):
        fake = Faker()

        user_id = random.randint(1,4)

        payload = {
            'userId': user_id,
            'title': fake.name(),
            'body': fake.sentence()}

        with self.client.post('posts', data=payload, catch_response=True, name=f'create user with id{user_id}') as response:
            print(response.status_code)
            if user_id == 2:
                response.failure(f'we don"t use user with id {user_id}')

            if user_id == 3:
                raise MyException("We can't create post")

        post_id = response.json().get('userId')

        # Get post from user
        self.client.get(f'posts/{post_id}')

        # Delete user
        self.client.delete(f'posts/{post_id}')