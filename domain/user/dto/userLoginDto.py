from pydantic import BaseModel


class UserLogInDto(BaseModel):
    username: str
    password: str