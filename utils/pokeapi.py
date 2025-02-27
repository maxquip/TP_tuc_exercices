import requests

base_url = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']

def get_pokemon_stats(api_id):
    """
        Get pokemon stats from the API pokeapi
    """
    return False

def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{base_url}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_api_id, second_api_id):
    """
        Do battle between 2 pokemons
    """
    premierPokemon = get_pokemon_data(first_api_id)
    secondPokemon = get_pokemon_data(second_api_id)
    battle_result = 0
    return premierPokemon if battle_result > 0 else secondPokemon if battle_result < 0 else {'winner': 'draw'}


def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stat between two pokemons
    """

    poke_1_wins = 0
    poke_2_wins = 0
    print(first_pokemon_stats)
    for stat_poke_1, stat_poke_2 in zip(first_pokemon_stats, second_pokemon_stats):
        if(stat_poke_1["base_stat"] > stat_poke_2["base_stat"]):
            poke_1_wins += 1
        elif (stat_poke_2["base_stat"] > stat_poke_1["base_stat"]):
            poke_2_wins += 1
        else:
            pass

    if(poke_1_wins > poke_2_wins):
        return f"pokemon 1 wins / Score: pokemon 1: {poke_1_wins} - pokemon 2: {poke_2_wins}"
    else:
        return f"pokemon 2 wins / Score: pokemon 1: {poke_1_wins} - pokemon 2: {poke_2_wins}"
