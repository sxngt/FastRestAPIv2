from typing import Annotated

import bcrypt
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi_restful.cbv import cbv

from domain.auth.AuthService import AuthService
from domain.user.dto.RegisterUserDto import RegisterUserDto
from domain.user.dto.userLoginDto import UserLogInDto

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/api/user"
)


@cbv(router)
class UserController:
    authService: AuthService = Depends(AuthService)

    @router.post("/register")
    async def createUser(self, registerUserDto: RegisterUserDto):
        print(registerUserDto)
        await self.authService.createUser2(registerUserDto)

    @router.post("/login")
    async def validateUser(self, userLogInDto: UserLogInDto):
        return await self.authService.authenticate(userLogInDto)

    @router.get("/getme")
    async def getMe(self, token: Annotated[str, Depends(oauth2_scheme)]):
        print(token)
        return await self.authService.getMe(token)
