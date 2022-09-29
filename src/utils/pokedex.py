import json
from src import core
from src.db.database import Database
from typing import Any
from src.schemas.pokedex import PokedexCreate


def insert_pokedex() -> None:
    database: Any = Database.get_db()
    if core.pokedex.does_exists(db=database, query=dict({})) is False:
        with open('src/mocks/pokedex.json') as json_lines:
            pokedex = json.load(json_lines)
            for config in pokedex:
                insert_config: PokedexCreate = PokedexCreate(
                    name=config['name'],
                    age=config['age'],
                    working_time=config['working_time'],
                    proficiency=config['proficiency'],
                    skills=config['skills']
                )
                print(core.pokedex.create(db=database, obj_in=insert_config))
