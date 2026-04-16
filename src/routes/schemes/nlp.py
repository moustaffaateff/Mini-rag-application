from pydantic import BaseModel
from typing import Optional


class PushRequest (BaseModel) : 
    do_reest : Optional[int] = 0
    

