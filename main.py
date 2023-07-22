from fastapi import FastAPI

from domain.board import BoardController
from domain.user import UserController
from prismaClient import prisma

app = FastAPI()


@app.on_event("startup")
async def startup():
    print('Database connected')
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown():
    print('Database disconnected')
    await prisma.disconnect()


app.include_router(BoardController.router)
app.include_router(UserController.router)

