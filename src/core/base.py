from typing import Any, Dict, Generic, List, TypeVar, Union
from pydantic import BaseModel
from bson import ObjectId


CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
# ReadSchemaType = TypeVar("ReadSchemaType", bound=BaseModel)
# UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
# DeleteSchemaType = TypeVar("DeleteSchemaType", bound=BaseModel)


def add_regex_on_name(query: dict) -> dict:
    """
    change from:
    {"name": "AOC"}
    to:
    {"name": {"$regex": "(?i)^AOC$"}}
    """
    for tuple in query.items():
        k, v = tuple
        if (type(v) is str) and (k == "name"):
            query[k] = {"$regex": "(?i)^" + v + "$"}
        if (type(v) is ObjectId) and (k == "brand_id"):
            query[k] = v

    print(query)
    return query


def convert_nested_to_dict(input: Any) -> dict:
    response: List = []
    for item in input:
        if (type(item[1]) is List) or (type(item[1]) is list):
            response_list: List = []
            for item_list in item[1]:
                if type(item_list) != int:
                    response_list.append(convert_nested_to_dict(item_list))
                else:
                    response_list.append(item_list)
            item = (item[0], response_list)
        response.append(item)
    return dict(response)


class CRUDBase(Generic[CreateSchemaType]):
    def __init__(self, collection):
        self.collection = collection

    def get(self, db: Any, query: dict, sortBy: Any = ''):
        if (len(sortBy) > 0):
            cursor = db[self.collection].find(query).sort(sortBy)
        else:
            cursor = db[self.collection].find(query)
        data = []
        for register in cursor:
            data.append(register)
        return data

    def create(
        self,
        db: Any,
        obj_in: dict
    ):
        try:
            ins = db[self.collection].insert_one(obj_in).inserted_id
            if type(ins) == ObjectId:
                return True
            return False
        except Exception as err:
            print("error in base create", err)
            return False

    def update(self, db: Any, data: dict):
        print(self.collection)
        return db[self.collection].update_one(data['id'], data['query'])

    def remove(self, db: Any, query: dict):
        query = add_regex_on_name(query)
        return db[self.collection].delete_many(query)

    def does_exists(self, db: Any, query: dict):
        query = add_regex_on_name(query)
        return db[self.collection].count_documents(query) > 0
