from datetime import date
import json
from app import models, schemas
from app.sqlite import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

def get_db():
    """
        Get the DB
    """
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()



def age_from_birthdate(birthdate):
    """
        Return an age from a birthday
    """
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day)
        < (birthdate.month, birthdate.day))

def create_random_trianer(name: str, birthdate: str):
   return schemas.TrainerCreate(name=name, birthdate=date.fromisoformat(birthdate))
        
def create_pokemon_init(poke_id: int, cust_name: str):
    return schemas.PokemonBase(api_id=poke_id, custom_name=cust_name)