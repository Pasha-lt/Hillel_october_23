from locust import SequentialTaskSet, task, HttpUser, constant


class PostSet(SequentialTaskSet):
    @task
    def get_all_posts(self):
        self.client.get('posts')
        print('get posts')

class CommentsSet(SequentialTaskSet):
    @task
    def get_comments(self):
        self.client.get('comments')
        print('get comments')

class TodoSet(SequentialTaskSet):
    @task
    def get_all_todo(self):
        self.client.get('todos')
        print('get todos')


class LoadTest(HttpUser):
    host = 'https://jsonplaceholder.typicode.com/'
    tasks = [PostSet, CommentsSet, TodoSet]
    wait_time = constant(1)