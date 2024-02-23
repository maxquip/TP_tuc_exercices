import unittest
from fastapi.testclient import TestClient
import sys
import os
from unittest.mock import MagicMock, call, patch
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, project_root)
from main import app

class TestTrainerByID(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.client = TestClient(app)

    def test_get_trainer_with_valid_id(self):
        response = self.client.get("/trainers/4")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], 4)

    def test_get_trainer_with_invalid_id(self):
        response = self.client.get("/trainers/999")
        self.assertEqual(response.status_code, 404)

    def test_get_trainers(self):
        response = self.client.get("/trainers")
        self.assertEqual(response.status_code, 200)
    


    if __name__ == '__main__':
        unittest.main()