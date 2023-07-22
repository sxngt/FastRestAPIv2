from typing import Optional

from pydantic import BaseModel


class CreateBoardDto(BaseModel):
    name: str
    description: Optional[str] = None
