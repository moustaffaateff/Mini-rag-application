from enum import Enum

class LLMEnums(Enum):
    OPENAI = "OPENAI"
    COHERE = "COHERE"

class OpenAIEnums(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

class CoHereEnums(Enum):
    SYSTEM = "SYSTEM"
    USER = "USER"
    ASSISTANT = "CHATBOT"


    # its is different if the embeded part is a chunk of data or user input 
    DOCUMENT = "search_document"  #Datachunk
    QUERY = "search_query"        #User prompt


class DocumentTypeEnum(Enum):
    DOCUMENT = "document"
    QUERY = "query"