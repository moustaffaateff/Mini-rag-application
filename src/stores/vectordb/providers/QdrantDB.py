from qdrant import models ,QdrantClient 
from ..VectoDBInterface import VectorDBInterface 
from logging import Logger 


class QdrantDB (VectorDBInterface):
    def __init__(self , db_path, distance_method ) :

        self.client= None 
        self.db_path= db_path
        self.distance_method = None
        
    