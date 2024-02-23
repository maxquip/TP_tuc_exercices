# from datetime import date
# import unittest
# from unittest.mock import MagicMock
# from fastapi.testclient import TestClient
# from httpx import patch
# from app import schemas
# from main import app 

# class TestCreateTrainerEndpoint(unittest.TestCase):
#     def setUp(self):
#         self.client = TestClient(app)

#     # @patch('TP_tru_examen.app.actions.create_trainer')
#     # def test_create_trainer(self, mock_create_trainer):
#     #     # Define the return value of the mock function
#     #     mock_create_trainer.return_value = schemas.TrainerBase(
#     #         name="John Doe",
#     #         birthdate=date(1990, 1, 1)
#     #     )

#     #     # Create a sample trainer data
#     #     trainer_data = {
#     #         "name": "John Doe",
#     #         "birthdate": "1990-01-01"
#     #     }

#         # Send a POST request to the endpoint with the sample trainer data
#         # response = self.client.post("/", json=trainer_data)

#         # Check if the request was successful (status code 200)
#         # self.assertEqual(response.status_code, 200)

#         # # Check if the response contains the expected data
#         # created_trainer = response.json()
#         # self.assertEqual(created_trainer["name"], "John Doe")
#         # self.assertEqual(created_trainer["birthdate"], "1990-01-01")

# # @patch('app.routers.trainers')
# # def test_create_trainer(self, mock_create_trainer):
# #     '''
# #     Should post a trainer
# #     '''
# #     # Mock the create_trainer function to return a mock trainer
# #     mock_trainer = MagicMock()
# #     mock_trainer.name = "Ash Ketchum"
# #     mock_trainer.birthdate = "1990-05-04"
# #     mock_create_trainer.return_value = mock_trainer
# #     # Make the request to create a trainer
# #     response = self.client.post("/", json={"name": "Ash Ketchum", "birthdate": "1990-05-04"})
# #     # Check if the request was successful (status code 200)
# #     self.assertEqual(response.status_code, 200)
# #     # Check if the response data matches the expected data
# #     created_trainer = response.json()
# #     self.assertEqual(created_trainer["name"], "Ash Ketchum")
# #     self.assertEqual(created_trainer["birthdate"], "1990-05-04")

#     def test_get_trainers(self):
#         response_data =  [
#   {
#     "name": "trainer0",
#     "birthdate": "1995-01-11",
#     "id": 1,
#     "inventory": [],
#     "pokemons": []
#   },
#   {
#     "name": "trainer1",
#     "birthdate": "1995-01-11",
#     "id": 2,
#     "inventory": [],
#     "pokemons": []
#   },
#   {
#     "name": "trainer2",
#     "birthdate": "1995-01-11",
#     "id": 3,
#     "inventory": [],
#     "pokemons": []
#   },
#   {
#     "name": "trainer3",
#     "birthdate": "1995-01-11",
#     "id": 4,
#     "inventory": [],
#     "pokemons": []
#   },
#   {
#     "name": "trainer4",
#     "birthdate": "1995-01-11",
#     "id": 5,
#     "inventory": [],
#     "pokemons": []
#   },
#   {
#     "name": "trainer5",
#     "birthdate": "1995-01-11",
#     "id": 6,
#     "inventory": [],
#     "pokemons": []
#   },
#   {
#     "name": "trainer6",
#     "birthdate": "1995-01-11",
#     "id": 7,
#     "inventory": [],
#     "pokemons": []
#   },
#   {
#     "name": "trainer7",
#     "birthdate": "1995-01-11",
#     "id": 8,
#     "inventory": [],
#     "pokemons": []
#   },
#   {
#     "name": "trainer8",
#     "birthdate": "1995-01-11",
#     "id": 9,
#     "inventory": [],
#     "pokemons": []
#   },
#   {
#     "name": "trainer9",
#     "birthdate": "1995-01-11",
#     "id": 10,
#     "inventory": [],
#     "pokemons": []
#   },
#   {
#     "name": "Ash Ketchum",
#     "birthdate": "1990-05-04",
#     "id": 11,
#     "inventory": [],
#     "pokemons": []
#   },
#   {
#     "name": "John Doe",
#     "birthdate": "1990-01-01",
#     "id": 12,
#     "inventory": [],
#     "pokemons": []
#   }
# ]

#         response = self.client.get("/trainers")

#         self.assertEqual(response.status_code, 200)
        
#         trainers = response.json()
#         self.assertEqual(trainers, response_data)

# if __name__ == '__main__':
#     unittest.main()
