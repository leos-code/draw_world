from typing import Any, Optional
from pydantic import BaseModel

class Response(BaseModel):
    code: Optional[int] = 0
    msg: Optional[str] = ""
    data: Optional[Any] = None
    