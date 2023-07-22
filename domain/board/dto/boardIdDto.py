from pydantic import BaseModel


class BoardIdDto(BaseModel):
    id: str