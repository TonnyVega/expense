from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel

class Expense(BaseModel):
    id: Optional[UUID] =  uuid4()
    name : str
    category :str
    amount :int
    date :  str

