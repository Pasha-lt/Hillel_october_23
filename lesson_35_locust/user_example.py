from locust import User, task, between, constant
from calc_for_user_class import calculate_some_data

class MyFirstTest(User):

    # wait_time = constant(2)  # коли є конкретний час на запит
    wait_time = between(2, 7)  # коли хочемо зробити рандомний час запити час на запит

    def on_start(self) -> None: # Сетап
        print('We start our test')

    @task
    def first(self):
       calculate_some_data()
       print('first_test')

    @task
    def second(self):
        calculate_some_data()
        print('first_test')


    def on_stop(self) -> None: # Тердаун
        print('We finished our test')
