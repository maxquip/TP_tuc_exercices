import random
from locust import HttpUser, task, between

class TrainersTest(HttpUser):
    wait_time= between(1, 5)
    @task
    def get_trainers(self):
        self.client.get('/trainers')


    @task(3)
    def post_trainer(self):
        self.client.post("/trainers/", json={"name":"foo", "birthdate":"1995-01-11"})

    @task
    def get_trainer(self):
        self.client.request_name = "/trainer/?id=[id]"
        self.client.get(f'/trainers/{random.randint(0, 10)}')
     
    @task
    def get_all_pokemons(self):
        self.client.get(f'/pokemons/')

    @task
    def pokemon_battle(self):
        self.client.request_name = "/pokemons/battle/?id=[id]"
        self.client.get(f'/pokemons/battle/{random.randint(0, 10)}/{random.randint(0, 10)}')
    