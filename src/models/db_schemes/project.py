from pydantic import BaseModel ,Field , validator
from typing import Optional
from bson.objectid import ObjectId 

class Project ( BaseModel ) : 
    id: Optional[ObjectId] = Field(None, alias="_id")
    project_id : str =Field(...,min_length=1)

    @validator("project_id")
    def validate_project_id( cls , value ): 
        if not value.isalnum() :
            raise ValueError ('project is must be alpha numeric') 
        
        return value 

    class Config:
        arbitrary_types_allowed = True   # To make pydantic ignore the (objectid) data type created by mongo for every document in the collection 

        # allow using 'id' to fill '_id' and vice versa
        allow_population_by_field_name = True      
            