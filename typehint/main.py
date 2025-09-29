from typing import List,Optional,SupportsInt, Tuple, Dict
from enum import Enum
from datetime import datetime
import time

price: List[int]=[12,13]
price: Tuple[int,int,int]
price: Dict[str,int]
def even_numbers():
    i = 0
    while i <= 20:
        yield i
        i += 2

even_numbers()


class Language(str, Enum):
    PY="python"
    JS = "JavaScript"


from pydantic import BaseModel, Field,field_validator,model_validator
class Blog(BaseModel):
    title:str= Field(min_length=10)
    is_active:bool
    description: Optional[str]=None
    lang:Language=Language.PY
    time:datetime=datetime.now()

blog=Blog(title="jdbhhhhhhhhhhjh",is_active=True)
print(blog)


blog.model_dump_json()



