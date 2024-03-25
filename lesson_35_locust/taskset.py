from locust import TaskSet, task, HttpUser, constant


class PostSet(TaskSet):
    @task
    def get_all_posts(self):
        self.client.get('posts')
        print('get posts')

class CommentsSet(TaskSet):
    @task
    def get_comments(self):
        self.client.get('comments')
        print('get comments')

class TodoSet(TaskSet):
    @task
    def get_all_todo(self):
        self.client.get('todos')
        print('get todos')

class LoadTest(HttpUser):
    host = 'https://jsonplaceholder.typicode.com/'
    tasks = [PostSet, CommentsSet, TodoSet]
    wait_time = constant(2)