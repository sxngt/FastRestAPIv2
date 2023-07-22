from fastapi import APIRouter
from fastapi_restful.cbv import cbv

router = APIRouter(
    prefix="/api/user"
)


@cbv(router)
class UserController:
    @router.post("/register")
    def createUser(self):
        return "aa"

    @router.post("/login")
    def validateUser(self):
        return "bb"
