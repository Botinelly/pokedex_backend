from bson import ObjectId
from typing import Any, List
from fastapi import APIRouter, Depends, status
from src.schemas.pokedex import PokedexCreate
from src import core
from src.db.database import Database

router = APIRouter()


@router.post("/insert",
    status_code=status.HTTP_200_OK
)
def insert(
    *,
    db: Any = Depends(Database.get_db),
    user: PokedexCreate
) -> Any:
    print("db", db)
    return core.pokedex.insert_new(db=db, usr=user)


@router.get(
    "/get_all",
    status_code=status.HTTP_200_OK
)
def get_all(
    *,
    db: Any = Depends(Database.get_db)
) -> Any:
    return core.pokedex.get_all(db)


@router.put(
    "/update",
    status_code=status.HTTP_200_OK,
)
def update(
    *,
    db: Any = Depends(Database.get_db),
    user: PokedexCreate
) -> Any:
    print(user)
    try:
        core.pokedex.update(db, data={
            "id": {"_id": user.id},
            "query": {
                '$set': {
                    "name": user.name,
                    "age": user.age,
                    "working_time": user.working_time,
                    "proficiency": user.proficiency,
                    "skills": user.skills
                    }
            }
        })
        return True
    except Exception as err:
        print("error in update endpoint", err)
        return False

@router.delete(
    "/delete",
    status_code=status.HTTP_200_OK
)
def delete(
    *,
    db: Any = Depends(Database.get_db),
    ids: List[str]
) -> Any:
    try:
        for id in ids:
            core.pokedex.remove(db, query={
                "_id": ObjectId(id)
            })
        return True
    except Exception as err:
        print("error deleting", err)
        return False
