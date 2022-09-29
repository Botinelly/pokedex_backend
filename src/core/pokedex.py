from typing import Any, List
from src.core.base import CRUDBase
from src.schemas.pokedex import PokedexCreate
from src.config.config import settings


class CRUDPokedex(CRUDBase[PokedexCreate]):
    def aggregate(self, db: Any, pipeline: List):
        return db[self.collection].aggregate(pipeline)

    def insert_new(self, db, usr: PokedexCreate):
        try:
            del usr.id
            if not self.does_exists(db, {"name": usr.name}):
                inserted = self.create(db, usr.__dict__)
                return inserted
            return False
        except Exception as err:
            print("error creating new", err)
            return False
    
    def get_all(self, db):
        all_usr = self.get(db=db, query={})
        for poke in all_usr:
            poke["_id"] = str(poke["_id"])
            print(poke)
        print(all_usr)
        return all_usr

pokedex = CRUDPokedex(settings.POKEDEX_COLLECTION)
