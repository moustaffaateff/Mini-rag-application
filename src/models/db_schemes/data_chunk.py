from pydantic import BaseModel ,Field , validator
from typing import Optional
from bson.objectid import ObjectId 


class DataChunk (BaseModel): 
    _id : Optional[ObjectId]
    chunk_text :str = Field(... , min_length = 1)
    chunk_metadata : dict
    chunk_order : int = Field(... , gt = 0 )
    chunk_project_id  : ObjectId                           






    class Config :
        arbitrary_types_allowed = True      # To make pydantic ignore the (objectid) data type created by mongo for every document in the collection 
        


    @classmethod
    def get_indexes(cls):
        return [
            {
                "key": [
                    ("chunk_project_id", 1)
                ],
                "name": "chunk_project_id_index_1",
                "unique": False
            }
        ]