from locust import task, HttpUser
import random

url = '/object'


class ObjectUser(HttpUser):
    response = None
    name_object = None
    id_object = None

    def on_start(self) -> None:
        body = {
            "data": {"color": "silver", "size": "large"},
            "name": "Objects locust"
        }
        self.response = self.client.post(url=url, json=body)
        self.name_object = self.response.json()['name']
        self.id_object = self.response.json()['id']

    @task(1)
    def get_all_objects(self):
        self.client.get(url=f'{url}')

    @task(3)
    def get_one_object(self):
        self.client.get(
            url=f'{url}/{random.choices([1220, 1, 1221, 1223, 1224, 1225])}'
        )

    @task(1)
    def put_object(self):
        body = {
            "data": {"color": "violet", "size": "LS"},
            "name": "Objects locust put"
        }
        self.client.put(url=f'{url}/{self.id_object}', json=body)
