from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app import actions, schemas
from app.utils.pokeapi import battle_compare_stats, get_pokemon_data, get_pokemon_stats
from app.utils.utils import get_db
import requests
import random

router = APIRouter()

@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all pokemons
        Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons

@router.get("/battle/{pokemon1}/{pokemon2}")
def pokemons_batter(pokemon1: int, pokemon2:int, database: Session = Depends(get_db)):
    get_pokemon_1_db = actions.get_pokemon(database, pokemon_id=pokemon1).api_id
    get_pokemon_2_db = actions.get_pokemon(database, pokemon_id=pokemon2).api_id


    pokemon_stat_1 = get_pokemon_data(get_pokemon_1_db)
    pokemon_stat_2 = get_pokemon_data(get_pokemon_2_db)
    return battle_compare_stats(pokemon_stat_1["stats"], pokemon_stat_2["stats"])

@router.get("/randomPokemon")
def random_pokemons():
    pokemon_list = []
    pokemons = [str(random.randint(1, 100)) for _ in range(3)]

    for pokemon in pokemons:
        request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        pokemon_data = request.json()
        pokemon_info = {
            'name': pokemon_data['name'],
            'stats': [{'stat': stat['stat']['name'], 'base_stat': stat['base_stat']} for stat in pokemon_data['stats']]
        }
        pokemon_list.append(pokemon_info)
    return pokemon_list
