from .BaseController import BaseController
from models.db_schemes import Project , DataChunk
from typing import List
from ..stores.llm.LLMEnums import DocumentTypeEnum


class NLPController(BaseController):
 def __init__(self, vectordb_client, generation_client, embedding_client):
    super().__init__() 
    
    self.vectordb_client = vectordb_client
    self.generation_client = generation_client
    self.embedding_client = embedding_client



def create_collection_name(self, project_id : str ):
  collection_name = f"collection_{project_id}".strip()
  return collection_name

def reset_vectordb_collection (self, project:Project  ):
   
  collection_name = self.create_collection_name( project_id = project.project_id )
  return self.vectordb_client.delete_collection(collection_name =collection_name )

def get_vector_db_collection_info (self, project:Project ):
  collection_name = self.create_collection_name( project_id = project.project_id )  
  collection_info = self.vectordb_client.get_collection_info(collection_name= collection_name)
  return collection_info


def index_into_vector_db (self, project : Project,  chunks : List[DataChunk],
                          do_reset : bool = False ): 
    #Step1 : create collection_name 
    collection_name = self.create_collection_name( project_id = project.project_id )  

    #Step2 : get all chunks items 
    texts = [ c.chunk_text for c in chunks ]
    metadata = [c.chunk_metadata for c in chunks]
    vectors = [self.embedding_client.embed_text(text , document_type = DocumentTypeEnum.DOCUMENT.value )
               for text in texts 
               ] 
    #Step3 : create collection 
    _ =  self.vectordb_client.create_collection( collection_name =collection_name, 
                                    embedding_size = self.embedding_client.embedding_size,
                                    do_reset = do_reset)
    

    #Step4 : write in vectordb every chunk and its embeddings
    self.vectordb_client.insert_many( collection_name = collection_name ,
                                     texts = texts, 
                                    vectors= vectors,
                                     metadata= metadata
                                     )

    return True 
    

    