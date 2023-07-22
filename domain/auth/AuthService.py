import bcrypt
import jwt
from starlette.responses import JSONResponse

from domain.user.UserRepository import UserRepository


class AuthService:
    userRepository = UserRepository()

    async def createUser(self, registerUserDto):
        # TODO: v1에선 평문 암호 입력
        # TODO: v2에선 bcrypt를 이용한 암호화 후 암호 입력합니다.

        return await self.userRepository.createUser(registerUserDto)

    async def createUser2(self, registerUserDto):
        name = registerUserDto.name
        username = registerUserDto.username
        password = registerUserDto.password
        hashedPassword = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        print(hashedPassword)
        return await self.userRepository.createUser(name, username, hashedPassword)

    # 첫 스텝에서 간단한 형태의 집접 비교 형식 validation 메소드
    async def validate(self, userLogInDto):
        hashedPassword = await self.userRepository.findUser(userLogInDto.username)
        print(userLogInDto.password)
        print(hashedPassword.password)
        if bcrypt.checkpw(userLogInDto.password.encode("utf-8"), hashedPassword.password.encode("utf-8")):
            print("로긴 성공 ㅎㅎ")
        else:
            print("틀렸다 이자식아")

    async def authenticate(self, userLogInDto):
        hashedPassword = await self.userRepository.findUser(userLogInDto.username)
        pydanticToJson = {
            "username": userLogInDto.username,
            "password": userLogInDto.password
        }
        if bcrypt.checkpw(userLogInDto.password.encode("utf-8"), hashedPassword.password.encode("utf-8")):
            jwtToken = jwt.encode(
                pydanticToJson,
                "secret",
                algorithm="HS256")
            return JSONResponse({"access_token": jwtToken})
        else:
            return JSONResponse("LogInFailed", status_code=404)

    async def getMe(self, token):
        payload = jwt.decode(token, "secret", algorithms="HS256")
        user = await self.userRepository.findUser(payload.get("username"))
        return user
