import unittest
import sys
import os
from unittest.mock import MagicMock, call, patch

from fastapi.testclient import TestClient
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, project_root)

from app.utils.pokeapi import get_pokemon_data, battle_compare_stats
from app.actions import add_trainer_pokemon
from ..main import app


class TestGetPokemonData(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.client = TestClient(app)

    @patch('app.utils.pokeapi.requests.get')
    def test_get_pokemon_data(self, mock_get):
        expected_json = {'name': 'Pikachu', 'id': 25,}
        mock_get.return_value.json.return_value = expected_json
        
        result = get_pokemon_data(25)
        
        mock_get.assert_called_once_with('https://pokeapi.co/api/v2/pokemon/25', timeout=10)
        
        self.assertEqual(result, expected_json)

    def test_pokemon_1_wins(self):
        first_stats = [{"base_stat": 50}, {"base_stat": 60}, {"base_stat": 70}]
        second_stats = [{"base_stat": 40}, {"base_stat": 50}, {"base_stat": 60}]
        result = battle_compare_stats(first_stats, second_stats)
        self.assertEqual(result, "pokemon 1 wins / Score: pokemon 1: 3 - pokemon 2: 0")

    def test_pokemon_2_wins(self):
        first_stats = [{"base_stat": 40}, {"base_stat": 50}, {"base_stat": 60}]
        second_stats = [{"base_stat": 50}, {"base_stat": 60}, {"base_stat": 70}]
        result = battle_compare_stats(first_stats, second_stats)
        self.assertEqual(result, "pokemon 2 wins / Score: pokemon 1: 0 - pokemon 2: 3")

    def test_draw(self):
        first_stats = [{"base_stat": 50}, {"base_stat": 60}, {"base_stat": 70}]
        second_stats = [{"base_stat": 50}, {"base_stat": 60}, {"base_stat": 70}]
        result = battle_compare_stats(first_stats, second_stats)
        self.assertEqual(result, "pokemon 2 wins / Score: pokemon 1: 0 - pokemon 2: 0")

    def test_add_trainer_pokemon(self):
        database_mock = MagicMock()

        class PokemonCreateMock:
            def __init__(self, api_id):
                self.api_id = api_id
            def model_dump(self):
                return {'api_id': self.api_id}

        pokemon_data = {'api_id': 25}
        trainer_id = 1

        result = add_trainer_pokemon(database_mock, PokemonCreateMock(pokemon_data['api_id']), trainer_id)

        database_mock.refresh.assert_called_once_with(result) 
        
    def test_get_traine_pokemons(self):
        response = self.client.get("/pokemons")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
