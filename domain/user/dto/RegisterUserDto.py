from pydantic import BaseModel, Field, validator


class RegisterUserDto(BaseModel):
    # 한글만 가능 (자음 불가능)
    name: str = Field(title="이름", regex="^[가-힣]+$")
    # 영문만 가능
    username: str = Field(regex="^[a-zA-Z]+$")
    # 4~12자 영문소문자, 숫자, 언더라인(_) 사용가능
    password: str = Field(regex="^[a-z0-9_]{4,12}$")

    @validator('name')
    def name_joke(cls, v):
        if "장난" in v:
            raise ValueError('넌 이름이 장난이냐')
        return v
