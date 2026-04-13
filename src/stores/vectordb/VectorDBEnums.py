from enum import ENUM

class VectorDBEnums(ENUM):
    QDRANT = "QDRANT"

class DistanceMethodEnums(ENUM) : 
    COSINE = "cosine"
    DOT = "dot"